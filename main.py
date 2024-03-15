# Imported Libraries
import translate # pip install translate
import streamlit as st # pip install streamlit==0.82.0
import gtts # pip install gtts
import pyperclip # pip install pyperclip

# Set the page configuration
st.set_page_config(page_title='Simply! Translate', page_icon='translator-icon.png', 
                   layout='wide', initial_sidebar_state='expanded')

# Language Codes
Languages = {'afrikaans':'af','albanian':'sq','amharic':'am','arabic':'ar','armenian':'hy',
             'azerbaijani':'az','basque':'eu','belarusian':'be','bengali':'bn','bosnian':'bs',
             'bulgarian':'bg','catalan':'ca','cebuano':'ceb','chichewa':'ny',
             'chinese (simplified)':'zh-cn','chinese (traditional)':'zh-tw','corsican':'co',
             'croatian':'hr','czech':'cs','danish':'da','dutch':'nl','english':'en',
             'esperanto':'eo','estonian':'et','filipino':'tl','finnish':'fi','french':'fr',
             'frisian':'fy','galician':'gl','georgian':'ka','german':'de','greek':'el',
             'gujarati':'gu','haitian creole':'ht','hausa':'ha','hawaiian':'haw','hebrew':'iw',
             'hebrew':'he','hindi':'hi','hmong':'hmn','hungarian':'hu','icelandic':'is',
             'igbo':'ig','indonesian':'id','irish':'ga','italian':'it','japanese':'ja',
             'javanese':'jw','kannada':'kn','kazakh':'kk','khmer':'km','korean':'ko',
             'kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latin':'la','latvian':'lv',
             'lithuanian':'lt','luxembourgish':'lb','macedonian':'mk','malagasy':'mg',
             'malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi','marathi':'mr',
             'mongolian':'mn','myanmar (burmese)':'my','nepali':'ne','norwegian':'no',
             'odia':'or','pashto':'ps','persian':'fa','polish':'pl','portuguese':'pt',
             'punjabi':'pa','romanian':'ro','russian':'ru','samoan':'sm','scots gaelic':'gd',
             'serbian':'sr','sesotho':'st','shona':'sn','sindhi':'sd','sinhala':'si',
             'slovak':'sk','slovenian':'sl','somali':'so','spanish':'es','sundanese':'su',
             'swahili':'sw','swedish':'sv','tajik':'tg','tamil':'ta','telugu':'te',
             'thai':'th','turkish':'tr','turkmen':'tk','ukrainian':'uk','urdu':'ur',
             'uyghur':'ug','uzbek':'uz','vietnamese':'vi','welsh':'cy','xhosa':'xh',
             'yiddish':'yi','yoruba':'yo','zulu':'zu'}

# Set the title of the web app
st.title("AI Connects India")
st.title("Language Translator:balloon:")

# create a input box for source language in streamlit
option1 = st.selectbox('Input Language',
                      ('english', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 
                       'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 
                       'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 
                       'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish',
                       'dutch',  'esperanto', 'estonian', 'filipino', 'finnish', 'french', 
                       'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 
                       'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 
                       'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 
                       'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 
                       'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian',
                       'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 
                       'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 
                       'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 
                       'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic',
                       'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian',
                       'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 
                       'telugu', 'thai', 'turkish', 'turkmen', 'ukrainian', 'urdu', 'uyghur', 
                       'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'))

# create a input box for destination language in streamlit
option2 = st.selectbox('Output Language',
                      ('hindi', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch',  'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'turkmen', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'))

# create a translator object
translator = translate.Translator(to_lang=option2, from_lang=option1)

st.write('''
[![Star](https://img.shields.io/github/stars/tusharkhanna575/Language-Translation)](https://gitHub.com/tusharkhanna575/Language-Translation)
[![Streamlit](https://img.shields.io/badge/Made%20with%20-Streamlit-red)](https://streamlit.io/)
''')

# create a text area for user input
text = st.text_area("Enter text:",height=None,max_chars=None,key=None,help="Enter your text here")

value1 = Languages[option1]
value2 = Languages[option2]

# create a button for translation
if st.button('Translate Sentence'):
    # check if the text area is empty
    if text == "":
        st.warning('Please **enter text** for translation')

    # if the text area is not empty
    else:
        # translate the text
        translate = translator.translate(text)
        st.info(str(translate))
        # copy the translated text to clipboard
        #pyperclip.copy(translate)
        st.success("Translation is **successfully** completed! Translated text is copied to clipboard.")
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
