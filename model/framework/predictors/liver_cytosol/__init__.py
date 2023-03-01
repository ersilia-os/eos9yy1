import pickle
import sys
import os
import warnings

from tqdm import tqdm
from os import path

warnings.filterwarnings("ignore")

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, ".."))


def download_file(model_number, models_dict):
    hlc_model_path = f'../../checkpoints/model_{model_number}.pkl'
    with open(hlc_model_path, 'rb') as pkl_file:
        hlc_rf_model = pickle.load(pkl_file)
    return hlc_rf_model


def load_models():
    print(f'Loading human liver cytosol stability random forest models', file=sys.stdout)

    hlc_models_dict = {}

    for model_number in tqdm(range(1, 4)):
        hlc_model_path = f'../../checkpoints/model_{model_number}.pkl'
        if path.exists(hlc_model_path) and os.path.getsize(hlc_model_path) > 0:
            with open(hlc_model_path, 'rb') as pkl_file:
                hlc_models_dict[f'model_{model_number}'] = pickle.load(pkl_file)
        else:
            os.makedirs(f'../../checkpoints', exist_ok=True)
            hlc_models_dict[f'model_{model_number}'] = download_file(model_number, hlc_models_dict)

    print(f'Finished loading human liver cytosol stability models', file=sys.stdout)
    return hlc_models_dict

hlc_models_dict = load_models()
