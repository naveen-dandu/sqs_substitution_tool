from pymatgen.core import Structure
from pymatgen.io.vasp import Poscar
import random

# === Load structure ===
structure = Structure.from_file("POSCAR_CoBHT")

# === Prompt for atom substitution ===
host = input("Which atom do you want to substitute (e.g., Co)? ").strip()

# Get all indices of that atom
host_indices = [i for i, site in enumerate(structure) if site.specie.symbol == host]
if not host_indices:
    raise ValueError(f"No atoms of type '{host}' found in structure.")

print(f"Found {len(host_indices)} atoms of {host}.")

# How many atoms to substitute
max_replace = len(host_indices)
n_replace = int(input(f"How many atoms do you want to substitute? [1 <= n <= {max_replace}] "))

if not (1 <= n_replace <= max_replace):
    raise ValueError("Invalid number of atoms to replace.")

# What elements to substitute with
subs_input = input("Enter substitution elements (e.g., Cu Ni Mn): ").strip().split()
n_subs = len(subs_input)

# Assign equal fractions by default
replace_indices = random.sample(host_indices, n_replace)
random.shuffle(replace_indices)

per_element = n_replace // n_subs
leftover = n_replace % n_subs

assigned = []
idx = 0
for i, elem in enumerate(subs_input):
    count = per_element + (1 if i < leftover else 0)
    for _ in range(count):
        structure.replace(replace_indices[idx], elem)
        assigned.append((replace_indices[idx], elem))
        idx += 1

# === Output ===
Poscar(structure).write_file("POSCAR_substituted")
print("\n✅ Substitution complete. Output written to POSCAR_substituted")
print("🧬 Replacements made:")
for i, e in assigned:
    print(f" - Atom index {i} → {e}")