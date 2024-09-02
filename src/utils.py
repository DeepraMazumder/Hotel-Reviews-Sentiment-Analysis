import joblib
import sys
import matplotlib.pyplot as plt

# Function to load pickle file
def load_object(file_path):
    with open(file_path, 'rb') as f:
        obj = joblib.load(f)
    return obj


# Function to print senitment distribution
def plot_pie_chart(predictions):
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

