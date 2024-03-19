# Imported Libraries
import streamlit as st # pip install streamlit==0.82.0
import gtts # pip install gtts
from deep_translator import GoogleTranslator # pip install deep-translator
import pyperclip # pip install pyperclip

# Set the page configuration
st.set_page_config(page_title='Simply! Translate', page_icon='translator-icon.png', 
                   layout='wide', initial_sidebar_state='auto')

# Language Codes
Languages = {'bengali':'bn','bosnian':'bs', 'english':'en',
             'gujarati':'gu', 'hindi':'hi','kannada':'kn',
             'malayalam':'ml','marathi':'mr', 'odia':'or',
             'punjabi':'pa','sindhi':'sd','sinhala':'si',
             'somali':'so','sundanese':'su','swahili':'sw',
             'tamil':'ta', 'telugu':'te','urdu':'ur',
            }

# Set the title of the web app
st.title("AI Connects India")
st.title("Language Translator:balloon:")

# create a input box for source language in streamlit
option1 = st.selectbox('Input Language',
                      ('english', 'bengali', 'bosnian', 
                       'gujarati', 'hindi', 'kannada', 
                       'malayalam', 'marathi', 'odia', 
                       'punjabi', 'sindhi', 'sinhala',
                       'somali', 'sundanese', 'swahili', 
                       'tamil', 'telugu', 'urdu'))

# create a input box for destination language in streamlit
option2 = st.selectbox('Output Language',
                      ('hindi', 'bengali', 'bosnian', 
                       'gujarati', 'english', 'kannada', 
                       'malayalam', 'marathi', 'odia', 
                       'punjabi', 'sindhi', 'sinhala',
                       'somali', 'sundanese', 'swahili', 
                       'tamil', 'telugu', 'urdu'))


st.write('''
[![Star](https://img.shields.io/github/stars/tusharkhanna575/Language-Translation)](https://gitHub.com/tusharkhanna575/Language-Translation)
[![Streamlit](https://img.shields.io/badge/Made%20with%20-Streamlit-red)](https://streamlit.io/)
''')

# create a text area for user input
text = st.text_area("Enter text:",height=None,max_chars=500,key=None,help="Enter your text here")

value1 = Languages[option1]
value2 = Languages[option2]


# create a translator object
translator=GoogleTranslator(source='auto', target=value2)


# create a button for translation
if st.button('Translate Sentence'):
    # check if the text area is empty
    if text == "":
        st.warning('Please **enter text** for translation')

    # if the text area is not empty
    else:
        # translate the text
        translate = translator.translate(text)
        # print(translate)
        st.info(str(translate))
        # copy the translated text to clipboard
        # pyperclip.copy(translate)
        st.success("Translation is **successfully** completed!")
        # create a button for text to speech
        converted_audio = gtts.gTTS(translate, lang=value2)
        converted_audio.save("translated.mp3")
        audio_file = open('translated.mp3','rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio')
        # create a button for download
        st.write("To **download the audio file**, click the kebab menu on the audio bar.")
        st.balloons()
else:
    pass

# create a footer
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: variable;
left: 0;
bottom: 0;
width: 100%;
background-color: navyblue;
color: darkred;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with 💗 by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/tusharkhanna575/" target="_blank">Tushar Khanna</a></p>
</div>

<!-- center the title -->
<style>
h1 {
  text-align: center;
}
</style>

"""
st.markdown(footer,unsafe_allow_html=True)
