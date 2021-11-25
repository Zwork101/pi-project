from subprocess import Popen, PIPE, STDOUT, DEVNULL
# from signal import SIGINT
import os
import time

import speech_recognition as sr

sopare_path = os.path.join(os.path.dirname(__file__), "../dev/sopare/")
run_command = ["python", "sopare.py", "-l"]

def await_name(trigger = "bro"):
    p = Popen(run_command, stdout=PIPE, stderr=DEVNULL, cwd=sopare_path)
    while True:
        print("Waiting for name")
        line = p.stdout.readline()
        print(line)
        if line.decode() == "[u'" + trigger + "']\n":
            print("Name trigger identified")
            break
        # p.send_signal(SIGINT)
    p.kill()
    print(decipher_text())

def decipher_text():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening for commands...")
        time.sleep(.33)
        audio = r.listen(source)

    text = r.recognize_google(audio)
    return text

if __name__ == "__main__":
    while True:
        await_name()
