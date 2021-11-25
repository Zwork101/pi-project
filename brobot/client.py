from brobot.listening import decipher_text

import espeak

espeak.init()
speaker = espeak.Espeak()


class Client:

  def on_answer(self, text, cards, **meta):
    speaker.say(text)

  def on_ask(self, slot, text, choices, **meta):
    speaker.say(text)  # I dont want to mess with this
