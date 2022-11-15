"""
Main module
"""
import sys
sys.path.insert(0,'../')

import config
import controller
from robot import Robot

if __name__ == '__main__':
    PEPPER = Robot(config.IP_ADDRESS, config.PORT)
    while True:
        PEPPER.ask_google()

    