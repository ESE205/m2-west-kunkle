import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
import sys

import argparse as ap

#Blink flag
flags = ap.ArgumentParser(description="Use the -n flag to specify the nmbr of blinks default is 5")
flags.add_argument("-n",type = int, default = 5, help="Number of times the LED will flash (int)")

#Dictionary to store command line args
args = flags.parse_args()
args = vars(args)

ITER_COUNT = args['n'] #Nmbr of blinks passed in CLI

pin1 = 15 #GPIO OUT LED

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   

while ITER_COUNT > 0: # Run ITER_COUNT times
   ITER_COUNT -= 1 # Decrement counter
   GPIO.output(pin1, GPIO.HIGH) # Turn on
   sleep(0.5)                     # Sleep for 1 second
   GPIO.output(pin1, GPIO.LOW)  # Turn off
   sleep(0.5)                     # Sleep for 1 second
GPIO.cleanup()

