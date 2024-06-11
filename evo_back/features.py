import subprocess
from playsound import playsound as ps
import eel
from evo_back.command import *
from evo_back.config import ASSISTANT_NAME
import os
import pywhatkit as kit
import re
import sqlite3
import webbrowser
from evo_back.helper import extract_yt_term, remove_words
import speech_recognition as sr
import pyautogui
import time
from hugchat import hugchat, exceptions
from urllib.parse import quote
from evo_back.helper import extract_yt_term, remove_words, extr_yt_term
from pipes import quote
import logging

con = sqlite3.connect("evo.db")
cursor = con.cursor()

# playing evosense sound
@eel.expose
def playEvoSound():
    music_dir = "evo_front\\components\\audio\\start_sound.mp3"
    ps(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    app_name = query.strip()
    if app_name != "":        
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()
            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])
            elif len(results) == 0:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening " + query)
                    try:
                        os.system('start' + query)
                    except:
                        speak("not found")
        except :
            speak("some thing went wrong")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on Youtube")
    kit.playonyt(search_term)

def PlayYT(query):
    src_term = extr_yt_term(query)
    speak("Playing "+ src_term + " from Youtube")
    kit.playonyt(src_term)

def hotword():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # List of hotwords to detect
    hotwords = {"sense", "evo", "essence"}

    print("Listening for hotword...")

    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            speech_as_text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {speech_as_text}")

            for hotword in hotwords:
                if hotword in speech_as_text:
                    print("Hotword detected")

                    # Press shortcut key Win + J
                    pyautogui.keyDown("ctrl")
                    pyautogui.press("v")
                    time.sleep(2)
                    pyautogui.keyUp("ctrl")
                    break

        except sr.UnknownValueError:
            # Could not understand the audio
            print("Could not understand audio")
        except sr.RequestError as e:
            # Could not request results from Google Speech Recognition service
            print(f"Could not request results; {e}")

def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
def whatsApp(mobile_no, message, flag, name):
    
    if flag == 'message':
        target_tab = 12
        evo_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        evo_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        evo_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(evo_message)

#chat bot
def chatBot(query):
    user_input = query.lower()
    cookie_path = os.path.join("evo_back", "cookies.json")
    chatbot = hugchat.ChatBot(cookie_path=cookie_path)

    try:
        id = chatbot.new_conversation()
        chatbot.change_conversation(id)
        response = chatbot.chat(user_input)
        print(response)
        speak(response)
        return response
    except exceptions.ChatError as e:
        logging.error(f"ChatError occurred: {e}")
        speak("There was an error processing your request.")
        return "Sorry, I couldn't process that request."
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        speak("An unexpected error occurred.")
        return "Sorry, an unexpected error occurred."