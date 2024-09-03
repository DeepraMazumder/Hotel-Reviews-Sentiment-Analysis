from collections import Counter
from io import BytesIO

import nltk
import pandas as pd
import plotly.express as px
import streamlit as st
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer



nltk.download('stopwords')
import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st
from PIL import Image
from wordcloud import WordCloud


# Function to load pickle file
def load_object(file_path):
    with open(file_path, 'rb') as f:
        obj = joblib.load(f)
    return obj


# Function to print sentiment distribution
def plot_pie_chart(predictions):
    distribution = predictions.value_counts()
    
    fig = px.pie(
        names=distribution.index,
        values=distribution.values,
        title="Review Sentiment Distribution",
        color_discrete_sequence=['#4CAF50', '#F44336']  # Green for positive, red for negative
    )
    
    # Adjust the layout for a better appearance and title visibility
    fig.update_layout(
        title_font_size=35, 
        title_x=0.52,         
        title_y=0.95,        
        margin=dict(l=600, r=80, t=80, b=80),  
        height=500,           
        width=1300,           
        showlegend=True       
    )

    # Update the font size and style for labels and percentages
    fig.update_traces(
        textposition='inside',   
        textinfo='percent+label', 
        textfont_size=16,     
        marker=dict(line=dict(color='#000000', width=2))  
    )
    
    st.plotly_chart(fig)

def plot_pie_chart1(predictions):
    distribution = predictions.value_counts()
    
    fig = px.pie(
        names=distribution.index,
        values=distribution.values,
        title="Sentiment Pie Chart",
        color_discrete_sequence=['#4CAF50', '#F44336']  # Green for positive, red for negative
    )
    
    # Adjust the layout 
    fig.update_layout(
        title_font_size=35, 
        title_x=0.0,            # Title left-aligned
        title_y=0.95,          # Title position vertically
        margin=dict(l=100, r=100, t=100, b=100),  # Adjust margins as needed
        height=500,           
        width=800,             # Adjust width to center the pie chart
        showlegend=True
    )

    
    fig.update_traces(
        textposition='inside',   
        textinfo='percent+label', 
        textfont_size=16,     
        marker=dict(line=dict(color='#000000', width=2))  
    )
    
    st.plotly_chart(fig)

def plot_wordcloud(dataset):
    reviews = " ".join([review for review in dataset['REVIEWS']])
                        

    wc = WordCloud(background_color='white', max_words=50).generate(reviews)
    

    wc_image = wc.to_image()


    img_buffer = BytesIO()
    wc_image.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    img_pil = Image.open(img_buffer)

    fig = go.Figure()


    fig.add_trace(go.Image(z=img_pil))


    fig.update_layout(
        title_text='Wordcloud for  Reviews',
        title_x=0.55,          
        title_y=0.9,          
        title_font_size=40,    
        margin=dict(l=600, r=0, t=0, b=0), 
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        width=1200,             
        height=500             
    )


    st.plotly_chart(fig)
    



def plot_wordcloud1(dataset,x):
    
    reviews = " ".join(review for review in dataset['Reviews'])
                        
    # Initialize wordcloud object
    wc = WordCloud(background_color='white', max_words=50).generate(reviews)
    
   
    wc_image = wc.to_image()


    img_buffer = BytesIO()
    wc_image.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    img_pil = Image.open(img_buffer)


    fig = go.Figure()


    fig.add_trace(go.Image(z=img_pil))

   
    fig.update_layout(
    title_text=f'Wordcloud for {x} Reviews',
    title_x=0.0,              
    title_y=0.95,             
    title_font_size=40,       
    margin=dict(l=20, r=20, t=40, b=20), 
    xaxis=dict(
        visible=False,       
        showgrid=False,      
        zeroline=False      
    ),
    yaxis=dict(
        visible=False,        
        showgrid=False,       
        zeroline=False        
    ),
    width=800,                
    height=600
)          



    st.plotly_chart(fig)





def plot_frequency_chart(dataset):
    # Get English stopwords
    stop_words = set(stopwords.words('english'))
    stop_words.update(["Read","more","..."])
    
    # Combine all reviews into one large string
    reviews = " ".join(review for review in dataset['REVIEWS'])

    # Split the string into words and remove stopwords
    words = [word for word in reviews.split() if word.lower() not in stop_words]

    # Use Counter to count the frequency of each word
    word_counts = Counter(words)

    # Create a dataframe from the word counts for easy plotting
    word_freq_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])

    # Sort the dataframe by frequency in descending order
    word_freq_df = word_freq_df.sort_values(by='Frequency', ascending=False)

    # Filter the top N most frequent words
    top_n = 20  
    word_freq_df = word_freq_df.head(top_n)

    # Create a bar chart using Plotly
    fig = px.bar(
        word_freq_df, 
        x='Word', 
        y='Frequency', 
        title="Word Frequency Distribution ",
        color='Frequency',  # Optional: color bars by frequency
        color_continuous_scale='Blues',  # Optional: color scale
    )


    fig.update_layout(
        title_font_size=35,
        title_x=0.0,          # Title left-aligned
        title_y=0.95,         # Title position vertically
        margin=dict(l=100, r=100, t=100, b=100),  # Adjust margins as needed
        height=500,
        width=800,
        showlegend=False     
    )

    fig.update_traces(
        textfont_size=16,  
        marker=dict(line=dict(color='#000000', width=1.5))  
    )
    

    st.plotly_chart(fig)

