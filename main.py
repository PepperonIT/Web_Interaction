from PepperConnection import PepperConnection
from listen import Listen
import os
import time
import sys


def main():
    conn = PepperConnection("130.240.238.32", 9559, "nao", os.getenv("password")) 
    conn.connect()   
    
    tts_service = conn.get_speech_service()
    spch_service = conn.get_speech_recognition()
    audio_recorder = conn.get_audio_device()
    memory_service = conn.get_memory()
    
    
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print("Interrupted by user, shutting down")
        Listen.listen()
        sys.exit(0)
    #tts_service.say("Give me a question")
    
    

    
    #tts.say("Hello there")
    

main()
