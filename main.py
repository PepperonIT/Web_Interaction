<<<<<<< HEAD
from PepperConnection import PepperConnection
from listen import Listen
import os
import time
import sys


def main():
    conn = PepperConnection("ip", "port", "name", os.getenv("password")) 
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
    

=======
"""
Main module
"""
from robot import Robot

def main():
    """infinite loop for testing"""
    pepper = Robot("130.240.238.32", "9559")
    while True:
        try:
            pepper.ask_wikipedia()
            # pepper.ask_google()
        except Exception as error:# pylint: disable=broad-except
            print(error)# pylint: disable=superfluous-parens
            # pepper.say("I dont know mate")
            pepper.say("Vet inte fett oklart")
>>>>>>> 224322b... Swedish working, pylint implemented
main()
