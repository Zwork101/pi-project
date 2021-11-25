from pytlas import training, intent

import os

@training("en")
def my_data():
  path = os.path.join(os.path.dirname(__file__), 'training.chatl')
  with open(path) as f:
    return f.read()

