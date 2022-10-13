from PepperConnection import PepperConnection
import os


def main():
    conn = PepperConnection("130.240.238.32", 9559, "nao", os.getenv("password")) 
    conn.connect()   
    
    tts_service = conn.get_speech_service()
    
    spch_service = conn.get_speech_recognition
    
    spch_service.setVisualExpression(False)
    spch_service.setVisualExpression(False)
    tts_service.say("Give me a question")
    
    

    
    #tts.say("Hello there")
    
main()
