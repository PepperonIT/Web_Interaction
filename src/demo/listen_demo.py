"""
Main module
"""
import sys
sys.path.insert(0,'../')

import config
import controller
from robot import Robot

def start():
    word = PEPPER.listen_to(controller.LANGUAGES)
    controller.set_language(PEPPER.speech_service, PEPPER.dialog_service, word)
    dialog = controller.set_dialog(word)
    method = PEPPER.listen_to(controller.METHODS)
    PEPPER.set_method(method, controller.METHODS, dialog)

if __name__ == '__main__':
    PEPPER = Robot(config.IP_ADDRESS, config.PORT)
    start()# pylint: disable=no-value-for-parameter

    