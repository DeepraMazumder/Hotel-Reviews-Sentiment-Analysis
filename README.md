# Hotel Reviews Sentiment Analysis

Welcome to my **Hotel Sentiment Analysis** project! This repository contains all the necessary components to scrape, analyze, predict and summarise sentiments from hotel reviews.

## 🚀 Project Overview

Our project focuses on predicting **positive & negative sentiments** from hotel reviews using a combination of advanced Natural Language Processing (NLP) techniques and classical Machine Learning models. We aim to provide a robust solution that can assist hotels in understanding guest satisfaction through automated sentiment analysis.

## 📂 Project Structure

- **Artifacts**:  
  - `NPN_Logistic_Regression_Model.pkl`: Logistic Regression model for comparison.
  - `NPN_Random_Forest_Model.pkl`: Random Forest model for advanced predictions.
  - `NPN_Naive_Bayes_Model.pkl`: Naive Bayes model used for baseline performance.
  - `NPN_XGBoost_Model.pkl`: XGBoost model for high-performance predictions.
  - `NPN_LightGBM_Model.pkl`: LightGBM model trained for sentiment analysis.
  - `NPN_Label_Encoder.pkl`: Pre-trained label encoder for categorical variables.
  - `NPN_TF_IDF_Vectorizer.pkl`: TF-IDF vectorizer to transform text data.

- **Dataset**:  
  - `Scraped_Dataset.csv`: The dataset scraped from various hotel review sites.
  - `Single_Hotel_Dataset.csv`: Dataset focusing on a single hotel's reviews.

- **notebooks**:  
  - `Hotel_Sentiment_Analysis.ipynb`: The Jupyter notebook detailing the model training and evaluation.

- **src**:  
  - `__init__.py`: Initialization for the source module.
  - `prediction.py`: Contains functions for making sentiment predictions.
  - `summariser.py`: Script for summarizing reviews and key sentiments.
  - `utils.py`: Utility functions used throughout the project.

- **templates**:  
  - `img/`: Images and media files used in the project.

- **Web_Scraping**:  
  - `scraper.py`: The web scraping script to extract reviews from online sources.
  - `test.py`: Testing scripts to validate the scraper's performance.

- `.gitignore`: Files and folders to be ignored by Git.
- `requirements.txt`: Python packages required to run the project.
- `.streamlit/`: Streamlit configuration files for deploying the web app.
- `streamlit_app.py`: The main Streamlit application file that launches the web interface for the project, allowing users to interact with the sentiment analysis model and visualize the results.
- `setup.py`: Setup script for easy installation of the project.

## 🛠️ Getting Started

### Prerequisites

Make sure you have Python installed. Clone this repository and install the required packages:

```bash
git clone https://github.com/your-repo/NPN-Cognizant-Hackathon.git
cd NPN-Cognizant-Hackathon
pip install -r requirements.txt
```

### Running the Project

1. **Scrape Data**: Use the web scraper to collect hotel reviews.
   ```bash
   python Web_Scraping/test.py
   ```

2. **Run Analysis**: Execute the Jupyter notebook to train models and analyze sentiments.
   ```bash
   jupyter notebook notebooks/Hotel_Sentiment_Analysis.ipynb
   ```

3. **Deploy the App**: Deploy the Streamlit web app to showcase your results.
   ```bash
   streamlit run streamlit_app.py
   ```

## 🧠 Model Overview

- **Logistic Regression**: Baseline model for comparison.
- **Random Forest**: Ensemble method to capture complex patterns.
- **Naive Bayes**: Quick and interpretable model.
- **LightGBM & XGBoost**: Gradient boosting models for high accuracy.

## 📈 Results

Our models have been fine-tuned and evaluated to achieve high accuracy in predicting sentiment from hotel reviews. Detailed results can be found in the notebook.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.