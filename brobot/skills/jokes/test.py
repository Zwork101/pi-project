import os
import csv

from pytlas.testing import create_skill_agent
from sure import expect

agent = create_skill_agent(os.path.dirname(__file__))

joke_file = os.path.join(os.path.dirname(__file__), 'jokes.csv')
with open(joke_file) as f:
  reader = csv.DictReader(f)
  jokes = tuple(line["Joke"] for line in reader)


class TestJoke:

  def setup(self):
    agent.model.reset()

  def test_joke(self):
    agent.parse("im sad tell me a joke")
    on_answer = agent.model.on_answer.get_call()
    jokes.should.contain(on_answer.text)
    
