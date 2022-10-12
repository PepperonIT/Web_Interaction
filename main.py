from PepperConnection import PepperConnection
import os


def main():
    conn = PepperConnection("130.240.238.32", 9559, "nao", os.getenv("password")) 
    conn.connect()   
    
    tts_service = conn.get_speech_service()

    
    #tts.say("Hello there")
    
main()
