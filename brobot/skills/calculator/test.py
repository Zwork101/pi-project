from sure import expect
from pytlas.testing import create_skill_agent
import os

agent = create_skill_agent(os.path.dirname(__file__))

class TestAddition:

  def setup(self):
    agent.model.reset()

  def test_simple(self):
    agent.parse('whats 3 plus 9')
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal('3.0 plus 9.0 is 12.0')

  def test_words(self):
    agent.parse('add thirty two and fifty four')
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal('32.0 plus 54.0 is 86.0')

  def test_negative(self):
    agent.parse('add negative five plus negative two thousand three hundred and fifty five')
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("-5.0 plus -2355.0 is negative 2360.0")

class TestSubtract:

  def setup(self):
    agent.model.reset()

  def test_simple(self):
    agent.parse("what is 4 minus 1")
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("4.0 minus 1.0 is 3.0")

  def test_words(self):
    agent.parse("what is twenty two minus twelve")
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("22.0 minus 12.0 is 10.0")

  def test_negative(self):
    agent.parse("subtract ninety nine by two hundred and three")
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("99.0 minus 203.0 is negative 104.0")
  
class TestMultiply:

  def setup(self):
    agent.model.reset()

  def test_simple(self):
    agent.parse("what is 90 times 2")
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("90.0 times 2.0 is 180.0")

  def test_words(self):
    agent.parse("multiply fifteen with fifteen")
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("15.0 times 15.0 is 225.0")

  def test_negative(self):
    agent.parse("multiply negative ten by sixty")
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("-10.0 times 60.0 is negative 600.0")

class TestDivide:

  def setup(self):
    agent.model.reset()

  def test_simple(self):
    agent.parse("what is 30 divided by 3")
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("30.0 divided by 3.0 is 10.0")

  def test_words(self):
    agent.parse("calculate four hundred fifty over four hundred fifty")
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("450.0 divided by 450.0 is 1.0")

  def test_negative(self):
    agent.parse("divide negative sixty six by four")
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("-66.0 divided by 4.0 is negative 16.5")

  def test_zero(self):
    agent.parse("divide 2 by 0")
    on_answer = agent.model.on_answer.get_call()
    expect(on_answer.text).to.equal("zero cannot be used as a denominator")
