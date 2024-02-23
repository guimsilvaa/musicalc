from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from itertools import product
import os

# Function to read SMILES file
def read_smiles_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [(line.split()[0], line.split()[1]) for line in lines]

# Function to calculate Tanimoto similarity
def calculate_similarity(query, dataset, fingerprint):
    similarities = []
    for q_smiles, q_name in query:
        q_mol = Chem.MolFromSmiles(q_smiles)
        q_fp = fingerprint(q_mol)
        for d_smiles, d_name in dataset:
            d_mol = Chem.MolFromSmiles(d_smiles)
            d_fp = fingerprint(d_mol)
            similarity = DataStructs.TanimotoSimilarity(q_fp, d_fp)
            similarities.append((q_name, d_name, similarity))
    return similarities

# Function to calculate MACCS keys
def maccs(mol):
    return Chem.rdMolDescriptors.GetMACCSKeysFingerprint(mol)

# Function to calculate Morgan fingerprint
def morgan(mol):
    return AllChem.GetMorganFingerprintAsBitVect(mol, 2)  # Use radius 2, you can adjust this as needed

# Function to prompt user for fingerprint choice
def prompt_for_fingerprint():
    print("\nSelect which fingerprint(s) do you want to use for similarity calculation:")
    print("1) Morgan")
    print("2) RDKit")
    print("3) MACCS")
    choice = input("Enter the number(s) separated by comma (e.g. 1,2,3): ")
    fingerprints = []
    for c in choice.split(','):
        if c == '1':
            fingerprints.append(morgan)
        elif c == '2':
            fingerprints.append(Chem.RDKFingerprint)
        elif c == '3':
            fingerprints.append(maccs)
    return fingerprints

# Function to prompt user to choose file
def prompt_for_file(files, file_type):
    print(f"\nSelect the {file_type} file:")
    for i, file in enumerate(files, 1):
        print(f"{i}) {file}")
    choice = int(input("Enter the number corresponding to your choice: "))
    return files[choice - 1]

# Function to get SMILES files in current directory
def get_smiles_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.smi')]
    return files

# Function to write results
def write_results(similarities, fingerprints, query_file, dataset_file):
    query_name = query_file.split('.')[0]
    dataset_name = dataset_file.split('.')[0]
    output_file = f"musicalc_out_{query_name}_{dataset_name}.txt"
    header = ["query", "dataset_compound"]
    for fingerprint in fingerprints:
        if fingerprint.__name__ == 'RDKFingerprint':
            header.append("rdkit_similarity")
        else:
            header.append(f"{fingerprint.__name__}_similarity")
    with open(output_file, "w") as file:
        file.write('\t'.join(header) + '\n')
        results_dict = {}
        for similarity in similarities:
            query_name, dataset_name, *similarity_values = similarity
            pair = (query_name, dataset_name)
            if pair not in results_dict:
                results_dict[pair] = []
            results_dict[pair].extend(similarity_values)
        for pair, values in results_dict.items(): # Write rows from the dictionary
            row = [pair[0], pair[1]] + values
            file.write('\t'.join(map(str, row)) + '\n')

# Read SMILES files
smiles_files = get_smiles_files()
query_file = prompt_for_file(smiles_files, "query")
smiles_files.remove(query_file)
dataset_file = prompt_for_file(smiles_files, "dataset")
query = read_smiles_file(query_file)
dataset = read_smiles_file(dataset_file)

# Prompt user for fingerprint choice
fingerprints = prompt_for_fingerprint()

# Calculate similarity
similarities = []
for fingerprint in fingerprints:
    similarities.extend(calculate_similarity(query, dataset, fingerprint))

# Write results to a table
write_results(similarities, fingerprints, query_file, dataset_file)

print("\n(MUlti) SImilarity CALCulations completed and results written to current directory. \n\nThank you for using my script! \nAuthor: Dr. Guilherme M. Silva - Harvard Medical School - BIDMC - guimsilva@gmail.com")
