import tools

class Wikipedia():

    def ask_wikipedia(self):
            """
            Ask for question and then robot will say first two sentences from Wikipedia
            ..warning:: Autonomous life has to be turned on to process audio
            """
            self.speech_service.setAudioExpression(False)
            self.speech_service.setVisualExpression(False)
            self.set_awareness(False)
            self.say("Give me a question")
            question = self.listen()
            self.say("I will tell you")
            answer = tools.get_knowledge(question)
            self.say(answer)
            self.set_awareness(True)
            self.speech_service.setAudioExpression(True)
            self.speech_service.setVisualExpression(True)