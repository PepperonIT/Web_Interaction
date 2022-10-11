from PepperConnection import PepperConnection 

class Wikipedia:
    def __init__(self, service):
        self.service = service
        
    
    def ask_wikipedia(self):
        self.service.say("What is your question")