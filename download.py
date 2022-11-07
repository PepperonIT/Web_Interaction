"""
Download module
Allows Pepper to download the recorded audio file
"""
import requests

def download_file(self, file_name):
    """file_name"""
    self.scp.get(file_name, local_path="/tmp/")
    print("[INFO]: File "+ file_name + " downloaded")# pylint: disable=superfluous-parens
    self.scp.close()

def speech_to_text_swe(self, audio_file):# pylint: disable=no-self-use
    """audio_file"""
    url = 'http://92.32.44.72:5000/recieve'# server request endpoint
    audio_file = {"file": open('/tmp/' + audio_file, 'rb')}
    with open('/tmp/speech.wav', 'rb') as source:
        requests.post(url, files={'fieldname': source})
        request = requests.post(
            url, files=audio_file)# Recieves the json with the transcibed text
        recognized = request.text[11:-2]# budget json handling, the text
        print("[INFO]: s2t:" + recognized)# pylint: disable=superfluous-parens
    return recognized