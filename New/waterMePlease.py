import speech_recognition as sr
from generateVoice import generate_voice
from queryGPT import queryGPT
import random
import os
import pygame
# from localTextToSpeach import text_to_speech_local  
def trigger_function():
    print("Triggered function because the specific word was detected!")

def waterMePlease():
    endWord = "end conversation" 

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    conversation_state = False

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for any input...")
    


    pygame.mixer.init()

    convo_starters_dir = "/Users/will/Documents/MVP Plant Pal/Convo Starters"
    mp3_files = [f for f in os.listdir(convo_starters_dir) if f.endswith('.mp3')]

    if mp3_files:
        random_file = random.choice(mp3_files)
        pygame.mixer.music.load(os.path.join(convo_starters_dir, random_file))
        pygame.mixer.music.play()
    else:
        print("No MP3 files found in the directory.")
    chatContext = []

    run = True
    while run:
        try:
            with microphone as source:
                print("Start recording...")
                
                try:
                    audio_data = recognizer.listen(source, timeout=3, )
                    audioText = recognizer.recognize_google(audio_data)
                    print(f"Input Audio Text: {audioText}")

                    if (endWord.lower() in audioText.lower()):
                        conversation_state = False
                        print("Conversation ended...")
                        chatContext.clear()
                        run = False
                    else:
                        conversation_state = True
                        print("Conversation started...")
                        
                    if conversation_state:
                        response = queryGPT(audioText, chatContext)
                        print(f"GPT Response: {response}")
                        generate_voice(response)
                        chatContext.append({"role": "user", "content": audioText})
                        chatContext.append({"role": "assistant", "content": response})
                        # text_to_speech_local(response)

                except:
                    print("no input")
                
               


        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")


 # Change to the specific word you want to end the conversation

