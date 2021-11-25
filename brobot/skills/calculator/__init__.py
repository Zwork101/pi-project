from pytlas import training, intent

import os

def get_values(request):
  v1 = request.intent.slot("number1")
  v2 = request.intent.slot("number2")

  num1 = None
  num2 = None

  if not v1:
    if len(v2) == 2:
      num1 = float(v2.pop(0).value)
      num2 = float(v2[0].value)
    else:
      assert AssertionError, "Number 1 value not found"
  elif not v2:
    if len(v1) == 2:
      num2 = float(v1.pop(1).value)
      num1 = float(v1[0].value)
    else:
      assert AssertionError, "Number 2 value not found"
  elif not v1 and v2:
    assert AssertionError, "No numbers found"
  else:
    num1 = float(v1[0].value)
    num2 = float(v2[0].value)

  return num1, num2

@training("en")
def my_data():
  path = os.path.join(os.path.dirname(__file__), 'training.chatl')
  with open(path) as f:
    return f.read()

@intent("calc_add")
def handle_addition(request):

  num1, num2 = get_values(request)

  result = num1 + num2

  if result < 0:
    resp = f"{num1} plus {num2} is negative {str(result)[1:]}"
  else:
    resp = f"{num1} plus {num2} is {result}"

  request.agent.answer(resp)

  return request.agent.done()

@intent("calc_subtract")
def handle_subtraction(request):
  
  num1, num2 = get_values(request)

  result = num1 - num2
  if result < 0:
    resp = f"{num1} minus {num2} is negative {str(result)[1:]}"
  else:
    resp = f"{num1} minus {num2} is {result}"

  request.agent.answer(resp)

  return request.agent.done()

@intent("calc_multiply")
def handle_multiplication(request):
  
  num1, num2 = get_values(request)

  result = num1 * num2
  if result < 0:
    resp = f"{num1} times {num2} is negative {str(result)[1:]}"
  else:
    resp = f"{num1} times {num2} is {result}"

  request.agent.answer(resp)

  return request.agent.done()

@intent("calc_divide")
def handle_division(request):

  num1, num2 = get_values(request)

  if num2 == 0:
    resp = "zero cannot be used as a denominator"
  else:
    result = num1 / num2
    if result < 0:
      resp = f"{num1} divided by {num2} is negative {str(result)[1:]}"
    else:
      resp = f"{num1} divided by {num2} is {result}"

  request.agent.answer(resp)

  return request.agent.done()


