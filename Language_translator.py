# importing libraries
import streamlit as st
from streamlit_option_menu import option_menu
from googletrans import Translator
import easyocr
import cv2
import numpy as np



# page config
st.set_page_config(page_title='Translator', page_icon='🤓', layout='wide')

# page setup

with st.sidebar:
    with st.container():
        choose = option_menu("Translation app",
                             ["Language Translator", "Image Translation"],
                             icons=[],
                             )
        


if choose == "Language Translator":
    st.title("Text Translator")

    # Input text box
    trans = st.text_area('Enter the text to translate', height=100)

    # Language Selection
    target_lang = st.selectbox("Select target language", ["English (en)", "Tamil (ta)", "French (fr)", "Spanish (es)", "German (de)", "Japanese (ja)"])

    # Translator
    translator = Translator()

    if st.button("Translate"):
        if not trans:
            st.warning("Please enter some text to translate.")
        else:
            translation = translator.translate(trans, dest=target_lang.split(" ")[0].lower())
            st.subheader("Translation Result")
            st.write(f"Original Text ({translator.detect(trans).lang}):", trans)
            st.write(f"Translated: ", translation.text)

elif choose == "Image Translation":
    st.subheader("Image Translation")

    image_file = st.file_uploader('Upload the image file', type=['jpg', 'png', 'jpeg'])
    st.write('##')
    target_lang = st.selectbox("Select target language", ["English (en)", "Tamil (ta)", "French (fr)", "Spanish (es)", "German (de)", "Japanese (ja)"])

    if st.button("Translate Text") and image_file is not None:
        detected_text = ""

        # Initialize the EasyOCR reader
        reader = easyocr.Reader(['en']) 

        # Read text from the image
        image = image_file.read()
        results = reader.readtext(image)

        # Extract and display the detected text
        for (box, text, prob) in results:
            detected_text += text + " "

        st.subheader("Detected Text:")
        st.write(detected_text)
        translator = Translator()
        translation = translator.translate(detected_text, dest=target_lang.split(" ")[0].lower())
        st.subheader("Translation Result")
        st.write(f"Original Text ({translator.detect(detected_text).lang}):", detected_text)
        st.write(f"Translated Text: ", translation.text)

    