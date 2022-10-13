import qi

class PepperConnection():

    def __init__(self, ip, port, user_name, password):
        self.ip = ip
        self.port = port
        self.user_name = user_name
        self.password = password
        self.session = qi.Session()


    def connect(self):
        self.session.connect("tcp://{0}:{1}".format(self.ip, self.port))
        if self.session.isConnected():
            print("Successfully connected to robot")
        else:
            print("Error connecting to robot")
            raise ConnectionError("Error connecting to robot")

        # ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.load_system_host_keys()
        # ssh.connect(hostname=self.ip, username=self.user_name, password=self.password)

    def get_speech_service(self):
        return self.session.service("ALAnimatedSpeech")
    
    def get_battery_service(self):
        return self.session.service("ALBattery")
    
    def get_tablet_service(self):
        return self.session.service("ALTabletService")
    
    def get_speech_recognition(self):
        return self.session.service("ALSpeechRecognition")
    
    def get_audio_device(self):
        return self.session.service("ALAudioDevice")
    
    def get_memory(self):
        return self.session.service("ALMemory")
    
    

