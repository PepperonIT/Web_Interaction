from naoqi import ALProxy


def main():
    tts = ALProxy("ALTextToSpeech", "130.240.238.32", 9559)
    tts.say("Hello there")

main()