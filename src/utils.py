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
    
    # Create a Plotly pie chart with improved aesthetics
    fig = px.pie(
        names=distribution.index,
        values=distribution.values,
        title="Review Sentiment Distribution",
        color_discrete_sequence=['#4CAF50', '#F44336']  # Green for positive, red for negative
    )
    
    # Adjust the layout for a better appearance and title visibility
    fig.update_layout(
        title_font_size=35,   # Title font size
        title_x=0.52,          # Center the title
        title_y=0.95,          # Set title at the top of the plot
        margin=dict(l=600, r=80, t=80, b=80),  # Increase top margin to prevent title cutoff
        height=500,           # Slightly increase height to accommodate the title
        width=1300,            # Maintain width
        showlegend=True       # Show the legend
    )

    # Update the font size and style for labels and percentages
    fig.update_traces(
        textposition='inside',   # Position text inside the pie slices
        textinfo='percent+label', # Show both label and percentage
        textfont_size=16,        # Increase font size
        marker=dict(line=dict(color='#000000', width=2))  # Add a black border around slices
    )
    
    st.plotly_chart(fig)


def plot_wordcloud(dataset):
    # Combine all reviews
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
        title_x=0.55,           # Center the title horizontally
        title_y=0.9,          # Adjust the vertical position of the title
        title_font_size=40,    # Increase the font size for better visibility
        margin=dict(l=600, r=0, t=0, b=0),  # Increase top margin to prevent title overlap
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        width=1200,             # Adjust the width of the figure
        height=500             # Adjust the height of the figure
    )

    # Render the Plotly figure in Streamlit
    st.plotly_chart(fig)