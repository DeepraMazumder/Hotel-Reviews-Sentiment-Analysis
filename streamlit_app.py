import streamlit as st
from streamlit_navigation_bar import st_navbar
from streamlit_modal import Modal
# import streamlit.components.v1 as components
# from streamlit_extras.switch_page_button import switch_page
# from streamlit_float import *

import pandas as pd
from src.prediction import PredictPipeline
from src.utils import plot_pie_chart, plot_wordcloud


st.set_page_config(
    page_title="innsights.ai",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="collapsed",
)

pages = ["Home", "Analyze", "Predict", "About Us", "GitHub"]
urls = {"GitHub": "https://github.com/DeepraMazumder/NPN-Cognizant-Hackathon"}
logo_path = ("templates\img\innsights-logo.svg")

# Navbar CSS
styles = {
    "div": {"max-width": "50rem"},
    "nav": {
        "background-color": "rgba(233, 236, 239)",
        "justify-content": "left",
        "height": "55px",
    },
    "img": {
        "padding-right": "10px",
    },
    "span": {
        "color": "black",
        "padding": "18px",
        "font-size": "20px",
        "border-radius": "5px",
        "margin": "0 0.315rem",
        "padding": "0.4375rem 0.625rem",
        "font-family": "Poppins, sans-serif",
    },
    "active": {
        "background-color": "rgba(173, 181, 189, 0.35)",
        "color": "black",
        "font-weight": "bold",
        "padding": "14px",
        "height": "100%",  
        "margin": "0 0.315rem",
        "padding": "0.4375rem 0.625rem",
        "font-family": "Poppins, sans-serif"
    },
    "hover": {
        "background-color": "rgba(173, 181, 189, 0.35)",
        "margin": "0 0.215rem",
        "padding": "0.3375rem 0.525rem",
        "font-family": "Poppins, sans-serif"
    }
}

options = {
    "show_menu": True,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

# Poppins Font 
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}
</style>
''', unsafe_allow_html=True)
# End of Poppins Font


############################################## START - HOME PAGE ##############################################
if page == "Home":
    # Background Image
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://i.imgur.com/qpN2PJt.jpg");

            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # End of Background Image

    # Main Heading
    st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Satisfy&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200;300;400;500;600;700&display=swap');

    .display-3 {
        font-size: calc(1.575rem + 3.8vw);
        font-weight: 300;
        line-height: 1.2;
        font-family: 'Oswald', sans-serif;
    }

    .fw-bolder {
        font-weight: bolder !important;
    }

    .mb-2 {
        margin-bottom: .5rem !important;
    }

    .bsb-tpl-highlight {
        background: linear-gradient(90deg, #caf0f8, #90e0ef);
        background-position: 28% 65%;
        background-repeat: no-repeat;
        background-size: 96% 40%;
        opacity: 90%;
    }

    .bsb-tpl-font-hw {
        font-family: 'Satisfy', cursive !important;
    }

    .display-2 {
        font-size: calc(1.575rem + 3.8vw);
        font-weight: 300;
        line-height: 1;
    }

    .text-accent {
        color: #a4161a;
    }

    .fw-normal {
        font-weight: 400 !important;
    }
                
    .custom-position {
        margin-top: 5px;
    }
    </style>
    ''', unsafe_allow_html=True)


    st.markdown('''
    <h1 class="display-3 fw-bolder mb-2 custom-position" style="color: #faa307; line-height: 1.1;">
        Turning <mark class="bsb-tpl-highlight">
        <span class="bsb-tpl-font-hw display-2 text-accent fw-normal">guest reviews</span></mark><br>
        <span style="line-height: 0;">into better business</span>
    </h1>

    ''', unsafe_allow_html=True)
    # End of Main Heading

    # Sub-Heading
    st.markdown('''
        <style>
        .sub-text {
            font-size: 1.35rem !important;
            margin-bottom: 1.5rem !important; 
            margin-top: -30px;
            color: white; 
        }
        </style>
    ''', unsafe_allow_html=True)

    st.markdown('<p class="sub-text">Intuitive insights, effortless impact, unforgettable stays.</p>', unsafe_allow_html=True)
    # End of Sub-Heading


    # Add CSS to the Streamlit app
    st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200;300;400;500;600;700&display=swap');

    .home-btn {
        margin-top: -30px;
        width: 265px;
        background-color: #faa307;
        border-color: #d7ae19; 
        border-radius: 50px;
        padding: 0.5rem 0.5rem;
        font-size: 1.9rem;
        font-weight: 500;
        transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
        text-align: center;
        text-decoration: none; 
        display: inline-block;
        font-family: 'Oswald', sans-serif;  
    }

    .home-btn:hover {
        background-color: #f48c06;
        border-color: #f48c06;
        text-decoration: none;
        transition: transform 0.5s ease, box-shadow 0.5s ease, background-color 0.5s ease;
        transform: scale(1.02);
    }
    </style>
    ''', unsafe_allow_html=True)

    # st.markdown('<a href="#" class="home-btn" style="color: white;" >Predict Insights</a>', unsafe_allow_html=True)

    # Bootstrap CDN
    st.markdown('''
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.10.5/font/bootstrap-icons.min.css');
        </style>
    ''', unsafe_allow_html=True)

    # Predict Button
    st.markdown('''
        <a href="#" class="home-btn" style="color: white; text-decoration: none;">
            Predict Insights
            <i class="bi bi-arrow-right-circle-fill" style="padding-left: 2px;"></i>
        </a>
    ''', unsafe_allow_html=True)
############################################## END - HOME PAGE ##############################################



######################################### START - SERVICES PAGE #########################################

elif page == "Analyze":
    st.markdown("""
        <style>
        .center-container {
            text-align: center;
        }
     
        .centered-title {
            font-size: 30px;
            text-align: center;
            margin-top: 0px;
            margin-bottom: -40px;
        }
                
        div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl {
            height: 40px;
        }

        .stButton {
            margin-top: 0px;
            margin-bottom: 20px;
            display: flex;
            justify-content: center;
        }
        
        .stButton > button {
            margin: 0 auto;
            width: 265px;
            background-color: #faa307;
            border-color: #d7ae19;
            color: #ffffff;
            border-radius: 50px;
            padding: 0.5rem 0.5rem;
            font-size: 2.2rem; 
            font-weight: 700; 
            transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
            text-align: center;
            text-decoration: none; 
            display: inline-block;
            font-family: 'Oswald', sans-serif;  
        }

        .stButton > button:hover {
            background-color: #f48c06;
            border-color: #f48c06;
            color: #ffffff; /* Ensure text color is visible */
            text-decoration: none;
            transition: transform 0.5s ease, box-shadow 0.5s ease, background-color 0.5s ease;
            transform: scale(1.02);
        }

        .stButton p {
            font-size: 1.5rem;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            color: #ffffff;
        }
                
        
        
        </style>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1], vertical_alignment="top")
    with col1:
       pass

    with col2:
        # File Uploader
        st.markdown("<h4 class='centered-title'>Upload your hotel reviews .csv file here</h4>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("", type=["csv"])
        
        analyze_btn2 = st.button("Predict Insights")
        # CSV File
        if analyze_btn2:
            if uploaded_file is not None:
                df = pd.read_csv(uploaded_file)
                pipeline = PredictPipeline()
                st.success("File fetched successfully!")
                pred = pipeline.predict_csv(df)
                st.write(pred)
                plot_pie_chart(pred["Sentiment"])
                plot_wordcloud(df)
            else:
                st.warning("Please upload a .CSV file!")

    with col3:
        st.markdown("""
        <style>
            .popup {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: white;
                padding: 20px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                z-index: 9999;
            }
            .popup-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.5);
                z-index: 9998;
            }

            div.st-emotion-cache-12h5x7g.se1nzilvr5{
                background-color: #ffffff;
            }
                    
            div.st-emotion-cache-l6wp7i.e1f1d6gn2{
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                max-height: 80vh; /* Limit the height to make it scrollable */
                overflow-y: auto; /* Enable vertical scrolling */
                padding: 20px;
                background-color: white;
                z-index: 99999; /* Ensure it is above other elements */
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* Optional: shadow for better visibility */
                border-radius: 8px; /* Optional: Rounded corners */
            }
            div.st-emotion-cache-j5r0tf.e1f1d6gn3{
                position: fixed;
                bottom: 20px;
                right: 20px;
                padding: 10px;
                z-index: 9999;
                border-radius: 8px;
            }
        </style>
        """, unsafe_allow_html=True)


        modal = Modal("Summarize Reviews", key="unique_modal_key")

        # Button to open the modal
        summarize_btn = st.button('Summarize')
        if summarize_btn:
            modal.open()

        # Display the modal content
        if modal.is_open():
            with modal.container():
                # CSS for modal styling with increased width
                st.markdown("""
                    <style>
                        /* Modal Heading Styling */
                        div.st-emotion-cache-pgf13w.e1nzilvr3 h2 {
                            font-size: 30px;
                            margin-top: 0px;
                            margin-bottom: 0px;
                        }

                        /* Modal Container Styling */
                        .modal-container {
                            max-height: 80vh;
                            max-width: 80vw; /* Increase width to 80% of viewport */
                            margin: auto; /* Center the modal */
                            overflow-y: auto; /* Enable scrolling if content exceeds 80% height */
                        }

                        /* Centered Title within Modal */
                        .modal-centered-title {
                            font-size: 20px;
                            text-align: center;
                            margin-top: -30px;
                            margin-bottom: 0px;
                        }

                            
                        div.st-emotion-cache-0.e1f1d6gn0{
                            width: 100vw;
                            max-width: 80vw;
                            margin: auto;
                        }
                        
                        hr {
                            display: none;
                        }
                    </style>
                """, unsafe_allow_html=True)

                # Placeholder function for generating summary
                def generate_summary(text):
                    return "This is a placeholder summary"

                # Modal Content: Select features for sentiment evaluation
                st.markdown("<h5 class='modal-centered-title'>Select some features for sentiment evaluation</h5>", unsafe_allow_html=True)
                
                # Options for sentiment evaluation
                choices = ["Room Quality", "Hospitality", "Food & Beverages", "Value for money"]
                selected_aspects = st.multiselect("", options=choices, key="unique_multiselect_key")

                # Button to generate the summary
                if st.button("Generate Summary", key="unique_summary_button_key"):
                    # Example text input for summarization
                    text_input = "Sample text for summarization."
                    
                    # Generate the summary
                    summary = generate_summary(text_input)

                    # Display the generated summary within an expander
                    with st.expander("Summary", expanded=True):
                        st.markdown(summary)


######################################## END - SERVICES PAGE #########################################



######################################### START - PREDICT PAGE #########################################
elif page == "Predict":
    col1 = st.container()
    with col1:
        st.markdown("""
        <style>
        .full-width {
            width: 100%;
            text-align: center;
            font-size: 75px;
            font-family: 'Poppins', sans-serif;
            font-weight: 1000;
            color: #212529;
            margin-top: 0px;
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
        """, unsafe_allow_html=True)

        st.markdown(
            '<div class="full-width">A faster way to analyze<br><span class="line2">your hotel review</span></div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <style>
        .sub-heading {
            width: 100%;
            text-align: center;
            font-size: 20px;
            font-family: 'Poppins', sans-serif;
            font-weight: 200;
            color: #555555;
            margin-top: -15px;
        }
        </style>
        """, unsafe_allow_html=True)

        # CSS for highlighting text bg
        highlight_css = """
        <style>
        .container {
            line-height: 1.4;
            text-align: center;
            padding: 44px;
            color: #333;
        }

        h1 {
            font-size: 50px;
        }

        p {
            font-size: 18px;
        }

        p small {
            font-size: 80%;
            color: #666;
        }

        .highlight-container, .highlight {
            position: relative;
            font-weight: bold;
        }

        .highlight-container {
            display: inline-block;
        }

        .highlight-container:before {
            content: " ";
            display: block;
            height: 90%;
            width: 105%;
            margin-left: -1px;
            margin-right: -3px;
            position: absolute;
            background: #ffd500;
            transform: rotate(2deg);
            top: -1px;
            left: -1px;
            border-radius: 20% 25% 20% 24%;
            padding: 10px 3px 3px 10px;
        }
        </style>
        """

        # Apply the CSS
        st.markdown(highlight_css, unsafe_allow_html=True)

        # Sub-heading with the highlighted "innsights.ai"
        st.markdown(
            '''
            <div class="sub-heading">Analyze Sentiments in Hotel Reviews for Better Service with 
                <span class="highlight-container">
                    <span class="highlight"> innsights.ai</span>
                </span>
            </div>
            ''',
            unsafe_allow_html=True
        )


    # Multiselector      
    col1, col2, col3 = st.columns([1, 3, 1], vertical_alignment="top")
    with col1:
        pass

    with col2:
        st.markdown("""
            <style>
                .centered-title {
                    font-size: 25px;
                    text-align: center;
                    margin-top: 20px;
                    margin-bottom: -50px;
                }
                    
                .custom-textarea {
                    text-align: center;
                    margin-top: 50px;
                    margin-bottom: -50px;
                    width: 90%;
                    height: 50px;
                    max-height: 100px;
                    border-radius: 25px;
                    border: 1px solid #d7ae19;
                    padding: 10px;
                }

                .stButton {
                    margin-top: 0px;
                    margin-bottom: 20px;
                    display: flex;
                    justify-content: center;
                }
                
                .stButton > button {
                    margin: 0 auto;
                    width: 250px;
                    background-color: #faa307;
                    border-color: #d7ae19;
                    color: #ffffff;
                    border-radius: 50px;
                    padding: 0.5rem 0.5rem;
                    font-size: 2rem; 
                    font-weight: 500; 
                    transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
                    text-align: center;
                    text-decoration: none; 
                    display: inline-block;
                    font-family: 'Oswald', sans-serif;  
                }

                .stButton > button:hover {
                    background-color: #f48c06;
                    border-color: #f48c06;
                    color: #ffffff; /* Ensure text color is visible */
                    text-decoration: none;
                    transition: transform 0.5s ease, box-shadow 0.5s ease, background-color 0.5s ease;
                    transform: scale(1.02);
                }

                .stButton p {
                    font-size: 1.2rem;
                    font-family: 'Poppins', sans-serif;
                    font-weight: 600;
                    color: #ffffff;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("<h4 class='centered-title'>Enter a  review to predict its sentiment</h4>", unsafe_allow_html=True)
        # Create a text area with custom styling
        user_reviews = st.text_area("", placeholder="e.g: Absolutely loved our stay! The staff was incredibly friendly and helpful, and the breakfast was amazing. Will definitely be returning.", height=50, key="custom_textarea")

        # Create a button to fetch the content
        if st.button("Predict"):
            if not user_reviews.strip():
                st.warning("Please enter a review before analyzing.")
            else:
                st.write("Review: ", user_reviews)

    with col3:
        pass

######################################### END - PREDICT PAGE #########################################



######################################## START - ABOUT PAGE ########################################
elif page == "About Us":
    st.header("About Us")
######################################## END - ABOUT PAGE #########################################