"""
Main module
"""
import sys
sys.path.insert(0,'../')

import config
import controller
import click
from robot import Robot

@click.command()
@click.option(
    '--method',
    '-m',
    help='Whether you want to ask wikipedia or google or youtube.'
)
@click.option(
    '--key',
    '-k',
    help='If you do not want to talk to pepper, but write the input'
)
def cli(method, key):
    """
    infinite loop for testing
    key: flag for terminal input strings
    """
    if method=="wikipedia":
        if key:
            PEPPER.ask_wikipedia_api(key, wiki_lang)
        else:
            PEPPER.ask_wikipedia(dialog)
    elif method=="google":
        if key:
            PEPPER.ask_google_api(key)
        else:
            PEPPER.ask_google(dialog)
    elif method=="youtube":
        if key:
            PEPPER.ask_youtube_api(key)
        else:
            PEPPER.ask_youtube(dialog)

if __name__ == '__main__':
    """
    Sets up for pepper with a starting language,
    And then allows you to use flags in the terminal.
    Check README.md for specifics
    """
    language = "Swedish" # change language
    PEPPER = Robot(config.IP_ADDRESS, config.PORT)
    controller.set_language(PEPPER.speech_service, PEPPER.dialog_service, language)
    dialog = controller.set_dialog(language)
    wiki_lang = dialog[4]
    cli()# pylint: disable=no-value-for-parameter
    