import pickle
import sys
import os
import warnings
warnings.filterwarnings("ignore")

from tqdm import tqdm
from os import path

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, ".."))


def load_models():
    base_url = os.path.abspath(os.path.join(root, '../../../checkpoints'))
    print(f'Loading human liver cytosol stability random forest models', file=sys.stdout)

    hlc_models_dict = {}

    for model_number in tqdm(range(1, 4)):
        hlc_model_path = f'{base_url}/model_{model_number}.pkl'
        if path.exists(hlc_model_path) and os.path.getsize(hlc_model_path) > 0:
            with open(hlc_model_path, 'rb') as pkl_file:
                hlc_models_dict[f'model_{model_number}'] = pickle.load(pkl_file)
        else:
            print(f'Model {model_number} not found, skipping...', file=sys.stderr)

    print(f'Finished loading human liver cytosol stability models', file=sys.stdout)
    return hlc_models_dict

hlc_models_dict = load_models()
