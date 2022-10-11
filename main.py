from PepperConnection import PepperConnection
#from interactions.wikipedia import Wikipedia
import os


def main():
    # session = qi.Session()
    conn = PepperConnection("130.240.238.32", 9559, "nao", os.getenv("password")) 
    conn.connect()   
    
    tts = conn.get_speech_service()

    tts.say("Hello there")
    
    #Wikipedia.ask_wikipedia()
    

main()