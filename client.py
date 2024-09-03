import time
import pandas as pd
import streamlit as st

from src.prediction import PredictPipeline
from src.summariser import Summariser
from src.utils import plot_frequency_chart, plot_pie_chart1, plot_wordcloud1


@st.fragment
def visualize_data_1(data,pred):
    with st.container(height=500):
        st.markdown("## Uploaded Reviews")
        st.write(data.head(15))
    with st.container(height=500):
        plot_pie_chart1(pred["Sentiment"])
    with st.container(height=500):
        
        plot_frequency_chart(data)


def visualize_data_2(data,pred):
    
    with st.container(height=500):
        st.markdown("## Reviews with Sentiment")
        st.write(pred.head(15))
            
    with st.container(height=500):
        
        with st.container(height=500):
            
            positive_reviews = pred[pred['Sentiment'] == 'POSITIVE']
            plot_wordcloud1(positive_reviews,"Positive")
            
    with st.container(height=500):
        with st.container(height=500):
            negative_reviews = pred[pred['Sentiment'] == 'NEGATIVE']
            plot_wordcloud1(negative_reviews,"Negative")
            
    return pred


def stream_data(txt:str):
    for word in txt.split(" "):
        yield word + " "
        time.sleep(0.02)




def summarizer_display(df):
    #css
    st.markdown("""
            <style>
                .centered-title {
                    font-size: 25px;
                    text-align: center;
                    margin-top: 20px;
                    margin-bottom: -50px;
                }
            
                </style>
            """, unsafe_allow_html=True)
    

    # Initialize summary result in session state 
    # if 'summary_result' not in st.session_state:
    #     st.session_state['summary_result'] = None


    st.markdown("<h4 class='centered-title'>Select the desired parameters for summary generation or click 'Generate Summary' for a comprehensive overview</h4>", unsafe_allow_html=True)
    selected_aspects = st.multiselect(
        "",
        ["Staff Quality", "Ambience", "Parking", "Transportation", "Internet", "Restaurant"], key="unique_multiselect_key"
    )

    if st.button("Generate Summary", key="unique_summary_button_key"):
        with st.spinner("Generating summary..."):
            summ = Summariser()
            summary_result = summ.summarize_reviews(df, selected_aspects)
            # st.session_state['summary_result'] = summary_result  # Save summary result to session state
            st.write("### Summary")
            st.write_stream(stream_data(summary_result))

    # if st.session_state['summary_result']:
    #     summary_result = st.session_state['summary_result']


        txt_file = summary_result
        
        # Generate a .txt file for download
        st.download_button(
            label="Download as TXT",
            data=txt_file,
            file_name="summary.txt",
            mime="text/plain"
        )





def sentiment_analyzer():
    st.markdown("""
        <style>
        .full-width {
            width: 100%;
            text-align: center;
            font-size: 70px;
            font-family: 'Poppins', sans-serif;
            font-weight: 800;
            color: #212529;
            margin-top: 30px;
            line-height: 1.1;
            background: rgb(116,3,1);
            background: -moz-linear-gradient(90deg, rgba(116,3,1,1) 2%, rgba(191,6,3,1) 37%, rgba(244,140,6,1) 65%, rgba(232,93,4,1) 97%);
            background: -webkit-linear-gradient(90deg, rgba(116,3,1,1) 2%, rgba(191,6,3,1) 37%, rgba(244,140,6,1) 65%, rgba(232,93,4,1) 97%);
            background: linear-gradient(90deg, rgba(116,3,1,1) 2%, rgba(191,6,3,1) 37%, rgba(244,140,6,1) 65%, rgba(232,93,4,1) 97%);
            filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#740301",endColorstr="#e85d04",GradientType=1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .line2 {
            margin-top: -10px;
        }
        </style>

        <div class="full-width">Accelerate your services<br><span class="line2">one step forward</span></div>
        """, unsafe_allow_html=True)
 
    st.markdown("""
    <div style="text-align: center; font-size: 2px; margin-top: 40px; margin-bottom: -50px;">
        <h1>Sentiment Analyzer</h1>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("",type=["csv"],accept_multiple_files=False)
    
    if uploaded_file is not None:
        # Read the CSV file
        dataframe = pd.read_csv(uploaded_file)
        
        # Initialize the progress bar
        progress_text = "Operation in progress. Please wait."
        progress_bar = st.progress(0)
        progress_text_display = st.empty()
        progress_text_display.text(progress_text)
        
        # Simulate a multi-step process with progress updates
        steps = ["Loading model", "Predicting data", "Generating results"]
        num_steps = len(steps)

        # Step 1: Initialize pipeline (simulate loading model)
        time.sleep(1)  
        progress_bar.progress(1 / num_steps)
        progress_text_display.text(f"{steps[0]}...")

        pipeline = PredictPipeline()

        # Step 2: Predict data (simulate prediction)
        time.sleep(1)  # Simulate time taken for prediction
        progress_bar.progress(2 / num_steps)
        progress_text_display.text(f"{steps[1]}...")

        pred = pipeline.predict_csv(dataframe)

        # Step 3: Display results
        time.sleep(1)  # Simulate time taken for result generation
        progress_bar.progress(3 / num_steps)
        progress_text_display.text(f"{steps[2]}...")

        # Update progress bar to 100% completion
        progress_bar.progress(1.0)
        progress_text_display.text("Completed!")
        progress_bar.empty()
        # Display results
        daily, monthly = st.columns(2)
        with daily:
            visualize_data_1(dataframe, pred)
        with monthly:
            visualize_data_2(dataframe, pred)
        with st.container():
            summarizer_display(dataframe)
