# \<Web_Interaction>
Provides added web interactive funcationality, such as:
    *- speech_to_text*
    *- ask_wikipedia*
    *- ask_wikipedia_api*
    *- ask_google*
    *- ask_google_:api*
    *- download_file*

*speech_to_text:* send the wav file to a backend, that transcribes it into swedish, return a json with text.  
*download_file:* Downloads audio file thats recorded onto Pepper.  
*ask_wikipedia:* Listens for a word/phrase
*ask_wikipedia_api:* Return the first 2 sentences of that wikipedia search.  
*ask_google:* Listens for a word/phrase
*ask_google_api:*  Return 1 image from google. custom search engine..  

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

> [scp](tools.md)
SSH:ing to pepper in order to have permission to download the wav soundfile.
https://pypi.org/project/scp/

> [paramiko](tools.md)
Helper for scp.
https://pypi.org/project/paramiko/

> [requests](tools.md)
Request handler for restful API, sending audiofile for transcribing.
https://pypi.org/project/requests/

> [argparse](tools.md)
Easy command line interface
https://pypi.org/project/argparse/

> [click](tools.md)
further ease of handling CLI
https://pypi.org/project/click/


# Usage
Currently we have a simple CLI in order to test what we'd like with different functions:
-g, --google: for ask_google
-w, --wikipedia: for ask_wikipedia
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
# License
TODO.
