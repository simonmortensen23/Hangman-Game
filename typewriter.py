import sys
from time import sleep

def typewriter(string):
    """
    Typewriter for welcome sentence at the start of the game
    The python code for the typewriter was taken from https://stackoverflow.com/questions/20302331/typing-effect-in-python
    """
    for i in string:
        sleep(0.02)
        sys.stdout.write(i)
        sys.stdout.flush()
