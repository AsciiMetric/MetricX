# MetricX

**AsciiMetric / MetricX – Official Repository**  
*Digital Strategy, Open Innovation & Confidentiality Governance*

---

## About MetricX

MetricX is a modular, open-core platform developed to facilitate the integration and creation of digital twins, as well as to support the evolution toward Industry 5.0.  
It offers a unified approach for the management, extraction, and enhancement of CAD, PLM, and XR data, enabling interoperability between physical and digital assets for advanced industrial and engineering use cases.

This repository is provided as a resource to enable testing and benchmarking of MetricX modules, and to transparently communicate selected performance reports for each open module of the solution.  
No proprietary, confidential, or client data is included; only safe, anonymized, or synthetic examples are provided.

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
├── docs/                      # Public technical documentation and usage guides
│   ├── index.md
│   └── module_overview.md
├── modules/                   # Public open-core modules (never proprietary core code)
│   ├── wapi/
│   ├── cad/
│   ├── dxf_data_extract/
│   ├── step_data_extract/
│   └── ...
├── demos/                     # Reproducible demos, notebooks, and sample scripts
│   ├── demo_notebooks/
│   │   └── demo1/
│   │       ├── notebook.ipynb
│   │       └── resources/
│   │           ├── example.drw
│   │           ├── example.prt
│   │           ├── example.dxf
│   │           └── example.step
│   └── demo_scripts/
├── performance_audit/         # Public benchmark & audit reports, performance test scripts (anonymized)
│   ├── reports/
│   └── test_scripts/
├── examples/                  # Safe, non-proprietary sample files for general use
├── public/                    # Public communication assets (logos, images, UI screenshots)
│   └── assets/
├── community/                 # Community information (Discord, contribution ideas, etc.)
│   ├── discord_invite.md
│   └── contribution_ideas.md
├── scripts/                   # Utility scripts (public, non-sensitive)
├── testdata/                  # Anonymized test datasets
├── .github/                   # CI workflows, issue/PR templates, funding
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── FUNDING.yml
└── private/                   # Never on GitHub: core code, sensitive modules, R&D (local only)
```

---

## Usage & Principles

- **Testing & transparency:** This repository is intended for safe public testing, reproducible demonstrations, and sharing anonymized performance audits of MetricX modules.
- **Digital twin & Industry 5.0:** MetricX enables practical experimentation around digital twin creation, advanced data integration, and industrial digitalization in line with Industry 5.0 values.
- **Strict separation:** No proprietary business logic, confidential, or client data is ever published here. All sensitive code and data remain private.
- **Security & confidentiality:** A strict `.gitignore` and privacy policy are enforced. Each resource folder includes a `README.md` stating the nature and origin of its contents.
- **Branding & communication:** All assets for communication (logos, screenshots, etc.) are centralized, and documentation is kept up-to-date for clarity.
- **Contributor experience:** The structure, documentation, and community spaces are designed to simplify onboarding and encourage safe, constructive contributions.

---

## Organizing Test and Demo Resources

- **Demo notebooks/scripts:** Place all resources required for a specific demo (such as `.drw`, `.prt`, `.dxf`, `.step` files) inside a subfolder like `demos/demo_notebooks/demo1/resources/`.
- **General test datasets:** Use `testdata/` for anonymized or synthetic files used in automated testing or scripts.
- **Performance audits:** Results and scripts for benchmarking modules are under `performance_audit/`.
- **Never include confidential, client, or proprietary data in any public folder.**
- Always document the nature and origin of files in a `README.md` inside each resource folder.

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

This repository is provided to support open testing, demonstration, and performance communication around MetricX modules, in line with AsciiMetric’s digital strategy:  
- Community openness  
- Technical proof for partners, clients, and recruiters  
- Exemplary security, confidentiality & governance

For specific requests, access to advanced modules, or collaboration: use the official contact form or the provided email addresses.

---
