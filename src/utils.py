import joblib
import plotly.express as px
import streamlit as st

# Function to load pickle file
def load_object(file_path):
    with open(file_path, 'rb') as f:
        obj = joblib.load(f)
    return obj


# Function to print senitment distribution
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
        title_font_size=20,   # Title font size
        title_x=0.5,          # Center the title
        margin=dict(l=80, r=80, t=80, b=80),  # Increase top margin to prevent title cutoff
        height=550,           # Slightly increase height to accommodate the title
        width=550,            # Maintain width
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