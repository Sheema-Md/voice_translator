# Voice Translator

A simple voice translation tool built with Python that recognizes speech, translates it into English, and converts the translated text into speech.

## Features
- **Speech Recognition**: Converts your speech into text using `SpeechRecognition`.
- **Translation**: Translates the recognized speech into English using the `googletrans` library.
- **Text-to-Speech**: Converts the translated text into speech using `pyttsx3`.
- **Exit Command**: You can say "exit" to stop the program.

## Requirements

Before running the project, install the necessary dependencies:

```bash
pip install -r requirements.txt

This will install the following libraries:

- **googletrans**==4.0.0

- **SpeechRecognition**==3.10.4

- **pyttsx3**==2.97

- **pyaudio**==0.2.11

#How to Use

Follow these steps to set up and use the Voice Translator:

1.**Clone the repository** or download the project.

git clone https://github.com/Sheema-Md/voice-translator.git

2.**Navigate to the project folder**.

cd voice-translator

3.**Install the required libraries using requirements.txt**.

pip install -r requirements.txt

4.**Run the Python script**.

python voice_translator.py

5.**Speak into the microphone** when prompted with **"Speak Now!!"**. The program will listen to your speech, translate it into English, and speak the translated text back to you.

6.To exit, simply say **"exit"**.

##Example Usage

1.Run the program.

2.Say something like "Hola, ¿cómo estás?".

3.The program will translate it into "Hello, how are you?" and speak it out loud.

##Libraries Used

- **googletrans**: Used for translating text with Google Translate API.

- **SpeechRecognition**: Used for recognizing speech from the microphone.

- **pyttsx3**: Used for converting text to speech (offline).

- **pyaudio**: Required for audio input/output in the SpeechRecognition library.

##Notes

- This project is a simple example of combining multiple libraries to create a voice translation tool. It works well for basic translations, but keep in mind that the translation may not always be perfect depending on the speech and language.
