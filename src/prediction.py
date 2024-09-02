import pandas as pd
from utils import load_object

class PredictPipeline:
    def __init__(self) -> None:
        # Load the TF-IDF Vectorizer and Logistic Regression Model
        self.vectorizer = load_object('artifacts\NPN_TF_IDF_Vectorizer.pkl')
        self.model = load_object('artifacts\NPN_Logistic_Regression_Model.pkl')
        self.encoder = load_object("artifacts\NPN_Label_Encoder.pkl")

    def predict_csv(self, dataset):
        # Read the CSV file
        data = pd.read_csv(dataset)

        reviews = data['Review']

        # Transform the reviews using the loaded TF-IDF vectorizer
        processed_data = self.vectorizer.transform(reviews)

        # Predict using the loaded Logistic Regression model
        predictions = self.model.predict(processed_data)

        # Decode the predictions using
        predictions = self.encoder.inverse_transform(predictions)

        return pd.Series(predictions)

    # def predict_str(self, review):
    #     # Transform the single review string using the loaded TF-IDF vectorizer
    #     X_tfv = self.vectorizer.transform([review])

    #     # Predict the sentiment using the loaded Logistic Regression model
    #     prediction = self.model.predict(X_tfv)

    #     return prediction[0]