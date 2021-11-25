from pytlas import Agent
from pytlas.understanding.snips import SnipsInterpreter
import os

from brobot.client import Client
from brobot.listening import await_name

import brobot.skills.calculator
import brobot.skills.jokes
import brobot.skills.cancel


if __name__ == "__main__":
  interpreter = SnipsInterpreter('en', cache_directory=os.path.join(os.path.dirname(__file__), 'cache'))

  interpreter.fit_from_skill_data()

  agent = Agent(interpreter, model=Client())

  print("Starting bot")
  while True:
    cmd = await_name()
    print("Got text:", cmd)
    agent.parse(cmd)