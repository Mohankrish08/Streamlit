import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# Disable onboarding message
st.set_option('deprecation.showfileUploaderEncoding', False)

st.set_page_config(page_title='My Webpage', page_icon=':tada:', layout='wide')

# Animations

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

Shrimp = Image.open('E:\\Second Brain\\Streamlit\\Images\\Shrimp disease montoring system.png')
Sign_lang = Image.open('E:\\Second Brain\\Streamlit\\Images\\Hand recognition.png')

# Loading assets

lottie_coding = load_lottieurl('https://lottie.host/a2e4e6ab-c839-408b-a17e-01a0973e6dc8/beKMsCTQEy.json')

# Container to organizer the code
with st.container():
    st.subheader('Hi, I am Mohan krishnan')
    st.title('Aspiring Data scientist')
    st.write('I am an enthusiastic learner with a keen interest in machine learning')
    st.write('[This is my Github > ](https://github.com/Mohankrish08)')


with st.container():
    st.write("------")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header('What I do')
        st.write("##")
        st.write(
            """
            As an AI & Data Science Enthusiast and an Undergraduate Student
            at KCT'24, majoring in Artificial Intelligence & Data Science, I am
            actively working on projects based on Machine Learning and Data
            Science. I consider myself a critical thinker, passionately curious,
            and a problem solver. Additionally, I am obsessed with
            photography. Being a fast learner, I always make sure to learn
            from my mistakes. Currently, I am eagerly looking for an
            Internship/Job in my area of expertise to apply my knowledge and
            contribute to consistent growth.

"""
        )
        st.write('[GitHub channel >](https://github.com/Mohankrish08)')
     
    with right_col:
        st_lottie(lottie_coding, height=300, key='coding')

with st.container():
    st.write('-------')
    st.header('My Projects')
    st.write("##")
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(Shrimp)
    with text_col:
        st.subheader('Shrimp disease monitoring system')
        st.write(
            """
            This project is to monitor and classify the Good shrimp and
            Infected shrimps in the pond, and also send an intimation to
            shrimp farm owners as to how many infected shrimps are in the
            pond.

            """
        )
with st.container():
    st.write('---------')
    st.write('##')
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(Sign_lang)
    with text_col:
        st.subheader('Sign language classification using days of a week (RNN VS LSTM)')
        st.write(
            """
            This project aims to classify sign language gestures for the days
            of the week using Recurrent Neural Networks (RNNs), This was
            trained by using Google’s Mediapipe Library to Predict the days of
            a week.
    
            """
        )    
