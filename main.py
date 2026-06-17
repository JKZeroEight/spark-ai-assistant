import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import musiclibrary
print("LOADED FROM:", musiclibrary.__file__)
print("HAS MUSIC:", hasattr(musiclibrary, "music"))


# SETUP 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "YOUR_NEWS_API_KEY"

#  Replace with real key OR keep AI disabled
client = OpenAI(api_key="YOUR_REAL_OPENAI_KEY")


def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    try:
        tts = gTTS(text)
        tts.save("temp.mp3")

        pygame.mixer.init()
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        os.remove("temp.mp3")

    except Exception as e:
        print("TTS Error:", e)
        speak_old(text)


#  AI 
def aiProcess(command):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a virtual assistant named Spark. Give short answers."
                },
                {"role": "user", "content": command}
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        print("OpenAI Error:", e)
        return "AI is not available right now."



def processCommand(c):
    cmd = c.lower()
    print("Command:", cmd)

    # websites
    if "google" in cmd:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "facebook" in cmd:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "youtube" in cmd:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "linkedin" in cmd:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    
    # music 
    elif cmd.startswith("play"):
        try:
            song = cmd.split(" ", 1)[1].strip().lower()

            print("Searching song:", song)

            if song in musiclibrary.music:
                speak(f"Playing {song}")
                webbrowser.open(musiclibrary.music[song])
            else:
                speak("Song not found")
                print("Available songs:", musiclibrary.music.keys())

        except IndexError:
            speak("Please say a song name")

    # news 
    elif "news" in cmd:
        try:
            r = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
            )

            data = r.json()

            if r.status_code == 200:
                articles = data.get("articles", [])
                for article in articles[:5]:
                    speak(article["title"])
            else:
                speak("News API error")

        except Exception as e:
            print("News error:", e)
            speak("Cannot fetch news")

    #  AI fallback (SAFE) 
    else:
        try:
            output = aiProcess(c)
            speak(output)
        except:
            speak("AI not available")


# MAIN LOOP 

if __name__ == "__main__":
    speak("Initializing Spark")

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)

                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "spark" in word.lower():
                speak("Yes")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)

                    print("Spark Active...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.WaitTimeoutError:
            print("Listening timeout")

        except Exception as e:
            print("Error:", e)
