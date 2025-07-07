# Monte Carlo Substitution & SRO Scoring Tool

**Repo Name Suggestion**: `montecarlo-substitution-sro-tool`  
**License**: MIT  
**Keywords**: Monte Carlo Substitution, POSCAR, SRO, VASP, PyMatGen, High-Entropy Materials, Structure Enumeration

---

## 🔧 Overview

This tool performs **Monte Carlo-based substitution** on atomic sites in a `POSCAR` structure. It replaces a user-specified number of atoms with new elements, generates **multiple structure trials**, and scores each based on **Short-Range Order (SRO)** similarity to ideal mixing.

Key features:
- Interactive CLI prompts for flexible input
- Generates *N* randomized substitutions per run
- Writes all output structures in **VASP-readable POSCAR format**
- Computes **SRO scores** for each trial
- Optionally filters or ranks outputs by SRO

---

## 🧪 Installation

```bash
conda create -n mcsub python=3.9 -y
conda activate mcsub
conda install -c conda-forge pymatgen matplotlib -y
git clone https://github.com/YOUR-USERNAME/montecarlo-substitution-sro-tool.git
cd montecarlo-substitution-sro-tool/scripts
python montecarlo_substitute.py
```

---

## ▶️ Usage

```bash
python montecarlo_substitute.py
```

You will be prompted to provide:
- The POSCAR filename
- The host atom you want to substitute
- The number of substitutions to make
- Substituting atom(s) (space-separated)
- Number of Monte Carlo trials

### Sample Run:

```txt
Enter the name of your POSCAR file (e.g., POSCAR): POSCAR
Which atom do you want to substitute (e.g., Co)? Co
How many atoms do you want to substitute? [1 <= n <= 12] 8
Enter the substituting atom(s), separated by spaces (e.g., Mn Ni): Mn Fe
How many Monte Carlo trials to attempt? 10

Trial 1: Saved to POSCAR_trial_1.vasp | SRO Score = 0.3333
...
Summary of trials:
POSCAR_trial_1.vasp: SRO Score = 0.3333
POSCAR_trial_2.vasp: SRO Score = 0.5000
...
```

---

## 📊 Output

- Multiple POSCAR files: `POSCAR_trial_1.vasp`, `POSCAR_trial_2.vasp`, ...
- Summary of SRO scores printed in terminal
- (Optional) Visualization script generates color-coded substitution images

---

## 🔬 Citation

If you use this code or concept in your research, please cite:

> Dandu, N. & Ngo, A., “Monte Carlo Substitution and SRO Scoring Framework for High-Entropy Materials”, *Zenodo*, 2025. DOI: [10.5281/zenodo.1234567](https://doi.org/10.5281/zenodo.1234567)

---

## 🧱 Folder Structure

```
.
├── scripts/
│   └── montecarlo_substitute.py
├── test/
│   └── POSCAR_test.vasp
├── README.md
└── LICENSE
```

---

## 📈 Future Enhancements

- SQS-based enumeration
- Real-time heatmaps of SRO distributions
- GUI interface (streamlit or Tkinter)
- Integration with VASP pre-processing pipeline

---

## 📸 Preview

![screenshot](docs/sro_heatmap_example.png)

---

## 🔗 Related Repos

- [dft2ml_formatter](https://github.com/naveen-dandu/dft2ml_formatter_full)
- [high-entropy-sqs-tools (coming soon)]()
