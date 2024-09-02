import joblib
from src.logger import logging
from src.exception import CustomException
import sys
import matplotlib.pyplot as plt

# Function to load pickle file
def load_object(file_path):
    try:
        logging.info(f"Loading object {file_path}")
        obj = joblib.load(file_path)
        return obj
    except Exception as e:
        logging.error(f"Error in utils.py: {str(e)}")
        CustomException(e, sys)

# Function to print senitment distribution
def plot_pie_chart(predictions):
    try:
        logging.info("Plotting pie chart for sentiment distribution")
        distribution = predictions.value_counts()
        colors = ['#4CAF50', '#F44336']  # Green and red color palette
        explode = (0.05, 0)
        plt.figure(figsize=(7, 7))
        plt.pie(distribution,
                labels=distribution.index,
                autopct='%1.1f%%',
                startangle=140,
                colors=colors,
                explode=explode,
                shadow=True,
                wedgeprops={'edgecolor': 'black'})
        
        plt.title("Review Sentiment Distribution", fontsize=16, fontweight='bold', color='#333')
        plt.tight_layout()
        plt.show()
        logging.info("Pie chart plotted successfully")

    except Exception as e:
        logging.error(f"Error in utils.py: {str(e)}")
        CustomException(e, sys)


