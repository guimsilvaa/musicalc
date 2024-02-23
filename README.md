# musicalc
MUlti SImilarity CALCulation

# description: #
Just a simple tool to calculate tanimoto similarity values using multiple types of fingerprints. Fingerprints implemented in current version: morgan, rdkit, and maccs. 
Outputs a table (.txt) including a first column with molecules/names from query file, a second column with molecules/names from dataset file, and column(s) with similarity values. 
Need to run the script in a folder with two .smi files: one for the query and one for the dataset. 
Useful to make a fast pair-match similarity comparison, or to further use the outputted table for chemical diversity analysis.

# place in folder: #
* musicalc.py 
* query.smi
* dataset.smi
