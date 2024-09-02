import joblib
import plotly.express as px
import streamlit as st
from wordcloud import WordCloud
from io import BytesIO
import plotly.graph_objs as go
from PIL import Image

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


def plot_wordcloud(dataset):
    reviews = " ".join([review for review in dataset['REVIEWS']])
                        
    # Initialize wordcloud object
    wc = WordCloud(background_color='white', max_words=50).generate(reviews)
    
    # Convert the wordcloud to an image
    wc_image = wc.to_image()

    # Convert the image to a format that Plotly can display
    img_buffer = BytesIO()
    wc_image.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    img_pil = Image.open(img_buffer)

    # Display the image using Plotly
    fig = go.Figure()

    # Add the wordcloud image to the figure
    fig.add_trace(go.Image(z=img_pil))

    # Update layout for better appearance and title visibility
    fig.update_layout(
        title_text='Wordcloud for All Reviews',
        title_x=0.55,          
        title_y=0.9,          
        title_font_size=40,    
        margin=dict(l=600, r=0, t=0, b=0), 
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        width=1200,             
        height=500             
    )

    # Render the Plotly figure in Streamlit
    st.plotly_chart(fig)