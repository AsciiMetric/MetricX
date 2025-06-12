#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ezdxf
import json
import os
import argparse
import re
from datetime import datetime, timezone
import math
import requests

from pdf2image import convert_from_path
import numpy as np
from paddleocr import PaddleOCR

try:
    import fitz
    PDF_VECTOR_AVAILABLE = True
except ImportError:
    PDF_VECTOR_AVAILABLE = False

DEMO_MODE = True
AUDIT_LOG = []

METRICX_ASCII_LOGO = r"""
++++++++++++               ++++++++++++                                                                                       +++++++++++            +++++++++++
+++++++++++++             +++++++++++++                                                                                        ++++++++++++        ++++++++++++ 
+++++++++++++++         +++++++++++++++                                                                                          ++++++++++++    ++++++++++++   
++++++++++++++++       ++++++++++++++++                                                                                           +++++++++++++ +++++++++++     
+++++++++++++++++     +++++++++++++++++   ++++++++++++++++++ ++++++++++++++++++++ +++++++++++++++++   +++++++    +++++++++++++       ++++++++++++++++++++       
+++++++++++++++++++ +++++++++++++++++++   ++++++++++++++++++ ++++++++++++++++++++ +++++++++++++++++++ +++++++  ++++++++++++++++++     +++++++++++++++++         
+++++++++++++++++++++++++++++++++++++++   +++++++            ++++++++++++++++++++ +++++++++++++++++++ +++++++ ++++++++++++++++++++      +++++++++++++           
+++++++++++++++++++++++++++++++++++++++   ++++++++++++++++++       +++++++        ++++++      +++++++++++++++ ++++++       +++++++     ++++++++++++++++         
++++++++++ +++++++++++++++++ ++++++++++   ++++++++++++++++++       +++++++        +++++++++++++++++++ +++++++ ++++++                 ++++++++++++++++++++       
++++++++++   +++++++++++++   ++++++++++   +++++++                  +++++++        +++++++++++++++++   +++++++ ++++++++++++++++++++ ++++++++++++++++++++++++     
++++++++++    +++++++++++    ++++++++++   ++++++++++++++++++       +++++++        ++++++    ++++++++  +++++++  ++++++++++++++++++++++++++++++   +++++++++++++   
++++++++++     +++++++++     ++++++++++   ++++++++++++++++++       +++++++        ++++++      +++++++ +++++++   ++++++++++++++++++++++++++++      +++++++++++++ 
+++++++++        +++++        +++++++++                                                                                        ++++++++++++          ++++++++++++
"""

def utc_now_str():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def log_console(msg):
    print(f"\033[1;32m[Module C | {utc_now_str()}]\033[0m {msg}")
    AUDIT_LOG.append(f"{utc_now_str()} | {msg}")

def parse_args():
    parser = argparse.ArgumentParser(description="Module C - DXF Extraction Engine + OCR + Vector PDF Extraction + LLM AI Correction (Demo Mode)")
    parser.add_argument('-i', '--input_dxf', required=True,
                        help='F:/MetricX_beta_0.1/CAD_datas/M0166-05-0001-00/m0166-05-0001-00.dxf')
    parser.add_argument('-t', '--input_template', required=True,
                        help='F:/MetricX_beta_0.1/CAD_datas/json_based_standard_file/base_file_template_01.1.json')
    parser.add_argument('-o', '--output_json', required=True,
                        help='F:/MetricX_beta_0.1/dxf_datas_extract/demo/Module_C_LLM-v1.json')
    parser.add_argument('-l', '--output_log', required=True,
                        help='F:/MetricX_beta_0.1/dxf_datas_extract/demo/Module_C_LLM-v1.log')
    parser.add_argument('--pdf', required=True,
                        help='F:/MetricX_beta_0.1/CAD_datas/M0166-05-0001-00/m0166-05-0001-00.pdf')
    parser.add_argument('--ollama_model', default="mistral", help="Ollama LLM model name (e.g. mistral, llama3)")
    parser.add_argument('--ollama_url', default="http://localhost:11434/api/chat", help="Ollama API URL")
    return parser.parse_args()

args = parse_args()
INPUT_DXF = args.input_dxf
INPUT_TEMPLATE = args.input_template
OUTPUT_JSON = args.output_json
OUTPUT_ENTITY_LOG = args.output_log
INPUT_PDF = args.pdf
OLLAMA_MODEL = args.ollama_model
OLLAMA_URL = args.ollama_url

DATUM_CHARS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DATUM_LAYERS = ["_DXF_DATUM", "_DXF_DIMENSION", "_DXF_TEXT", "_DXF_LABEL"]

def fix_corrupted_symbols(obj):
    if isinstance(obj, dict):
        return {k: fix_corrupted_symbols(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [fix_corrupted_symbols(x) for x in obj]
    elif isinstance(obj, str):
        patterns = [
            (r"â– ", "■"),
            (r"â\s*–\s* ", "■"),
            (r"â§«", "⧫"),
            (r"â\s*§\s*«", "⧫"),
            (r"Ã˜", "Ø"),
            (r"Ã\s*Ø", "Ø"),
            (r"âŒ–", "⌖"),
            (r"â\s*Œ\s*–", "⌖"),
            (r"â“‚", "Ⓜ"),
            (r"â\s*“\s*‚", "Ⓜ"),
        ]
        for pat, rep in patterns:
            obj = re.sub(pat, rep, obj)
        return obj
    else:
        return obj

def extract_text_entities(msp):
    res = []
    for ent in msp:
        if ent.dxftype() in ["TEXT", "MTEXT", "ATTRIB"]:
            txt = ent.dxf.text.strip() if ent.dxftype() != "MTEXT" else ent.text.strip()
            pos = (float(ent.dxf.insert.x), float(ent.dxf.insert.y))
            handle = getattr(ent.dxf, "handle", "")
            layer = getattr(ent.dxf, "layer", "")
            res.append({"text": txt, "pos": pos, "handle": handle, "layer": layer, "type": ent.dxftype(), "Z": False})
    log_console(f"DXF TEXT ENTITY EXTRACTION: {len(res)} text entities parsed from drawing.")
    return res

def extract_blocks(doc):
    blocks = {}
    for blk in doc.blocks:
        ents = []
        for ent in blk:
            ent_type = ent.dxftype()
            if ent_type in ["TEXT", "MTEXT", "ATTRIB"]:
                txt = ent.dxf.text.strip() if ent_type != "MTEXT" else ent.text.strip()
                pos = (float(ent.dxf.insert.x), float(ent.dxf.insert.y))
                handle = getattr(ent.dxf, "handle", "")
                layer = getattr(ent.dxf, "layer", "")
                ents.append({"text": txt, "pos": pos, "handle": handle, "layer": layer, "type": ent_type, "Z": False})
            elif ent_type in ["LWPOLYLINE", "POLYLINE"]:
                points = [(float(x), float(y)) for x, y, *_ in ent.get_points()]
                handle = getattr(ent.dxf, "handle", "")
                layer = getattr(ent.dxf, "layer", "")
                ents.append({"poly_points": points, "handle": handle, "layer": layer, "type": ent_type, "Z": False})
            elif ent_type == "LINE":
                start = (float(ent.dxf.start.x), float(ent.dxf.end.y))
                end = (float(ent.dxf.end.x), float(ent.dxf.end.y))
                handle = getattr(ent.dxf, "handle", "")
                layer = getattr(ent.dxf, "layer", "")
                ents.append({"start": start, "end": end, "handle": handle, "layer": layer, "type": ent_type, "Z": False})
        blocks[blk.name] = ents
    log_console(f"BLOCK EXTRACTION: {len(blocks)} DXF blocks parsed (for advanced geometry/arrows).")
    return blocks

def extract_inserts(msp):
    inserts = []
    for ent in msp:
        if ent.dxftype() == "INSERT":
            name = ent.dxf.name
            pos = (float(ent.dxf.insert.x), float(ent.dxf.insert.y))
            handle = getattr(ent.dxf, "handle", "")
            layer = getattr(ent.dxf, "layer", "")
            attribs = []
            for attrib in getattr(ent, "attribs", []):
                attribs.append({
                    "text": attrib.dxf.text.strip(),
                    "pos": (float(attrib.dxf.insert.x), float(attrib.dxf.insert.y)),
                    "handle": getattr(attrib.dxf, "handle", ""),
                    "layer": getattr(attrib.dxf, "layer", ""),
                    "type": "ATTRIB",
                    "Z": False
                })
            inserts.append({"name": name, "pos": pos, "handle": handle, "layer": layer, "attribs": attribs, "Z": False})
    log_console(f"INSERTS: {len(inserts)} block insertions found in model space.")
    return inserts

def extract_dxf_dimensions(msp):
    dims = []
    for ent in msp:
        if ent.dxftype() == "DIMENSION":
            dimtype = getattr(ent.dxf, "dimension_type", None)
            dimtxt = getattr(ent.dxf, "text", "")
            measured = getattr(ent.dxf, "measurement", None)
            layer = getattr(ent.dxf, "layer", "")
            handle = getattr(ent.dxf, "handle", "")
            pos = getattr(ent.dxf, "defpoint", None)
            pos = (float(pos.x), float(pos.y)) if pos else None
            dims.append({
                "type": "DIMENSION",
                "dimension_type": dimtype,
                "text": dimtxt,
                "measured": measured,
                "pos": pos,
                "layer": layer,
                "handle": handle,
                "Z": False
            })
    log_console(f"DXF DIMENSIONS: {len(dims)} dimension entities detected.")
    return dims

# ... (Ajoute ici toutes les autres fonctions du pipeline d'enrichissement, mapping, postprocessing, OCR, LLM, etc.
# Tu peux coller la suite du script ici, ou demander à ce que je la poursuive dans un second message.)

def main():
    print("\033[1;36m"+METRICX_ASCII_LOGO+"\033[0m")
    log_console("=== LAUNCHING: Module C DXF Extraction Engine [AI-Enhanced Demo Mode] ===")
    log_console(f"Loading DXF: {INPUT_DXF}")
    try:
        doc = ezdxf.readfile(INPUT_DXF)
        msp = doc.modelspace()
    except Exception as e:
        log_console(f"[ERR] Unable to open DXF: {e}")
        sys.exit(1)

    log_console("Step 1: Extracting entities from DXF...")
    texts = extract_text_entities(msp)
    blocks = extract_blocks(doc)
    inserts = extract_inserts(msp)
    dims = extract_dxf_dimensions(msp)

    # ... (Continue le pipeline complet ici: OCR, enrichissements, associations, exports, etc.)

if __name__ == "__main__":
    main()