import streamlit as st
from streamlit_navigation_bar import st_navbar

import pandas as pd

st.set_page_config(
    page_title="innsights.ai",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="collapsed",
)

pages = ["Home", "Predict", "Upload", "About Team", "GitHub"]
urls = {"GitHub": "https://github.com/"} #Our 'Official Repository' will be placed here...
logo_path = ("templates/img/innsights-logo.svg")

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


######################################### START - PREDICT PAGE #########################################
elif page == "Predict":

    #Dot-Matrix BG
    # st.markdown("""
    # <style>
    # .stApp {
    #     background-image: radial-gradient(circle, rgba(0,0,0,0.1) 10%, transparent 10%), radial-gradient(circle, rgba(0,0,0,0.1) 10%, transparent 10%);
    #     background-size: 20px 20px;
    #     background-color: #f0f0f0;
    # }
    # </style>
    # """, unsafe_allow_html=True)

    
    col1 = st.container()
    with col1:
        st.markdown("""
        <style>
        .full-width {
            width: 100%;
            text-align: center;
            font-size: 85px;
            font-family: 'Poppins', sans-serif;
            font-weight: 1000;
            color: #212529;
            margin-top: 40px;
            line-height: 1.2;
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
            '<div class="full-width">A faster way to analyze<br><span class="line2">your hotel reviews</span></div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <style>
        .sub-heading {
            width: 100%;
            text-align: center;
            font-size: 22px;
            font-family: 'Poppins', sans-serif;
            font-weight: 400;
            color: #555555;
            margin-top: 10px;
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
            margin-left: -3px;
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
            <div class="sub-heading">
                <span class="highlight-container">
                    <span class="highlight">innsights.ai</span>
                </span> 
                delivers sentiment-driven insights from hotel reviews,<br> helping the hoteliers to enhance their facilities.
            </div>
            ''',
            unsafe_allow_html=True
        )


    # Multiselector      
    col1, col2, col3 = st.columns([1, 3, 1], vertical_alignment="top")
    # Column 1 (content hidden)
    with col1:
        pass

    # Column 2 (content visible and centered)
    with col2:
        
        st.markdown("""
        <style>
            .centered-title {
                font-size: 30px;
                text-align: center;
                margin-top: 50px;
                margin-bottom: -50px;
            }
                  
            div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl {
                height: 50px;
            }

        </style>
        """, unsafe_allow_html=True)

        st.markdown("<h4 class='centered-title'>Select some features for sentiment evaluation</h4>", unsafe_allow_html=True)
        choices = ["Room Quality", "Hospitality", "Food & Beverages", "Value for money"]
        selected_aspects = st.multiselect("", options=choices, key="multiselect", label_visibility="collapsed")


        # Analyze button
        st.markdown("""
        <style>
        .center-container {
            text-align: center;
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

        analyze_btn = st.button("Analyze")
        
        if analyze_btn:
            if selected_aspects:
                st.success(f"Analyzing the following aspects: {', '.join(selected_aspects)}...")
            else:
                st.warning("Sorry, no aspects selected!")


    # Column 3 (content hidden)
    with col3:
        pass


######################################### END - PREDICT PAGE #########################################



######################################### START - UPLOAD PAGE #########################################
elif page == "Upload":

    col1, col2, col3 = st.columns([1, 3, 1], vertical_alignment="top")

    with col1:
        pass

    with col2:
        # CSS 
        st.markdown("""
        <style>
            .centered-title {
                font-size: 30px;
                text-align: center;
                margin-top: 50px;
                margin-bottom: -50px;
            }
                  
            div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl {
                height: 50px;
            }

        </style>
        """, unsafe_allow_html=True)

        # Analyze button
        st.markdown("""
        <style>
        .center-container {
            text-align: center;
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

        # File Uploader
        st.markdown("<h4 class='centered-title'>Upload your hotel reviews csv file here</h4>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("", type=["csv"])

        
        analyze_btn2 = st.button("Analyze")
        # CSV File
        if analyze_btn2:
            if uploaded_file is not None:
                df = pd.read_csv(uploaded_file)
                st.success("File fetched successfully!")
                st.dataframe(df)
            else:
                st.warning("Please upload a .CSV file!")

    with col3:
        pass

    
    


######################################## END - UPLOAD PAGE #########################################



######################################## START - ABOUT PAGE ########################################
elif page == "About Team":
    st.header("About Team")
######################################## END - ABOUT PAGE #########################################

# with st.sidebar:
#     st.header("Sidebar")