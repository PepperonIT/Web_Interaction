# Demo module for open house
Prepared "main" files for demo purposes. They link to the main file path "./src/..." and runs the development code. The most up to date "main" file can be found under "./src/main.py".   

## General info
    A server running OpenAI's Whisper is required

    In general one can follow along in the terminal to view the steps taken when she goes through a given program.

    In each demo file, under "__main__" you can chose which language you want pepper to boot in, write either "Swedish" or "English"

    *NOTE:* This entire README.md is assuming you are in the demo working directory: "./src/demo/"
    
## cli_demo
Demonstrates the simple cli created with the Click package, which allows you to put flags when starting for ease of use.
The flags are:
    *-w / --wikipedia*: for ask_wikipedia
    *-g / --google*: for ask_google
    *-k / --key*: for string input
with --wikipedia and --google being mutually exclusive and --key being an optional flag.

### examlpe 1.
If we want to run the ask_wikipedia method, with the robot listening to our question we would:
```bash
python cli_demo.py -w
```
which would simply run the ask_wikipedia method

### example 2.
If we want to run the ask_google method, but we do not want to deal with the process of recording and transcribing, we simply:
```bash
python cli_demo.py -g -k "Astronauts"
```
which will then directly call the ask_google_api method which inputs "Astronauts"

## google_demo
A simple call to the ask_google method, which will have Pepper prompt us for a question which she will process and return a picture from the word if one could be found

### example 1.
If we want to ask Pepper to show a picture of a cat from google:
```bash
python google_demo.py
```
    - Pepper will prompt us to ask her something, to which we respond "cat"

## listen_demo
Demonstrates the use of voice navigation with Pepper. This is a really newely introduced function so it's not bug free nor the easiest to explain. Basically you are to first provide a language; Swedish or English. Then you are to provide a method; Wikipedia or Google.   

Follow along in the terminal for the ques for when to talk. You can also listen to her prompts.
```
Robot is listening to you...
```

### example 1.
If we want to run Pepper in Swedish to ask Google a question:
```bash
python listen_demo.py
```
    1. look at the terminal or listen for the promt. Answer "Swedish":
```
Robot is listening to you...
```
(we say:) SWEDISH

    2. look at the terminal or listen for the prompt. for the second que to answer "Google":
```
Robot is listening to you...
```
(we say:) GOOGLE

    3. Now procede to follow Peppers prompt of what you want her to Google.

## listen_method_demo
Demonstrates the use of voice navigation with Pepper. This is a really newely introduced function so it's not bug free nor the easiest to explain. You are to provide a method; Wikipedia or Google.   

Follow along in the terminal for the ques for when to talk. You can also listen to her ques.
```
Robot is listening to you...
```

### example 1.
If we want to run Pepper in Swedish to ask Wikipedia a question:
```bash
python listen_demo.py
```

    1. look at the terminal or listen for the prompt. for the second que to answer "Wikipedia":
```
Robot is listening to you...
```
(we say:) Wikipedia

    2. Now procede to follow Peppers prompt of what you want her to search on Wikipedia.


## wikipedia_demo
A simple call to the ask_wikipedia method, which will have Pepper prompt us for a question which she will process and return the first sentence from a wikipedia page and a related picture.

### example 1.
If we want to ask Pepper about information about Stockholm:
```bash
python wikipedia_demo.py
```
    - Pepper will prompt us to ask her something, to which we respond "Stockholm".
