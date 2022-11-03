"""
Main module
"""
from robot import Robot

def main():
    """infinite loop for testing"""
    pepper = Robot("130.240.238.32", "9559")
    while True:
        try:
            pepper.ask_wikipedia()
            # pepper.ask_google()
        except Exception as error:# pylint: disable=broad-except
            print(error)# pylint: disable=superfluous-parens
            # pepper.say("I dont know mate")
            pepper.say("Vet inte fett oklart")
main()
