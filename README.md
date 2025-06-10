# MetricX – LLM Solution for Industrial Data, Digital Twins, PLM/PDM & XR Integration

**AsciiMetric / MetricX – Official Repository**  
*Digital Strategy, Open Innovation & Confidentiality Governance*

---

## About MetricX

MetricX is a next-generation, modular LLM solution designed to automate, standardize, and enhance the integration of industrial data across CAD, PLM/PDM, and XR ecosystems.  
Built to accelerate the creation of digital twins and support the transition toward Industry 5.0, MetricX leverages advanced local Large Language Models (LLMs), robust standardization, and deep interoperability to bridge the gap between physical and digital assets in complex industrial environments.

**Key features and modules:**
- **Wapi:** Secure, bi-directional data exchange and synchronization with PLM/PDM systems (Teamcenter, Windchill, SAP PLM, 3DEXPERIENCE), ensuring integrity, versioning, and end-to-end traceability.
- **CAD:** Advanced extraction and normalization of native CAD data (PTC Creo, SolidWorks, Siemens NX), supporting both 2D and 3D geometries, assemblies, and engineering metadata.
- **2D Data Extractor:** LLM-powered extraction, contextual correction, and standardization of 2D plans (DXF, PDF, scans) into “Industry Ready” structured files (JSON, STEP, CSV), optimized for quality control and automated integration.
- **3D Data Extractor:** Automated conversion and structuring of 3D model data for digital twin simulation, XR, and advanced analytics—eliminating silos and enabling seamless data flows.
- **XR Integrator:** Generation of output files for XR, AR/VR, and digital twin applications (Unity, Unreal, proprietary engines), contextualizing technical data for immersive visualization, maintenance, and training.

This repository enables public testing, benchmarking, and transparent performance reporting of open MetricX modules, with only anonymized or synthetic data—no proprietary, confidential, or client material is ever included.

---

## Repository Structure

```
metricx/
├── README.md
├── SECURITY.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── ROADMAP.md
├── CHANGELOG.md
├── DISCLOSURE.md
├── COMMERCIAL.md
├── .gitignore
├── docs/
│   ├── index.md
│   └── module_overview.md
├── modules/
│   ├── wapi/
│   ├── cad/
│   ├── dxf_data_extract/
│   ├── step_data_extract/
│   └── ...
├── demos/
│   ├── demo_notebooks/
│   │   └── demo1/
│   │       ├── notebook.ipynb
│   │       └── resources/
│   │           ├── example.drw
│   │           ├── example.prt
│   │           ├── example.dxf
│   │           └── example.step
│   └── demo_scripts/
├── performance_audit/
│   ├── reports/
│   └── test_scripts/
├── examples/
├── public/
│   └── assets/
├── community/
│   ├── discord_invite.md
│   └── contribution_ideas.md
├── scripts/
├── testdata/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── FUNDING.yml
└── private/
```

---

## Usage & Principles

- **Testing & transparency:** Public testing, reproducible demos, and sharing anonymized performance audits for MetricX modules.
- **Digital twin & Industry 5.0:** Practical experimentation for digital twin creation, advanced data integration, and industrial digitalization aligned with Industry 5.0 values.
- **Strict separation:** No proprietary business logic, confidential, or client data is published here. All sensitive code and data remain private.
- **Security & confidentiality:** Strict `.gitignore` and privacy policy. Each resource folder includes a `README.md` describing its contents.
- **Branding & communication:** Centralized communication assets; up-to-date documentation.
- **Contributor experience:** Clear structure, documentation, and community spaces for easy onboarding and safe, constructive contributions.

---

## Organizing Test and Demo Resources

- **Demo notebooks/scripts:** Place all demo resources (e.g., `.drw`, `.prt`, `.dxf`, `.step`) inside `demos/demo_notebooks/demo1/resources/`.
- **General test datasets:** Use `testdata/` for anonymized or synthetic files for automated testing or scripts.
- **Performance audits:** Benchmarking results and scripts are under `performance_audit/`.
- **Never include confidential, client, or proprietary data in any public folder.**
- Document the nature and origin of files in a `README.md` inside each resource folder.

---

## Contributing

1. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
2. Open an issue for questions, suggestions, or bug reports
3. Use only non-proprietary, safe examples in your contributions
4. **Never share** confidential data, credentials, or core business modules here

---

## Useful Links

- [Technical documentation](./docs/)
- [Security & disclosure](./SECURITY.md)
- [Roadmap](./ROADMAP.md)
- [Changelog](./CHANGELOG.md)
- [Commercial policy](./COMMERCIAL.md)
- [AsciiMetric Linktree](https://linktr.ee/AsciiMetric)  
- Contact: via GitHub issues or the official website form

---

## About

This repository supports open testing, demonstration, and transparent performance communication for MetricX modules, in line with AsciiMetric’s digital strategy:  
- Community openness  
- Technical proof for partners, clients, and recruiters  
- Exemplary security, confidentiality & governance

For specific requests, advanced module access, or collaboration: use the official contact form or provided email addresses.

---

**Official MetricX page:** [www.asciimetric.stuio/metricx_EN.html](http://www.asciimetric.stuio/metricx_EN.html)  
**AsciiMetric Freelance Official Website:** [www.asciimetric.studio](http://www.asciimetric.studio)  
**LinkedIn Page:** [https://www.linkedin.com/company/asciimetricservices](https://www.linkedin.com/company/asciimetricservices)  
**Created by Silan Laurent**  
**LinkedIn Profile:** [https://www.linkedin.com/in/lsilan/](https://www.linkedin.com/in/lsilan/)
