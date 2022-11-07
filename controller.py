"""
Controller module
Visual aid methods for Pepper that shows some interactivity
"""

def blink_eyes(self, rgb):
    """rbg"""
    self.led_service.fadeRGB('AllLeds', rgb[0], rgb[1], rgb[2], 1.0)

def turn_off_leds(self):
    """."""
    self.blink_eyes([0, 0, 0])

def say(self, text):
    """text"""
    self.tts_service.say(text)
    print("[INFO]: Robot says: " + text)# pylint: disable=superfluous-parens

def set_awareness(self, state):
    """state"""
    if state:
        self.awareness_service.resumeAwareness()
        print("[INFO]: Awareness is turned on")# pylint: disable=superfluous-parens
    else:
        self.awareness_service.pauseAwareness()
        print("[INFO]: Awareness is paused")# pylint: disable=superfluous-parens