from pytlas import training, intent

import csv
import os
import random

joke_file = os.path.join(os.path.dirname(__file__), 'jokes.csv')
with open(joke_file) as f:
  reader = csv.DictReader(f)
  jokes = tuple(line["Joke"] for line in reader)

@training("en")
def my_data():
  path = os.path.join(os.path.dirname(__file__), 'training.chatl')
  with open(path) as f:
    return f.read()

@intent("tell_joke")
def tell_joke(request):
  joke = random.choice(jokes)
  request.agent.answer(joke)
  return request.agent.done()
