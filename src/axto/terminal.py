import sys
from turtle import color
def clear():
    sys.stdout.write("\033[2J")

def move(x, y):
    sys.stdout.write(f"\033[{y};{x}H")

def write(text, color=""):
    sys.stdout.write(f"{color}{text}\033[0m")
    sys.stdout.flush()