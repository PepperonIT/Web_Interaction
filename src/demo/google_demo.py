"""
Main module
"""
import sys
sys.path.insert(0,'../')

import config
import controller
from robot import Robot

if __name__ == '__main__':
    """
    Sets up for pepper with a starting language,
    Calls ask_google with given language 
    """
    language = "Swedish" # change language
    PEPPER = Robot(config.IP_ADDRESS, config.PORT)
    controller.set_language(PEPPER.speech_service, PEPPER.dialog_service, language)
    dialog = controller.set_dialog(language)
    PEPPER.ask_google(dialog)

    