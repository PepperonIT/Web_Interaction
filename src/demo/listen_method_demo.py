"""
Main module
"""
import sys
sys.path.insert(0,'../')

import config
import controller
from robot import Robot
import time
    
def start_method(dialog):   
    """
    Voice activated decision of which method to run
    dialog: Pre determed script for Pepper to say in given language
    """ 
    controller.say(PEPPER.tts_service, dialog[6])
    method = PEPPER.listen_to(controller.METHODS)
    # if pepper didn't recognize anything, run again
    if method == "":
        controller.say(PEPPER.tts_service, dialog[1])
        time.sleep(1)
        start_method(dialog)
    # if the recognized method is not available, run again
    elif method not in controller.METHODS:
        controller.say(PEPPER.tts_service, dialog[8])
        time.sleep(1)
        start_method(dialog)
    # if it made it through the checks, run that method
    else:
        PEPPER.set_method(method, controller.METHODS, dialog)


if __name__ == '__main__':
    """
    Sets up for pepper with a starting language,
    which promots you for your prefered language,
    Which prompts you for your wanted method,
    and finally runs the given method with given lang
    """
    PEPPER = Robot(config.IP_ADDRESS, config.PORT)
    language = "Swedish" # START LANGUAGE
    dialog = controller.set_dialog(language)
    controller.set_language(PEPPER.speech_service, PEPPER.dialog_service, language)
    wiki_lang = dialog[4]
    start_method(dialog)
