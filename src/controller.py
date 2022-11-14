"""
Controller module
Visual aid methods for Pepper that shows some interactivity
"""

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
