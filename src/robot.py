"""
Robot module
Holds the methods for listening as well as the functions that call them
"""

import time
import qi
import paramiko
from cryptography.hazmat.backends import default_backend
from scp import SCPClient
import config
import tools
import controller
import download

class Robot:# pylint: disable=too-many-instance-attributes, old-style-class
    """class robot"""
    def __init__(self, ip_address, port):
        """
        Initializes qi session, ssh and the pepper services.
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
            """ Sets up the recording process """
            print(self.memory_service.getData("ALSpeechRecognition/Status"))# pylint: disable=superfluous-parens
            # if self.memory_service.getData("ALSpeechRecognition/Status") == "SpeechDetected":
            self.audio_recorder.startMicrophonesRecording(
                "/home/nao/speech.wav", "wav", 48000, (0, 0, 1, 0))
            print("[INFO]: Robot is listening to you")# pylint: disable=superfluous-parens
            controller.blink_eyes(self.led_service, 0x0000FF)
            break

        while True:
            """ Listens to you for the sleep_duration """
            time.sleep(sleep_duration)
            # if self.memory_service.getData("SpeechDetected") == False:
            self.audio_recorder.stopMicrophonesRecording()
            print("[INFO]: Robot is not listening to you")# pylint: disable=superfluous-parens
            controller.blink_eyes(self.led_service, 0x0000FF)
            break
        """ Need to download the file onto Pepper in order to access it"""
        download.download_file(self, "speech.wav")
        return download.speech_to_text("speech.wav")

    def listen_to(self, vocabulary):
        """
        Listen and match the vocabulary which is passed as parameter.
        vocabulary: list of approved words
        """
        sleep_duration = 3
        self.speech_service.pause(True)
        self.speech_service.setLanguage("English")
        try:
            self.speech_service.setVocabulary(vocabulary, True)
        except RuntimeError as error:
            print(error)# pylint: disable=superfluous-parens
            self.speech_service.pause(True)
            self.speech_service.removeAllContext()
            if self.speech_service.setVocabulary == False:
                self.speech_service.setVocabulary(vocabulary, True)
            self.speech_service.subscribe("Test_ASR")
        try:
            print("[INFO]: Robot is listening to you...")# pylint: disable=superfluous-parens
            self.speech_service.pause(False)
            controller.blink_eyes(self.led_service, 0x0000FF)
            time.sleep(sleep_duration)
            words = self.memory_service.getData("WordRecognized")
            controller.blink_eyes(self.led_service, 0xFFFFFF)
            words = str(words[0])
            word = words[6:-6]
            print("[RETURN]:" + word)# pylint: disable=superfluous-parens
            return word
        except:
            print("ERROR")# pylint: disable=superfluous-parens
            return ""

    def set_method(self, method, vocabulary, dialog):
        """
        Sets which method you would like to call
        method: string with method name
        vocabulary: list of appropriate words
        dialog: script in appropriate language for pepper to speak
        """
        if method in controller.METHODS:
            if method == "Wikipedia":
                return self.ask_wikipedia(dialog)
            elif method == "Google":
                return self.ask_google(dialog)


    def ask(self, dialog):
        """
        Helper method that sets the appropriate expressensions
            and then calls listen, returning the question(string)
        dialog: Custom scripted list of phrases for Pepper to TTS
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
        dialog: Custom scripted phrases for Pepper to use with TTS
        """
        wiki_lang = dialog[4]
        self.tablet_service.showImage(
            "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png")
        time.sleep(1)
        question = self.ask(dialog)
        self.ask_wikipedia_api(question, wiki_lang)

    def ask_wikipedia_api(self, question, wiki_lang):
        """
        End half of ask_wikipedia, it calls the helper function get_info_wikipedia
        question: the string input to wiki api
        wiki_lang: the language for wikipedia to search in, e.g. "sv"
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
        dialog: Custom scripted phrases for Pepper to use with TTS
        """
        self.tablet_service.showImage(
            "https://banffventureforum.com/wp-content/uploads/2018/08/Google-Transparent.png")
        question = self.ask(dialog)
        self.ask_google_api(question)

    def ask_google_api(self, question):
        """
        End half of ask_google, it calls the helper function get_info_google
        question: string input to google api
        """
        answer = tools.get_info_google(question)
        self.tablet_service.showImage(answer)
        time.sleep(10)
        controller.reset_all(self.led_service, self.tablet_service)

    def ask_youtube(self, dialog):
        """
        Calls self.ask to get the question
            Calls get_info_youtube with a string as input
                then shows the first youtube video on its display
        dialog: Custom scripted phrases for Pepper to use with TTS
        """
        self.tablet_service.showImage(
            "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.logo.wine%2Flogo%2FYouTube&psig=AOvVaw1xqrR-ztksqHUkdg9A7uo1&ust=1669209441700000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCNin2_DvwfsCFQAAAAAdAAAAABAT"
        )
        question = self.ask(dialog)
        self.ask_youtube_api(question)

    def ask_youtube_api(self, question):
        """
        End half of ask_youtube, it calls the helper function get_info_youtube
        question: string input to google api
        """
        answer, dur = tools.get_info_youtube(question)
        video = "https://www.youtube.com/embed/"+answer
        self.tablet_service.loadUrl(video)
        print("[INFO]: Youtube full link: " + video)# pylint: disable=superfluous-parens
        self.tablet_service.showWebview()        
        time.sleep(dur + 10) # video time + x for start delay
        controller.reset_all(self.led_service, self.tablet_service)
