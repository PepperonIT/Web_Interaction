import os

tmp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp_files")
if not os.path.exists(tmp_path):
    os.makedirs(tmp_path)
    print("Created temporary folder Pepper_Controller/pepper/tmp_files/ for retrieved data")

class Listen():
    def __init__(self, service):
        self.service = service


    def listen(self,lang):    
        self.spch_service.setVisualExpression(False)
        self.spch_service.setVisualExpression(False)
        self.audio_recorder.stopMicrophonesRecording()
        
        while True:
            print(self.memory_service.getData("ALSpeechRecognition/Status"))
            if self.memory_service.getData("ALSpeechRecognition/Status") == "SpeechDetected":
                self.audio_recorder.startMicrophonesRecording("speech.wav", "wav", 48000, (0, 0, 1, 0))
                print("[INFO]: Robot is listening to you")
                #self.blink_eyes([255, 255, 0])
                break

        while True:
            if self.memory_service.getData("ALSpeechRecognition/Status") == "EndOfProcess":
                self.audio_recorder.stopMicrophonesRecording()
                print("[INFO]: Robot is not listening to you")
                #self.blink_eyes([0, 0, 0])
                break

        self.download_file("speech.wav")
        self.spch_service.setAudioExpression(True)
        self.spch_service.setVisualExpression(True)

        return self.speech_to_text("speech.wav", lang)

def download_file(self, file_name):
    """
    Download a file from robot to ./tmp folder in root.
    ..warning:: Folder ./tmp has to exist!
    :param file_name: File name with extension (or path)
    :type file_name: string
    """
    self.scp.get(file_name, local_path=tmp_path)
    print("[INFO]: File " + file_name + " downloaded")
    self.scp.close()