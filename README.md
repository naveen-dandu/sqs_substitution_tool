# 🔁 SQS Substitution Tool

[![Documentation Status](https://img.shields.io/badge/docs-online-blue.svg)](https://naveen-dandu.github.io/sqs_substitution_tool/)
[![CI](https://github.com/naveen-dandu/sqs_substitution_tool/actions/workflows/python-package.yml/badge.svg)](https://github.com/naveen-dandu/sqs_substitution_tool/actions)
[![LICENSE](https://img.shields.io/github/license/naveen-dandu/sqs_substitution_tool)](LICENSE)

A substitution-based randomizer for generating VASP-compatible POSCAR files.

A Python-based command-line utility to perform **site substitution** in crystal structures (POSCAR/CONTCAR format), enabling the generation of **Special Quasirandom Structures (SQS)** for binary, ternary, or quaternary materials systems.

---

## 🔍 Overview

This tool automates the substitution of atoms in a crystal lattice with customizable control over:
- **Which elements to replace**
- **How many atoms to substitute**
- Randomized sampling of configurations (without replacement)
- Output format in standard VASP-compatible POSCAR format

---

## 🧪 Use Case

Simulating alloy or doped systems such as:

- Substituting `O` with `S` in ZnO₂
- Generating SQS-like structures for CoBHT by replacing Co atoms with Ni, Mn, or Cu
- Studying defect energetics or composition-dependent electronic structure

---

## 🚀 Installation

```bash
git clone https://github.com/naveen-dandu/sqs_substitution_tool.git
cd sqs_substitution_tool
pip install -r requirements.txt  # optional, if needed
```
---

## 🔀 SQS Substitution Tool
This Python script provides an interactive CLI interface for performing simple SQS-like random substitutions on atoms in a VASP structure (POSCAR) using pymatgen.

## 📦 Features
Select a host atom to substitute
Specify the number of substitutions
Choose multiple elements to substitute with
Performs randomized substitutions over the specified host atom indices
Outputs a modified structure as POSCAR_substituted

---

## 🖥️ Usage

```bash
python sqs_prompt_substitute.py
```

You will be prompted interactively:

```vbnet

Which atom do you want to substitute (e.g., Co)? Co
Found 3 atoms of Co.
How many atoms do you want to substitute? [1 <= n <= 12] 2
Enter substitution elements (e.g., Cu Ni Mn): Cu Mn

✅ Substitution complete. Output written to POSCAR_substituted
🧬 Replacements made:
 - Atom index 1 → Cu
 - Atom index 2 → Mn
```

---

## 📁 Input
Ensure a file named POSCAR_CoBHT is present in the same directory.
This should be a valid VASP POSCAR file readable by pymatgen.

---

## 📤 Output
A new file POSCAR_substituted will be generated with the substituted atoms.

---

## 🛠 Requirements
Python 3.7+
pymatgen

Install via pip:

```bash

pip install pymatgen
```

---

🧠 Features
 Works with any crystal structure containing labeled atoms
 Supports binary, ternary, and quaternary systems
 Tracks replaced atom indices for reproducibility
 Prepares data for machine learning and SQS generation

---

## 📄 License
MIT License. See LICENSE.

---

## 👨‍🔬 Author
Developed by Naveen Dandu, with integration in materials data workflows.

---
## Zenodo DOI

[![DOI](https://zenodo.org/badge/1012158238.svg)](https://doi.org/10.5281/zenodo.15792366)

---

## 📣 Citation

If you use this tool for your research or publication, please cite:

```
@software{sqs_sub_tool,
  author = {Naveen Dandu},
  title = {SQS Substitution Tool},
  year = 2025,
  url = {https://github.com/naveen-dandu/sqs_substitution_tool}
}
```

