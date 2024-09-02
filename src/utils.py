import joblib

def load_object(file_path):
    obj = joblib.load(file_path)
    return obj

