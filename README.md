# musicalc
MUlti SImilarity CALCulation

# description: #
Just a simple tool to calculate tanimoto similarity values using multiple types of fingerprints. 
<br /> Fingerprints implemented in current version: morgan, rdkit, and maccs. 
<br /> Outputs a table (.txt) including a first column with molecules/names from query file, a second column with molecules/names from dataset file, and column(s) with similarity values. 
<br /> Need to run the script in a folder with two .smi files: one for the query and one for the dataset. 
<br /> Useful to make a fast pair-match similarity comparison, or to further use the outputted table for chemical diversity analysis.
<br /> * it's advisable to run the script in a conda environment with the libraries (such as rdkit) properly installed

# place in folder: #
* musicalc.py 
* query.smi
* dataset.smi
