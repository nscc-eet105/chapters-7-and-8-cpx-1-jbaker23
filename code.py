#My name is Jacob Baker and this is Chapter 7 and 8 CPX which I am completing on July 8
from adafruit_circuitplayground import cp
import time
import random


filename = "pattern.txt"


try:
    with open(filename, "r") as file:
        line = file.readline().strip()
        pin_strings = line.split(", ")
        pattern = [int(pin) for pin in pin_strings]
except OSError:
    print(f"Error: Could not open file {filename}")
    pattern = []  # Fall back to empty pattern
except ValueError:
    print("Error: Invalid data in pattern.")
    pattern = []


black = (0, 0, 0)


def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


while True:
    for index in pattern:
        color = pixel_color()
        cp.pixels[index] = color
        time.sleep(0.5)
        cp.pixels[index] = black

