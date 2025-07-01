# SQS Substitution Tool 🧬

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

This Python toolkit enables interactive substitution of atoms in POSCAR files (VASP format) for modeling high-entropy or disordered materials using a pseudo-SQS approach.

## 🚀 Features

- Randomized atom substitution via CLI
- Binary, ternary, quaternary support
- Pymatgen-based structure editing
- SQS scoring via `pymatgen.analysis.structure_matcher`
- Jupyter Notebook demo
- Publish-ready POSCAR export

## 🛠 Requirements

```bash
pip install pymatgen
```

## 📦 How to Use

```bash
python scripts/sqs_prompt_substitute.py
```

## 📓 Jupyter Notebook

See [`notebooks/sqs_demo.ipynb`](notebooks/sqs_demo.ipynb) for an interactive demo.

## 🧪 Example

- `POSCAR_CoBHT`: cobalt BHT structure with metal sites ready for substitution

## 📤 Outputs

- `POSCAR_substituted`: Final structure with substitutions
- Optional export to CIF/XYZ formats (future)

## 📘 License

MIT License. Free for academic and commercial use.