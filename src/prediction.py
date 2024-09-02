import pandas as pd
from src.utils import load_object

'''
class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict_csv(self, dataset):
        pass

    def predict_str(self, review):
        pass
'''


class PredictPipeline:
    def __init__(self) -> None:
        # Load the TF-IDF Vectorizer and Logistic Regression Model
        self.vectorizer = load_object('../artifacts/NPN_TF_IDF_Vectorizer.pkl')
        self.model = load_object('../artifacts/NPN_Logistic_Regression_Model.pkl')

    def predict_csv(self, dataset):
        # Read the CSV file
        data = pd.read_csv(dataset)

        reviews = data['Review']

        # Transform the reviews using the loaded TF-IDF vectorizer
        X_tfv = self.vectorizer.transform(reviews)

        # Predict using the loaded Logistic Regression model
        predictions = self.model.predict(X_tfv)

        # Add the predictions as a new column in the DataFrame
        data['Predicted Sentiment'] = predictions

        return data

    def predict_str(self, review):
        # Transform the single review string using the loaded TF-IDF vectorizer
        X_tfv = self.vectorizer.transform([review])

        # Predict the sentiment using the loaded Logistic Regression model
        prediction = self.model.predict(X_tfv)

        return prediction[0]