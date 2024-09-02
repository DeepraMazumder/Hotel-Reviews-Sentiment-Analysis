import joblib

def load_object(file_path):
    with open(file_path, 'rb') as f:
        obj = joblib.load(f)
    return obj

