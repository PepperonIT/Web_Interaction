"""
Controller module
Visual aid methods for Pepper that shows some interactivity
"""

def blink_eyes(self, rgb):
    """
    rgb: the hexadecimal color value
    """
    self.led_service.fadeRGB('AllLeds', rgb[0], rgb[1], rgb[2], 1.0)

def rotate_eyes(self, rgb):
    """
    rgb: the hexadecimal color value
    """
    self.led_service.rotateEyes('AllLeds', rgb[0], rgb[1], rgb[2], 1.0)

def reset_leds(self):
    """Reset the eyes"""
    self.blink_eyes([255, 255, 255])

def reset_tablet(self):
    """Reset the tablet"""
    self.tablet_service.hideImage()
    
def reset_head(self):
    """Reset the head"""

def reset_body(self):
    """Reset the body, primarly arms"""

def say(self, text):
    """
    text: A string Pepper will say
    """
    self.tts_service.say(text)
    print("[INFO]: Robot says: " + text)# pylint: disable=superfluous-parens

def set_awareness(self, state):
    """
    state: True of False, for awareness On or Off
    """
    if state:
        self.awareness_service.resumeAwareness()
        print("[INFO]: Awareness is turned on")# pylint: disable=superfluous-parens
    else:
        self.awareness_service.pauseAwareness()
        print("[INFO]: Awareness is paused")# pylint: disable=superfluous-parens
        