import speech_recognition as sr
from gtts import gTTS
import os
import time

class Pottyboy():
    def __init__(self):
        self.wake_word = "hey"
        self.recognizer = sr.Recognizer()

    def wakeup_listening(self):
        with sr.Microphone() as source:
            print("Listening for the wake word...")
            audio = self.recognizer.listen(source)

        try:
            # Use Google Web Speech API with Thai language
            text = self.recognizer.recognize_google(audio)
            print("You said: {}".format(text))

            # Check if the wake word is detected
            if self.wake_word.lower() in text.lower():
                print("Wake word detected! Now you can give a command.")
                return 1
            else:
                return ""  # Return an empty string if the wake word is not detected
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return ""  # Return an empty string in case of an unknown value error
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""  # Return an empty string in case of a request error
        

    def command_listening(self):
        with sr.Microphone() as source:
            print("Listening for the command...")
            audio = self.recognizer.listen(source)

        try:
            # Use Google Web Speech API with Thai language
            text = self.recognizer.recognize_google(audio)
            print("You said: {}".format(text))
            return text.lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return ""  # Return an empty string in case of an unknown value error
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""  # Return an empty string in case of a request error

    def respond_to_wakeup(self):
        while True:
            if self.wakeup_listening() == 1:
                break
        return 1
    
    def text_to_speech(self, text, language='en'):
        # Create a gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the audio file
        audio_path = 'output.mp3'
        tts.save(audio_path)

        # Play the audio file
        os.system(f'open {audio_path}')  # On macOS

    def water_plant(self):
        self.text_to_speech("Watering the plant.", language='en')

    def register_plant(self):
        self.text_to_speech("Plant registration completed.", language='en')


pottyboy = Pottyboy()
count =0
while True:
    if pottyboy.respond_to_wakeup() == 1:
        while True:
            count+=1
            command = pottyboy.command_listening()
            if "hey" in command.lower():
                pottyboy.water_plant()
                print("water plant successful")
                break
            elif "register plant" in command.lower():
                pottyboy.register_plant()
                print("register plant successful")
                break
            
            print(count)
            if count >= 2:
                break