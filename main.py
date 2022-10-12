from PepperConnection import PepperConnection
import os


def main():
    conn = PepperConnection("130.240.238.32", 9559, "nao", os.getenv("password")) 
    conn.connect()   
    
    tts = conn.get_speech_service()

    tts.say("Hello there")
    
    #ask_wikipedia(tts)
main()

#def ask_wikipedia(tts):
#    tts.say("Success")

