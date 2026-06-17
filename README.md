# 🤖 Spark AI Assistant

Spark is a Python-based voice-controlled AI assistant. It helps you do things with your voice. You can tell Spark to open websites for you. Spark can also play music for you. Spark is also good, at getting news for you.. Spark can answer questions that you have in general about things. Spark uses something called Artificial Intelligence to do all these things.

## 🚀 Features

* 🎤 Voice recognition ( wake word: "Spark" )
* 🌐 Open popular websites (Google, YouTube, Facebook, LinkedIn)
* 🎵 Play music from a custom music library
* 📰 Fetch latest news using News API
* 🧠 AI-powered responses using OpenAI API
* 🔊 Text-to-speech responses using gTTS + pygame


## 🛠️ Technologies Used

* Python
* speech_recognition
* pyttsx3
* gTTS
* pygame
* requests
* OpenAI API
* webbrowser

## 📁 Project Structure

Mega Project-Spark/
│
├── main.py              # Main assistant logic
├── musiclibrary.py      # Music dictionary (songs & links)
├── client.py            # Optional testing file
├── README.md            # Project documentation
└── __pycache__/         # Auto-generated (ignore)


## ▶️ How to Run

### 1. Install dependencies

Bash
pip install speechrecognition pyttsx3 gtts pygame requests openai


### 2. Run the program

bash
python main.py

### 3. Activate assistant

Say:
spark 

Then give commands like:

* play shape of you
* open youtube
* what is the time
* news

## 🎵 Music Library Format

Add songs inside `musiclibrary.py` in this format:

python
music = {
    "shape of you": "https://youtube.com/...",
    "song name": "https://youtube.com/..."
}



## ⚠️ Important Notes

* You need to add your **OpenAI API key**.
* You also need to add your **News API key**.
* A working internet connection is needed for AI and news features to work.
* Your microphone needs to be accessible.


## 💡 Future Improvements

* It would be really great to have a graphical user interface, for this thing you know a GUI interface so it is easier to use.
* The wake word detection needs to be improved means the wake word detection so it can hear me better when I talk to it.
* It would be awesome to have Spotify integration to listen to music from Spotify with the Spotify integration.
* I want to be able to tell it to do something and then it remembers so we need a command memory system, a system that can     remember the commands.
* Sometimes If we do not have internet. I think it would be great to have offline AI support you know the offline AI support   so it can still work without the internet.
