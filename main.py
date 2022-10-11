from PepperConnection import PepperConnection
#from interactions.wikipedia import Wikipedia
import os
>>>>>>> dafe96a... added interactions folder


def main():
    # session = qi.Session()
    conn = PepperConnection("ip", 9559, "name", os.getenv("password")) 
    conn.connect()   
    
    tts = conn.get_speech_service()

    tts.say("Hello there")
    
    #Wikipedia.ask_wikipedia()
    

main()
