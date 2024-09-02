import pandas as pd
from src.utils import load_object

# class PredictPipeline:
#     def __init__(self) -> None:
#         pass

#     def predict_csv(self, dataset):
#         # Load the trained model
#         model = load_object('../artifacts/NPN_Logistic_Regression_Model.pkl')
#         # Load preprocessor
#         preprocessor = load_object('../artifacts/NPN_TF_IDF_Vectorizer.pkl')

#     def predict_str(self, review):
#         pass
# Load the trained model
model = load_object("NPN-Cognizant-Hackathon/artifacts/NPN_Logistic_Regression_Model.pkl")
# Load preprocessor
# preprocessor = load_object('../artifacts/NPN_TF_IDF_Vectorizer.pkl')
    