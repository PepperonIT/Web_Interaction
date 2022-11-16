"""
Robot module
Holds the methods for listening as well as the functions that call them
"""

import time
import config
import qi
import paramiko
from cryptography.hazmat.backends import default_backend
from scp import SCPClient
import tools
import controller
import download

class Robot:# pylint: disable=too-many-instance-attributes, old-style-class
    """class robot"""
    def __init__(self, ip_address, port):
        """
        ip: Peppers IP address
        port: Peppers port
        """
        self.session = qi.Session()
        self.session.connect("tcp://" + ip_address + ":" + port)

        self.ip_address = ip_address
        self.port = port

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.connect(hostname=self.ip_address, username=config.USERNAME,
                    password=config.PASSWORD, allow_agent=False)
        self.scp = SCPClient(ssh.get_transport())

        self.tts_service = self.session.service("ALAnimatedSpeech")
        self.tablet_service = self.session.service("ALTabletService")
        self.autonomous_life_service = self.session.service("ALAutonomousLife")
        self.awareness_service = self.session.service("ALBasicAwareness")
        self.audio_device = self.session.service("ALAudioDevice")
        self.memory_service = self.session.service("ALMemory")
        self.audio_service = self.session.service("ALAudioPlayer")
        self.speech_service = self.session.service("ALSpeechRecognition")
        self.dialog_service = self.session.service("ALDialog")
        self.audio_recorder = self.session.service("ALAudioRecorder")
        self.tablet_service = self.session.service("ALTabletService")
        self.led_service = self.session.service("ALLeds")
        #self.dialog = controller.PEPPER_DIALOG_SWEDISH # custom made dialog language for pepper
        print("[INFO]: Robot is initialized at " + ip_address + ":" + port)# pylint: disable=superfluous-parens
        self.tablet_service.preLoadImage( # wiki logo
            "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")
        self.tablet_service.preLoadImage( # google logo
            "https://banffventureforum.com/wp-content/uploads/2018/08/Google-Transparent.png")

    def listen(self):
        """
        Starts recording audio for 2 seconds,
            then calls download.download_file
                then returns download.speech_to_text
        """
        sleep_duration = 3 # hardcoded time to liten
        self.audio_recorder.stopMicrophonesRecording()
        print("[INFO]: Speech recognition is in progress. Say something.")# pylint: disable=superfluous-parens
        while True:
            print(self.memory_service.getData("ALSpeechRecognition/Status"))# pylint: disable=superfluous-parens
            # if self.memory_service.getData("ALSpeechRecognition/Status") == "SpeechDetected":
            self.audio_recorder.startMicrophonesRecording(
                "/home/nao/speech.wav", "wav", 48000, (0, 0, 1, 0))
            print("[INFO]: Robot is listening to you")# pylint: disable=superfluous-parens
            controller.blink_eyes(self.led_service, 0x0000FF)
            break

        while True:
            time.sleep(sleep_duration)
            # if self.memory_service.getData("SpeechDetected") == False:
            self.audio_recorder.stopMicrophonesRecording()
            print("[INFO]: Robot is not listening to you")# pylint: disable=superfluous-parens
            controller.blink_eyes(self.led_service, 0x0000FF)
            break

        download.download_file(self, "speech.wav")
        return download.speech_to_text("speech.wav")

    def listen_to(self, vocabulary):
        """
        Listen and match the vocabulary which is passed as parameter.
        vocabulary: list of approved words
        """
        sleep_duration = 2
        self.speech_service.pause(True)
        self.speech_service.setLanguage("English")
        try:
            self.speech_service.unsubscribe("Test_ASR") 
            self.speech_service.setVocabulary(vocabulary, True)
        except RuntimeError as error:
            print(error)
            self.speech_service.pause(True)
            self.speech_service.removeAllContext()
            # self.speech_service.setVocabulary(vocabulary, True)
            self.speech_service.subscribe("Test_ASR")
        try:
            print("[INFO]: Robot is listening to you...")
            self.speech_service.pause(False)
            controller.blink_eyes(self.led_service, 0x0000FF)
            time.sleep(3)
            words = self.memory_service.getData("WordRecognized")
            print("[INFO]: Robot understood: '" + words[0] + "'")
            controller.blink_eyes(self.led_service, 0xFFFFFF)
            words = str(words[0])
            word = words[6:-6]
            print("[RETURN]:" + word)
            return word
        except:
            pass

    def set_method(self, method, vocabulary, dialog):
        if method in controller.METHODS:
            if method == "Wikipedia":
                return self.ask_wikipedia(dialog)
            elif method == "Google":
                return self.ask_google(dialog)
        else:
            print("[INFO]: Couldn't understand, please try again")
            return self.listen_to(vocabulary)


    def ask(self, dialog):
        """
        Helper method that sets the appropriate expressensions
            and then calls listen, returning the question(string)
        """
        question = dialog[0]
        confusion = dialog[1]
        success = dialog[2]
        failure = dialog[3]

        time.sleep(1)
        self.speech_service.setAudioExpression(False)
        self.speech_service.setVisualExpression(False)
        controller.set_awareness(self.awareness_service, False)
        controller.say(self.tts_service, question)
        question = self.listen()
        controller.say(self.tts_service, success)
        controller.set_awareness(self.awareness_service, True)
        self.speech_service.setAudioExpression(True)
        self.speech_service.setVisualExpression(True)
        controller.blink_eyes(self.led_service, 0xFFFFFF)
        return question

    def ask_wikipedia(self, dialog):
        """
        Calls self.ask to get the question
            Calls get_info_wikipedia with a string as input
                then says the output, shows the output picutre
        """
        wiki_lang = dialog[4]
        self.tablet_service.showImage(
            "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")
        time.sleep(1)
        question = self.ask(dialog)
        self.ask_wikipedia_api(question, wiki_lang)

    def ask_wikipedia_api(self, question, wiki_lang):
        """
        question: the string input to wiki api
        """
        answer, answer2 = tools.get_info_wikipedia(question, wiki_lang)
        self.tablet_service.showImage(answer2)
        controller.say(self.tts_service, answer)
        time.sleep(2)
        controller.reset_all(self.led_service, self.tablet_service)

    def ask_google(self, dialog):
        """
        Calls self.ask to get the question
            Calls get_info_google with a string as input
                then shows the output picutre
        """
        self.tablet_service.showImage(
            "https://banffventureforum.com/wp-content/uploads/2018/08/Google-Transparent.png")
        question = self.ask(dialog)
        self.ask_google_api(question)

    def ask_google_api(self, question):
        """
        question: string input to google api
        """
        answer = tools.get_info_google(question)
        self.tablet_service.showImage(answer)
        time.sleep(5)
        controller.reset_all(self.led_service, self.tablet_service)
