"""
Robot module
Holds the methods for listening as well as the functions that call them
"""
import time
import qi
import speech_recognition
import paramiko
from scp import SCPClient
import tools
import controller
import download


class Robot:# pylint: disable=too-many-instance-attributes, old-style-class
    """class robot"""
    def __init__(self, ip_address, port=9559):
        """ip, port"""
        self.session = qi.Session()
        self.session.connect("tcp://" + ip_address + ":" + str(port))

        self.ip_address = ip_address
        self.port = port

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.connect(hostname=self.ip_address, username="nao",
                    password="FBLovesLMS2019", allow_agent=False)
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

        self.recognizer = speech_recognition.Recognizer() #ENGLISH QUICK TRANSCRIBING

        print("[INFO]: Robot is initialized at " + ip_address + ":" + port)# pylint: disable=superfluous-parens
        self.tablet_service.preLoadImage(
            "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")


    def listen(self):
        """listen"""
        self.speech_service.setAudioExpression(False)
        self.speech_service.setVisualExpression(False)
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
            time.sleep(2)
            # if self.memory_service.getData("SpeechDetected") == False:
            self.audio_recorder.stopMicrophonesRecording()
            print("[INFO]: Robot is not listening to you")# pylint: disable=superfluous-parens
            controller.blink_eyes(self, [0, 0, 0])
            break

        download.download_file(self, "speech.wav")
        self.speech_service.setAudioExpression(True)
        self.speech_service.setVisualExpression(True)

        return download.speech_to_text_swe("speech.wav")

    def speech_to_text(self, audio_file):
        """audio_file"""
        audio_file = speech_recognition.AudioFile("/tmp/" + audio_file)
        with audio_file as source:
            audio = self.recognizer.record(source)
            recognized = self.recognizer.recognize_google(audio, language="en_US")
            print("[INFO]: s2t:" + recognized)# pylint: disable=superfluous-parens
        return recognized

    def ask_wikipedia(self):
        """ask_wikipedia"""
        self.tablet_service.showImage(
            "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")
        time.sleep(1)
        self.speech_service.setAudioExpression(False)
        self.speech_service.setVisualExpression(False)
        controller.set_awareness(self, False)
        # self.say("Give me a question wikipedia")
        controller.say(self, "vad vill du mig")
        question = self.listen()
        # controller.say(self, "I will tell you")
        controller.say(self, "jag har dig bror")
        answer2 = tools.get_image_wikipedia(question)
        self.tablet_service.showImage(answer2)
        answer = tools.get_knowledge_wikipedia(question)
        controller.say(self, answer)
        controller.set_awareness(self, True)
        self.speech_service.setAudioExpression(True)
        self.speech_service.setVisualExpression(True)
        time.sleep(2)
        self.tablet_service.showImage(
            "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")
