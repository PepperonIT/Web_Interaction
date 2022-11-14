"""
Robot module
Holds the methods for listening as well as the functions that call them
"""

import time
import qi
import paramiko
from scp import SCPClient
import tools
import controller
import download
import config

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
        self.audio_recorder.stopMicrophonesRecording()
        print("[INFO]: Speech recognition is in progress. Say something.")# pylint: disable=superfluous-parens
        while True:
            print(self.memory_service.getData("ALSpeechRecognition/Status"))# pylint: disable=superfluous-parens
            # if self.memory_service.getData("ALSpeechRecognition/Status") == "SpeechDetected":
            self.audio_recorder.startMicrophonesRecording(
                "/home/nao/speech.wav", "wav", 48000, (0, 0, 1, 0))
            print("[INFO]: Robot is listening to you")# pylint: disable=superfluous-parens
            controller.blink_eyes(self, [255, 255, 0])
            break

        while True:
            time.sleep(3)
            # if self.memory_service.getData("SpeechDetected") == False:
            self.audio_recorder.stopMicrophonesRecording()
            print("[INFO]: Robot is not listening to you")# pylint: disable=superfluous-parens
            controller.blink_eyes(self, [150, 150, 0])

            break

        download.download_file(self, "speech.wav")
        return download.speech_to_text("speech.wav")

    def ask(self):
        """
        Helper method that sets the appropriate expressensions
            and then calls listen, returning the question(string)
        """
        time.sleep(1)
        self.speech_service.setAudioExpression(False)
        self.speech_service.setVisualExpression(False)
        controller.set_awareness(self, False)
        controller.say(self, "vad undrar du?")
        question = self.listen()
        controller.say(self, "jag tror jag hittade svaret")
        controller.set_awareness(self, True)
        self.speech_service.setAudioExpression(True)
        self.speech_service.setVisualExpression(True)
        controller.blink_eyes(self, [50, 50, 0])
        return question

    def ask_wikipedia(self):
        """
        Calls self.ask to get the question
            Calls get_info_wikipedia with a string as input
                then says the output, shows the output picutre
        """
        self.tablet_service.showImage(
            "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")
        time.sleep(1)
        question = self.ask()
        answer, answer2 = tools.get_info_wikipedia(question)
        self.tablet_service.showImage(answer2)
        controller.say(self, answer)
        time.sleep(2)
        controller.reset_tablet(self)

    def ask_google(self):
        """
        Calls self.ask to get the question
            Calls get_info_google with a string as input
                then shows the output picutre
        """
        self.tablet_service.showImage(
            "https://banffventureforum.com/wp-content/uploads/2018/08/Google-Transparent.png")
        question = self.ask()
        answer = tools.get_info_google(question)
        self.tablet_service.showImage(answer)
        controller.say(self, "jag letade efter " + question)
        time.sleep(8)
        controller.reset_tablet(self)
