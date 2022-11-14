"""
Main module
"""

from robot import Robot
import config
import argparse
import click

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
    pepper = Robot(config.IP_ADDRESS, config.PORT)
    if wikipedia:
        if key:
            pepper.ask_wikipedia_api(key)
        else:
            pepper.ask_wikipedia()
    if not wikipedia:
        if key:
            pepper.ask_google_api(key)
        else:
            pepper.ask_google()
     

        
if __name__ == '__main__':
    cli()
