# ai-nlp-avatar
Interactive AI Avatar Using Basic Natural Language Processing (NLP) Techniques through Speech Recognition and Text Processing

==============================================

Interactive AI Avatar Using Basic Natural Language Processing (NLP)

This project features an interactive AI avatar that leverages basic Natural Language Processing (NLP) techniques to interact with users through speech recognition and text processing. The avatar is built using Python with Pygame for graphical display, pyttsx3 for speech synthesis, and speech_recognition for speech-to-text conversion.


Features

Speech Recognition: Captures user speech using the speech_recognition library.

Speech Synthesis: Converts text responses into speech using pyttsx3.

Interactive Avatar: Displays a graphical avatar with changing mouth states to simulate speech.

Basic NLP: Processes recognized speech to handle predefined queries and provide relevant responses.

Custom Responses: Provides responses based on user queries related to Sevendyne IT consultancy.

Installation

Follow these steps to set up the project on your local machine:


Clone the Repository:


git clone https://github.com/aminakm123/ai-nlp-avatar.git

cd interactive-ai-avatar

Set Up a Virtual Environment (Optional but recommended):



python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:

Ensure you have pip installed. Then, install the required libraries:



pip install pygame pyttsx3 SpeechRecognition

Download Required Assets:

Make sure to place the following images in the root directory of the project:

avatar_closed.png

avatar_half_open.png

avatar_open.png

These images represent different states of the avatar’s mouth.


Run the Project:

Execute the script to start the interactive AI avatar:



python avatar.py

Usage

Voice Interaction: The avatar will prompt you to ask questions about Sevendyne IT consultancy. Speak into your microphone to interact.

Responses: The avatar will provide responses based on your queries and simulate speech with mouth animations.

Troubleshooting

Speech Recognition Issues: Ensure your microphone is properly connected and configured. Check for any errors in the console output.

Missing Images: Make sure that the required image files are present in the project directory.

Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and contributions are welcome!