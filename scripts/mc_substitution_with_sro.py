import random
from pymatgen.io.vasp import Poscar
from pymatgen.core import Structure
from pymatgen.analysis.local_env import VoronoiNN


def calculate_sro_score(structure, original_site_indices, substitute_map):
    """
    Calculate a simple pairwise Short Range Order (SRO) score.
    The score is based on the fraction of neighbors of each site that are of a different species.
    """
    vnn = VoronoiNN()
    sro_score_total = 0
    count = 0

    for i in original_site_indices:
        site = structure[i]
        neighbors = vnn.get_nn_info(structure, i)
        subspecies = structure[i].specie.symbol
        local_score = 0
        for neighbor in neighbors:
            neighbor_species = neighbor['site'].specie.symbol
            if neighbor_species != subspecies:
                local_score += 1
        if neighbors:
            sro_score_total += local_score / len(neighbors)
            count += 1

    if count == 0:
        return 0.0
    return round(sro_score_total / count, 4)


def substitute_atoms_mc_sro(poscar_filename, host_atom, num_subs, subs, num_trials):
    structure = Poscar.from_file(poscar_filename).structure
    host_indices = [i for i, site in enumerate(structure) if site.specie.symbol == host_atom]

    if len(host_indices) < num_subs:
        raise ValueError("Not enough host atoms to replace.")

    all_trials = []

    for trial in range(num_trials):
        structure_trial = structure.copy()
        selected_indices = random.sample(host_indices, num_subs)

        # Distribute substituting atoms as evenly as possible
        num_each = num_subs // len(subs)
        extras = num_subs % len(subs)
        new_species = []
        for sub in subs:
            new_species += [sub] * num_each
        new_species += random.choices(subs, k=extras)
        random.shuffle(new_species)

        # Apply substitutions
        for idx, new_atom in zip(selected_indices, new_species):
            structure_trial[idx] = new_atom

        # Sort sites by species for POSCAR order
        structure_trial = structure_trial.get_sorted_structure()
        trial_poscar = Poscar(structure_trial)
        out_fname = f"POSCAR_trial_{trial+1}.vasp"
        trial_poscar.write_file(out_fname)

        sro_score = calculate_sro_score(structure_trial, selected_indices, dict(zip(selected_indices, new_species)))
        all_trials.append((out_fname, sro_score))
        print(f"Trial {trial+1}: Saved to {out_fname} | SRO Score = {sro_score}")

    return all_trials


def main():
    print("### Monte Carlo Substitution with SRO Scoring ###")
    poscar_file = input("Enter the name of your POSCAR file (e.g., POSCAR): ").strip()
    host_atom = input("Which atom do you want to substitute (e.g., Co)? ").strip()
    num_subs = int(input("How many atoms do you want to substitute? [1 <= n <= 12] ").strip())
    subs_input = input("Enter the substituting atom(s), separated by spaces (e.g., Mn Ni): ").strip()
    subs = subs_input.split()
    num_trials = int(input("How many Monte Carlo trials to attempt? ").strip())

    results = substitute_atoms_mc_sro(poscar_file, host_atom, num_subs, subs, num_trials)
    print("\nSummary of trials:")
    for fname, score in results:
        print(f"{fname}: SRO Score = {score}")


if __name__ == "__main__":
    main()