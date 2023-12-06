# HandSpeak 🤚🏽🗣️

A Django-based web Application which takes in live audio recording or text as input, converts it into text and displays the relevant Indian Sign Language animation.

- Front-end built using HTML/CSS,JavaScript.
- Speech recognition using JavaScript Web speech API.
- Natural Language Processing using Natural Language Toolkit(NLTK).
- 3D animations of a character created


## Prerequisites

- Python >= 3.8
- A browser that supports Web Speech API
- Download all required packages for python script A2SL/views.py

## Installation Guide:

These instructions will get you download the project and running on your local machine for development and testing purposes:

### Instructions for local environment

1. Open the repository folder and then open the terminal.
2. To install all the required packages `pip install -r requirements.txt`
3. Run the python file using the command "python manage.py runserver 3000" (3000 being the optional port number).
3. It shows localhost address (looks like this "server at http://127.0.0.1:3000/") run on browser.
4. Sign up and start signing
5. Click on mic button to record speech or enter your sentence
6. Speech will be processed and respective animated signed outputs are shown.

### For sign language to text conversion:
- Please check the folder SignLangToText and follow the instructions its README.md file.