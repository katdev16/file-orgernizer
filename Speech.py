import speech_recognition as sr

class Speech:
   
    

    def __init__(self) :
        self.text = "" 


    def speech_to_text_from_microphone(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            print("Adjusting for ambient noise, please wait...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)
        
        try:
            # Use the Google Web Speech API
            self.text = recognizer.recognize_google(audio)
            print("Text from microphone:", self.text)
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

# Example usage
# speech_to_text_from_microphone()

# speech_instance = Speech()
# speech_instance.speech_to_text_from_microphone()