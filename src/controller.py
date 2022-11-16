"""
Controller module
Visual aid methods for Pepper that shows some interactivity
"""
import wikipedia

def blink_eyes(service, rgb):
    """
    rgb: the hexadecimal color value
    """
    service.fadeRGB('AllLeds', rgb, 1.0)

def rotate_eyes(service, rgb, sleep):
    """
    rgb: the hexadecimal color value
    """
    service.rotateEyes(rgb, 1.0, sleep)

def reset_leds(service):
    """Reset the eyes"""
    blink_eyes(service, 0xFFFFFF)

def reset_tablet(service):
    """Reset the tablet"""
    service.hideImage()

def reset_all(led_service, tablet_service):
    """Resets the entire pepper thingy"""
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
    langauge: the given language
    """
    service.pause(True)
    if language in PEPPER:
        service.setLanguage(language)
        dialog.setLanguage(language)
        #wikipedia.set_lang(language)
        print("[SYSTEM]: Pepper language set to: " + language)
        set_dialog(language)
    else:
        print("[SYSTEM]: EXIT can not chose that language")
        exit
    service.pause(False)
    return

def set_dialog(language):
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
    "Google"
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
    "sv"                           # 4 = language
]

PEPPER_DIALOG_ENGLISH = [
    "hello, what's your question?",     # 0 = question
    "I didn't understand, let's try again",# 1 = confusion
    "I found the answer!",              # 2 = success
    "Sorry I couldn't find the answer",      # 3 = failure
    "en"                               # 4 = language
]