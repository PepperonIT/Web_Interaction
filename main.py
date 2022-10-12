from PepperConnection import PepperConnection
import os
>>>>>>> dafe96a... added interactions folder


def main():
    conn = PepperConnection("ip", 9559, "name", os.getenv("password")) 
    conn.connect()   
    
    tts_service = conn.get_speech_service()

    
    #tts.say("Hello there")
    
main()
