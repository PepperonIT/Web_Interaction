"""
Controller module
Visual aid methods for Pepper that shows some interactivity
"""

def blink_eyes(service, rgb):
    """
    Stupid name, it just lights the eyes up in a given color
    rgb: the hexadecimal color value
    """
    service.fadeRGB('AllLeds', rgb, 1.0)

def rotate_eyes(service, rgb, sleep):
    """
    Makes the eye rotate with a color for a given time
    rgb: the hexadecimal color value
    sleep: duration of spin (also works as a sleep for Pepper)
    """
    service.rotateEyes(rgb, 1.0, sleep)

def reset_leds(service):
    """
    Reset the eyes
    service: led_service
    """
    blink_eyes(service, 0xFFFFFF)

def reset_tablet(service):
    """Reset the tablet
    service: tablet_service
    """
    service.hideImage()

def reset_all(led_service, tablet_service):
    """Resets the entire pepper thingy
    led_service: led_service
    tablet_service: tablet_service
    """
    reset_tablet(tablet_service)
    reset_leds(led_service)

def say(service, text):
    """
    text: A string Pepper will say
    """
    service.say(text)
    print("[INFO]: Robot says: " + text)# pylint: disable=superfluous-parens

def set_awareness(service, state):
    """
    state: True of False, for awareness On or Off
    """
    if state:
        service.resumeAwareness()
        print("[INFO]: Awareness is turned on")# pylint: disable=superfluous-parens
    else:
        service.pauseAwareness()
        print("[INFO]: Awareness is paused")# pylint: disable=superfluous-parens

def set_language(service, dialog, language):
    """
    Sets Peppers TTS language if a valid one
    dialog: custom scripted list of words for Pepper to TTS
    langauge: the given language
    """
    service.pause(True)
    if language in PEPPER:
        dialog.setLanguage(language)
        print("[SYSTEM]: Pepper language set to: " + language)# pylint: disable=superfluous-parens
        set_dialog(language)
    else:
        print("[SYSTEM]: EXIT can not chose that language")# pylint: disable=superfluous-parens
        exit
    service.pause(False)
    return language

def set_dialog(language):
    """
    Set a given language script for peppers TTS to use
    language: Given language, e.g. "Swedish"
    """
    if language == "Swedish":
        return PEPPER_DIALOG_SWEDISH
    elif language == "English":
        return PEPPER_DIALOG_ENGLISH
    else:
        exit

LANGUAGES = [
    "Swedish",
    "English",
    "Japanese",
    "French",
    "Italian",
    "German",
    "Spanish",
    "Chinese",
    "MandarinTaiwan",
    "Dutch",
    "Arabic",
    "Korean",
    "Polish",
    "Brazilian",
    "Portuguese",
    "Czech",
    "Danish",
    "Finish",
    "Russian",
    "Turkish",
    "Norweigan",
    "Greek"
]

METHODS = [
    "Wikipedia",
    "Google",
    "Youtube"
]

VERIFICATION = [
    "yes",
    "no"
]

PEPPER = [
    "Swedish",
    "English"
]

PEPPER_DIALOG_SWEDISH = [
    "hej, vad undrar du?",              # 0 = question
    "jag fattade inte, vi provar igen!",# 1 = confusion
    "jag hittade svaret!",              # 2 = success
    "jag kunde inte hitta svaret!",      # 3 = failure
    "sv",                           # 4 = language
    "pratar du svenska eller engelska? svara pa engelska", # 5 = lang q
    "Vilken sida ska jag kolla, Google eller Wikipedia?", # 6 = method q
    "Jag kan inte prata det, vi provar igen!",      # 7 = unknown lang
    "Jag kan inte hitta den sidan, vi provar igen!" # 8 = unknown site
]

PEPPER_DIALOG_ENGLISH = [
    "hello, what's your question?",     # 0 = question
    "I didn't understand, let's try again",# 1 = confusion
    "I found the answer!",              # 2 = success
    "Sorry I couldn't find the answer",      # 3 = failure
    "en",                               # 4 = language
    "What language do you want to speak?", # 5 = lang q
    "What site would you like me to search, Google or Wikipedia?", # 6 = method q
    "I don't speek that language, let's try again", # 7 = unknown lang
    "I can't search that site, let's try again"    # 8 = unknown site
]
