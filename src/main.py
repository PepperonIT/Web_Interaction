"""
Main module
"""

import config
import controller
import click
from robot import Robot
import time

@click.command()
@click.option(
    '--method',
    '-m',
    help='Whether you want to ask wikipedia, google or youtube.'
)
@click.option(
    '--key',
    '-k',
    help='If you do not want to talk to pepper, but write the input'
)
def cli(method, key):
    """infinite loop for testing"""
    if method == "wikipedia":
        if key:
            PEPPER.ask_wikipedia_api(key, WIKI_LANG)
        else:
            PEPPER.ask_wikipedia(DIALOG)
    elif method == "google":
        if key:
            PEPPER.ask_google_api(key)
        else:
            PEPPER.ask_google(DIALOG)
    elif method == "youtube":
        if key:
            PEPPER.ask_youtube_api(key)
        else:
            PEPPER.ask_youtube(DIALOG)

def start_language(dialog):
    """
    Voice activated language selection
    dialog: Pre determed script for Pepper to say in given language
    """
    controller.say(PEPPER.tts_service, dialog[5])
    language = PEPPER.listen_to(controller.LANGUAGES)
    # if pepper didn't recognize anything, run again
    if language == "":
        controller.say(PEPPER.tts_service, dialog[1])
        time.sleep(1)
        return start_language(dialog)
    # if the recognized language isn't compatible, run again
    elif language not in controller.PEPPER:
        controller.say(PEPPER.tts_service, dialog[7])
        time.sleep(1)
        return start_language(dialog)
    # if it made it through the checks, switch language
    else:
        controller.set_language(PEPPER.speech_service, PEPPER.dialog_service, language)
        controller.set_dialog(language)
        return language

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
    LANGUAGE = "Swedish"# pylint: disable=redefined-outer-name
    DIALOG = controller.set_dialog(LANGUAGE)# pylint: disable=redefined-outer-name
    controller.set_language(PEPPER.speech_service, PEPPER.dialog_service, LANGUAGE)
    WIKI_LANG = DIALOG[4]
    cli()
    LANGUAGE = start_language(DIALOG)
    DIALOG = controller.set_dialog(LANGUAGE)
    start_method(DIALOG)
    