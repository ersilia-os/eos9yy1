# imports
import os
import pandas as pd
import numpy as np
import csv
import sys
from rdkit import Chem

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, ".."))

from predictors.liver_cytosol.hlc_predictor import LCPredictor 
from predictors.utilities.utilities import addMolsKekuleSmilesToFrame 

input_file = sys.argv[1]
output_file = sys.argv[2]

def my_model(smiles_list):
    mols = [Chem.MolFromSmiles(smi) for smi in smiles_list]
    kek_mols = []
    for mol in mols:
        if mol is not None:
            Chem.Kekulize(mol)
        kek_mols += [mol]
    kek_smiles = [Chem.MolToSmiles(mol,kekuleSmiles=True) for mol in kek_mols]
    predictor = LCPredictor(kekule_smiles = np.asarray(kek_smiles), smiles = np.asarray(smiles_list))
    return predictor.get_predictions()
    

      
# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

outputs = my_model(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["hlcs_proba1"])  # header
    for o in outputs:
        writer.writerow([o])