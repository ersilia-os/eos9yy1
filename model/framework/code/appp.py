#original functional code 

# import pickle
# import requests
# import sys
# import os
# import warnings
# warnings.filterwarnings("ignore")

# from tqdm import tqdm
# from io import BytesIO
# from os import path

# root = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(root, ".."))


# def download_file(base_url, model_number, models_dict):
#     hlc_rf_pkl_url = f'{base_url}/model_{model_number}.pkl'
#     hlc_model_path = f'../../checkpoints/model_{model_number}.pkl'
#     hlc_rf_pkl_file_request = requests.get(hlc_rf_pkl_url)
#     with tqdm.wrapattr(
#         open(os.devnull, "wb"),
#         "write",
#         miniters=1,
#         desc=f'model_{model_number}',
#         total=int(hlc_rf_pkl_file_request.headers.get('content-length', 0))
#     ) as fout:
#         for chunk in hlc_rf_pkl_file_request.iter_content(chunk_size=4096):
#             fout.write(chunk)
#     with open(hlc_model_path, 'wb') as hlc_rf_pkl_file_writer:
#         hlc_rf_pkl_file_writer.write(hlc_rf_pkl_file_request.content)

#     hlc_rf_model = pickle.load(BytesIO(hlc_rf_pkl_file_request.content))
#     return hlc_rf_model

# def load_models():
#     # base_url = 'https://opendata.ncats.nih.gov/public/adme/models/current/static/liver_cytosol/'
#     base_url = 'file://' + os.path.abspath(os.path.join(root, '../../checkpoints'))
    
#     print(f'Loading human liver cytosol stability random forest models', file=sys.stdout)

#     hlc_models_dict = {}

#     for model_number in tqdm(range(1, 4)):
#         hlc_model_path = f'../../checkpoints/model_{model_number}.pkl'
#         if path.exists(hlc_model_path) and os.path.getsize(hlc_model_path) > 0:
#             with open(hlc_model_path, 'rb') as pkl_file:
#                 hlc_models_dict[f'model_{model_number}'] = pickle.load(pkl_file)
#         else:
#             os.makedirs(f'../../checkpoints', exist_ok=True)
#             hlc_models_dict[f'model_{model_number}'] = download_file(base_url, model_number, hlc_models_dict)

#     print(f'Finished loading human liver cytosol stability models', file=sys.stdout)
#     return hlc_models_dict

# hlc_models_dict = load_models()



