import qi
import speech_recognition
import playsound
import time
import paramiko
from cryptography.hazmat.backends import default_backend
from scp import SCPClient
import tools


class Robot:

    def __init__(self, ip_address, port):
        #speech, ip etc
        self.session = qi.Session()
        self.session.connect("tcp://" + ip_address + ":" + str(port))

        self.ip_address = ip_address
        self.port = port

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.connect(hostname=self.ip_address, username="name", password="password", allow_agent=False)
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
        self.led_service = self.session.service("ALLeds")
        self.tablet_service = self.session.service("ALTabletService")

        self.recognizer = speech_recognition.Recognizer()

        print("[INFO]: Robot is initialized at " + ip_address + ":" + port)
        self.tablet_service.preLoadImage("https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")

    def blink_eyes(self, rgb):
        self.led_service.fadeRGB('AllLeds', rgb[0], rgb[1], rgb[2], 1.0)

    def turn_off_leds(self):
        self.blink_eyes([0, 0, 0])

    def download_file(self, file_name):
        self.scp.get(file_name, local_path="/tmp/")
        print("[INFO]: File " + file_name + " downloaded")
        self.scp.close()


    def listen(self):
        self.speech_service.setAudioExpression(False)
        self.speech_service.setVisualExpression(False)
        self.audio_recorder.stopMicrophonesRecording()
        print("[INFO]: Speech recognition is in progress. Say something.")
        while True:
            print(self.memory_service.getData("ALSpeechRecognition/Status"))
            # if self.memory_service.getData("ALSpeechRecognition/Status") == "SpeechDetected":
            self.audio_recorder.startMicrophonesRecording("/home/nao/speech.wav", "wav", 48000, (0, 0, 1, 0))
            print("[INFO]: Robot is listening to you")
            self.blink_eyes([255, 255, 0])
            break

        while True:
            time.sleep(2)
            # if self.memory_service.getData("ALSpeechRecognition/Status") == "EndOfProcess":
            self.audio_recorder.stopMicrophonesRecording()
            print("[INFO]: Robot is not listening to you")
            self.blink_eyes([0, 0, 0])
            break

        self.download_file("speech.wav")
        self.speech_service.setAudioExpression(True)
        self.speech_service.setVisualExpression(True)

        return self.speech_to_text("speech.wav")

    def speech_to_text(self, audio_file):
        audio_file = speech_recognition.AudioFile("/tmp/" + audio_file)
        with audio_file as source:
            audio = self.recognizer.record(source)
            # recognized = self.recognizer.recognize_google(audio, language="en_US")
            recognized = self.recognizer.recognize_google(audio, language="en_US")
            print("[INFO]: s2t:" + recognized)
        return recognized

    def say(self, text):
        #stuff
        self.tts_service.say(text)
        print("[INFO]: Robot says: " + text)

    def set_awareness(self, state):
        if state:
            self.awareness_service.resumeAwareness()
            print("[INFO]: Awareness is turned on")
        else:
            self.awareness_service.pauseAwareness()
            print("[INFO]: Awareness is paused")

    
    def ask_wikipedia(self):
        #stuff
        self.tablet_service.showImage("https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")
        time.sleep(1)
        self.speech_service.setAudioExpression(False)
        self.speech_service.setVisualExpression(False)
        self.set_awareness(False)
        self.say("Give me a question wikipedia")
        # self.say("vad vill du mig")
        question = self.listen()
        self.say("I will tell you")
        # self.say("jag har dig bror")
        answer2 = tools.get_image_wikipedia(question)
        #############TABLET IMAGE###############
        print("[INFO]: answer2 (wikiimage): " + answer2)
        self.tablet_service.showImage(answer2)
        #############SAY ANSWER##################
        answer = tools.get_knowledge_wikipedia(question)
        self.say(answer)
        self.set_awareness(True)
        self.speech_service.setAudioExpression(True)
        self.speech_service.setVisualExpression(True)
        time.sleep(2)
        self.tablet_service.showImage("https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")
        


#    def ask_google(self):

