import pandas as pd
from src.utils import load_object

class PredictPipeline:
    def __init__(self) -> None:
        # Load the TF-IDF Vectorizer and Logistic Regression Model
        self.vectorizer = load_object('artifacts/NPN_TF_IDF_Vectorizer.pkl')
        self.model = load_object('artifacts/NPN_Logistic_Regression_Model.pkl')
        self.encoder = load_object("artifacts/NPN_Label_Encoder.pkl")


    # .CSV REVIEWS ANALYSER 
    def predict_csv(self, dataset):
        reviews = dataset['REVIEWS']

        # Transform the reviews using the loaded TF-IDF vectorizer
        processed_data = self.vectorizer.transform(reviews)

        # Predict using the loaded Logistic Regression model
        predictions = self.model.predict(processed_data)

        # Decode the predictions using
        predictions = self.encoder.inverse_transform(predictions)

        # Create a DataFrame with the original reviews and the predicted sentiments
        prediction_df = pd.DataFrame({
            'Reviews': dataset['REVIEWS'],
            'Sentiment': predictions
        })

        return prediction_df
    

    # SINGLE REVIEW ANALYSER
    def predict_str(self, review):
        # Transform the single review string using the loaded TF-IDF vectorizer
        processed_data = self.vectorizer.transform([review])
        prediction = self.model.predict(processed_data)
        prediction = self.encoder.inverse_transform(prediction)
        return prediction[0]