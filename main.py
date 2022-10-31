from robot import *

def main():
    pepper = Robot("130.240.238.32", "9559")
    while True:
        try:
            pepper.ask_wikipedia()
            # pepper.ask_google()
        except Exception as error:
            print(error)
            pepper.say("I dont know mate")
            # pepper.say("Vet inte fett oklart")

main()
