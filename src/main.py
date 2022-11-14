"""
Main module
"""

from robot import Robot
import config

def main():
    """infinite loop for testing"""
    pepper = Robot(config.IP_ADDRESS, config.PORT)
    while True:
        try:
            pepper.ask_google()
        except Exception as error:# pylint: disable=broad-except
            print(error)# pylint: disable=superfluous-parens
main()
