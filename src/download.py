"""
Download module
Allows Pepper to download the recorded audio file
"""

import requests
import config

def download_file(self, file_name):
    """
    Downloads an audiofile onto Pepper so we can use it
    file_name: Input audio file to download and store
    """
    self.scp.get(file_name, local_path="/tmp/")
    print("[INFO]: File "+ file_name + " downloaded")# pylint: disable=superfluous-parens
    self.scp.close()

def speech_to_text(audio_file):# pylint: disable=no-self-use
    """
    Sends the audio file to the server for transcribing,
        recieves a json of the transcribed text
            returns the text in a string format
    audio_file: Input audio file to send to the server
    """
    url = ('http://' + config.SERVER_IP_ADDRESS +
           ':' + config.SERVER_PORT + '/recieve')# server request endpoint
    audio_file = {"file": open('/tmp/' + audio_file, 'rb')}
    with open('/tmp/speech.wav', 'rb') as source:
        requests.post(url, files={'fieldname': source})
        request = requests.post(
            url, files=audio_file)# Recieves the json with the transcibed text
        recognized = request.text[11:-2]# budget json handling, the text
        print("####### \n: s2t:" + recognized + "\n#######")# pylint: disable=superfluous-parens
    return recognized
