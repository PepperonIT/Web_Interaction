# \<Web_Interaction>
Provides added web interactive funcationality, such as:
    *- speech_to_text*
    *- ask_wikipedia*
    *- ask_wikipedia_api*
    *- ask_google*
    *- ask_google_api*
    *- ask_youtube*
    *- ask_youtube_api*
    *- download_file*
    *- listen*
    *- listen_to*
    *- set_language*
    *- set_method*

*speech_to_text:* send the wav file to a backend, that transcribes it into swedish, return a json with text.  
*download_file:* Downloads audio file thats recorded onto Pepper.  
*ask_wikipedia:* Listens for a word/phrase
*ask_wikipedia_api:* Return the first 2 sentences of that wikipedia search.  
*ask_google:* Listens for a word/phrase
*ask_google_api:*  Return 1 image from google.
*ask_youtube:* Listens for a word/phrase
*ask_youtube_api:*  Return 1 image from google.
*listen:* Listens and records a wav file
*listen_to:* Listens and compares against a list of words
*set_language:* Changes pepper and method languages if available.  
*set method:* sets given method, e.g. wikipedia if available.

# tools / installation

The tools used are revolves around speech recognition, transcribing and API functionalities to chosen sites. Currently simplicity has been prioritized over advanced usage while we are still developing base functions. There is currently a server as well used to host OpenAI's whisper, in order to do the transcribing. This is needed due to the need to transcribe languages other than english, and even the small models are quite large so there are some computationals needs required.


## Docker enviroment
> [devcontainer](.devcontainer/README.md)
In order to gain the enviroment, we are using a docker enviroment created by out rock paper and sciccors group, for further intallation instructions:

## server/whisper
> [whisper](https://github.com/D7017E/Whisper_server/blob/main/README.md)
OpenAI's whisper is being used for transcribing. Server info TODO
https://github.com/openai/whisper

## Tools

> [wikipedia](tools.md)
Simple API calls to wikipedia, chosen for its simplicity.
https://pypi.org/project/wikipedia/

> [google_search](tools.md)
Simple API calls to google, chosen for simplicity with image urls.
https://pypi.org/project/google_search

> [youtube_websearch](tools.md)
Simple API calls to youtube, chosen for simplicity to show videos.
https://pypi.org/project/google_search


> [scp](tools.md)
SSH:ing to pepper in order to have permission to download the wav soundfile.
https://pypi.org/project/scp/

> [paramiko](tools.md)
Helper for scp.
https://pypi.org/project/paramiko/

> [requests](tools.md)
Request handler for restful API, sending audiofile for transcribing.
https://pypi.org/project/requests/

> [click](tools.md)
further ease of handling CLI
https://pypi.org/project/click/


# Usage
Currently we have a simple CLI in order to test what we'd like with different functions:
-g, --google: for ask_google
-w, --wikipedia: for ask_wikipedia
-y, --youtube: for ask_youtube
-k, --key: optional argument for testing

### example 1:
```bash
python ./src/python main.py -g
```
which calls the ask_google method which will prompt you to ask google as question.

### example 2:
```bash
python ./src/python main.py -w -k stockholm
```
which will call the ask_wikipedia_api method which will input stockholm, so you can skip the recording process for testing.
### example 3:
```bash
python ./src/python main.py -y -k madonna
```
which will call the ask_youtube_api method which will input madonna, so you can skip the recording process for testing.
# License
MIT License
