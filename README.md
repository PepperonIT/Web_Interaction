# \<Web_Interaction>
Provides added web interactive funcationality, such as:
    *- speech_to_text*
    *- ask_wikipedia*
    *- download_file*
    *- google_search*

*speech_to_text:* takes a wav recording as input and outputs a transcribed string, currently only supporting en_US.  
*speech_to_text_swe:* send the wav file to a backend, that transcribes it into swedish, return a json with text.  
*ask_wikipedia:* Listens for a word/phrase, and return the first 2 sentences of that wikipedia search.  
*download_file:* Downloads audio file thats recorded onto Pepper.  
*google_search:* Listens for a word/phrase, and return 1 image from google. custom search engine.

# tools / installation

The tools used are revolves around speech recognition, transcribing and API functionalities to chosen sites. Currently simplicity has been prioritized over advanced usage while we are still developing base functions. There is currently a server as well used to host OpenAI's whisper, in order to do the transcribing. This is needed due to the need to transcribe languages other than english, and even the small models are quite large so there are some computationals needs required.


## Docker enviroment
> [devcontainer](.devcontainer/README.md)
In order to gain the enviroment, we are using a docker enviroment created by out rock paper and sciccors group, for further intallation instructions:

## server/whisper
> [whisper](tools.md)
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


# Usage
Currently the entire functionality is run from a while true loop in main, so in order to run ask_wikipedia you:
```bash
python main.py
```
and then provide a question after pepper has prompted you to by "Give me a question Wikipedia".
## Examples
Currently same as above, under "Usage".

# License
TODO.
