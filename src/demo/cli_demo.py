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
    '--wikipedia/--google',
    '-w/-g',
    help='Whether you want to ask wikipedia or google.'
)
@click.option(
    '--key',
    '-k',
    help='If you do not want to talk to pepper, but write the input'
)
def cli(wikipedia, key):
    """
    infinite loop for testing
    key: flag for terminal input strings
    """
    if wikipedia:
        if key:
            PEPPER.ask_wikipedia_api(key, wiki_lang)
        else:
            PEPPER.ask_wikipedia(dialog)
    if not wikipedia:
        if key:
            PEPPER.ask_google_api(key)
        else:
            PEPPER.ask_google(dialog)

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
    