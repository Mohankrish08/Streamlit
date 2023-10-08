import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Mohan's Portfolio", page_icon=':tada:', layout='wide')

# Loading animations

def loader_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Define the URLs for your profiles

github_url = "https://github.com/Mohankrish08"
linkedin_url = "https://www.linkedin.com/in/mohan-krishnan-o-158417201/"
kaggle_url = "https://www.kaggle.com/mohankrishnan08"
medium_url = "https://medium.com/@mohankrishce"
cricket_url = 'https://miro.medium.com/v2/resize:fit:1050/1*lCa5MKZc8oEqjt6wcEFuDQ.jpeg'
rep_url = 'https://purepng.com/public/uploads/large/dumbbells-nzl.png'
pdf_url = 'https://docparser.com/wp-content/uploads/2017/05/pdf-parser.jpg'

# Define the HTML code for the icons as links

github_link = f'<a href="{github_url}" target="_blank"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" style="width: 100px;"></a>'
linkedin_link = f'<a href="{linkedin_url}" target="_blank"><img src="https://static.vecteezy.com/system/resources/previews/018/910/724/original/linkedin-logo-linkedin-symbol-linkedin-icon-free-free-vector.jpg" alt="LinkedIn" style="width: 100px;"></a>'
kaggle_link = f'<a href="{kaggle_url}" target="_blank"><img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png" alt="Kaggle" style="width: 100px;"></a>'
medium_link = f'<a href="{medium_url}" target="_blank"><img src="https://miro.medium.com/v2/resize:fit:2400/1*sHhtYhaCe2Uc3IU0IgKwIQ.png" alt="medium" style="width: 100px;"></a>'

# Loading assets

my_photo = Image.open('E:\\Second Brain\\Streamlit\\Images\\_DSC1742.JPG')
lottie_coding = loader_url('https://lottie.host/a2e4e6ab-c839-408b-a17e-01a0973e6dc8/beKMsCTQEy.json')
analytics = loader_url('https://lottie.host/f3850ea7-6153-47ad-9f30-b5013d59d10e/XYTKvi07ZX.json')
ml = loader_url('https://lottie.host/16a080a6-703e-42fa-9c2c-40f0c36a4050/MK19sf2Xbi.json')
dl = loader_url('https://lottie.host/bda8aeca-7063-4fbe-9516-d2666a26daa3/gDPKMOGy8T.json')
frameworks = loader_url('https://lottie.host/34898b06-05bc-4aaf-8646-1536e82bb023/lGwXvMbSnI.json')
editing = loader_url('https://lottie.host/584f11f4-1df5-4f1f-8c30-10e069d8255d/EMGqkesIgY.json')
photography = loader_url('https://lottie.host/fb05dd0c-0a84-4863-8025-90be36039cc5/MVZ90fW9QJ.json')
Shrimp = Image.open('E:\\Second Brain\\Streamlit\\Images\\Shrimp disease montoring system.png')
Sign_lang = Image.open('E:\\Second Brain\\Streamlit\\Images\\Hand recognition.png')
pdf = Image.open('E:\\Second Brain\\Streamlit\\Images\\Pdf parser.jpg')




# Containers to organize the code

with st.container():
    left_col, right_col = st.columns((1, 0.8))
    with right_col:
        st.title("Hi! I'm Mohan krishnan O")
        st.subheader('Final year at KCT')
        st.write('##')
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
        git_col, lin_col, kaggle_col, medium_col = st.columns((0.5,0.5,0.5,0.5))
        with git_col:
            st.markdown(github_link, unsafe_allow_html=True)
        with lin_col:
            st.markdown(linkedin_link, unsafe_allow_html=True)
        with kaggle_col:
            st.markdown(kaggle_link, unsafe_allow_html=True)
        with medium_col:
            st.markdown(medium_link, unsafe_allow_html=True)
    with left_col:
        st.title('My portfolio')
        st.image(my_photo, width=500)

st.write('------')

# Section 1: Professional Skills
st.header('Professional Skills')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Programming Languages
    
        - **Python**: A versatile and powerful programming language.
        - **SQL**: Essential for database management and querying.
        - **C++**: A popular choice for system and game development.
        """
    )

with left_col:
    st_lottie(lottie_coding, height=250, key='coding')

# Add whitespace between sections
st.write('------')

# Section 2: Data Analysis
st.header('Data Analysis')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Data Analysis 
    
        - **Tableau**
        - **Power BI**
        """
    )

with left_col:
    st_lottie(analytics, height=250, key='analytics')

# Add whitespace between sections
st.write('------')

# Section 3: Machine Learning
st.header('Machine Learning')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Machine Learning 
            
        - **Supervised**
        - **Unsupervised**
        """
    )

with left_col:
    st_lottie(ml, height=250, key='machine learning')

# Add whitespace between sections
st.write('------')

# Section 4: Deep Learning
st.header('Deep Learning')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Deep Learning
    
        - **Computer Vision**
        - **Natural Language Processing**
        """
    )

with left_col:
    st_lottie(dl, height=250, key='Deep learning')

# Add whitespace between sections
st.write('------')

# Section 5: Frameworks
st.header('Frameworks')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Frameworks
    
        - **TensorFlow**
        - **PyTorch**
        """
    )

with left_col:
    st_lottie(frameworks, height=250, key='frameworks')

# Add whitespace between sections
st.write('------')

# Section 6: Editing
st.header('Editing')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Editing
    
        - **Lightroom CC**
        - **Davinci Resolve**
        """
    )

with left_col:
    st_lottie(editing, height=250, key='editing')

# Add whitespace between sections
st.write('------')

# Section 7: Photographer
st.header('Photographer')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Photographer
    
        - **Photography**
        """
    )

with left_col:
    st_lottie(photography, height=250, key='photographer')


with st.container():
    st.write('-----')
    st.title('Projects')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Shrimp disease monitoring system')
        st.write('##')
        st.write(
            """
            This project is to monitor and classify the Good shrimp and
            Infected shrimps in the pond, and also send an intimation to
            shrimp farm owners as to how many infected shrimps are in the
            pond.

            """
        )
    with left_col:
        st.image(Shrimp, width=450)

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Sign Language classification using days of a week (LSTM vs GRU)')
        st.write('##')
        st.write(
            """
            This project aims to classify sign language gestures for the days
            of the week using Recurrent Neural Networks (RNNs), This was
            trained by using Google’s Mediapipe Library to Predict the days of
            a week.
    
            """)
    with left_col:
        #st.subheader('Sign Language classification using days of a week (LSTM vs GRU)')
        st.image(Sign_lang, width=450)

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Cricket inshits hub')
        st.write('##')
        st.write(
            """
            This project is about Tableau-powered cricket data insights
            project, where we transform raw cricket statistics into visually
            compelling and actionable insights for enthusiasts and
            professionals alike.
            """
        )
    with left_col:
        response_cricket = requests.get(cricket_url)
        cricket = Image.open(BytesIO(response_cricket.content))
        st.image(cricket, width=450)


with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Rep counter using Mediapipe')
        st.write('##')
        st.write(
            """
            This project uses the OpenCV library to detect and track the
            movement of an object, such as a weight or a human limb, within
            a video stream.
            """
        )
    with left_col:
        response_rep = requests.get(rep_url)
        rep = Image.open(BytesIO(response_rep.content))
        st.image(rep, width=450)

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Page parser chatbot')
        st.write('##')
        st.write(
            """
            Introducing our innovative project harnessing the power of FAISS
            to convert PDFs into vectors and LLMs like Llama to train models
            for intelligent, book-specific Q&A. Explore a new era of knowledge
            retrieval.
            """
        )
    with left_col:
        st.image(pdf, width=450)






    