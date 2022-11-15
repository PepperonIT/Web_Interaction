"""
Main module
"""

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
    """infinite loop for testing"""
    if wikipedia:
        if key:
            PEPPER.ask_wikipedia_api(key)
        else:
            PEPPER.ask_wikipedia()
    if not wikipedia:
        if key:
            PEPPER.ask_google_api(key)
        else:
            PEPPER.ask_google()

def start():
    word = PEPPER.listen_to(controller.LANGUAGES)
    controller.set_language(PEPPER.speech_service, PEPPER.dialog_service, word)
    method = PEPPER.listen_to(controller.METHODS)
    PEPPER.set_method(method, controller.METHODS)

if __name__ == '__main__':
    PEPPER = Robot(config.IP_ADDRESS, config.PORT)
    # cli()# pylint: disable=no-value-for-parameter
    start()# pylint: disable=no-value-for-parameter
    