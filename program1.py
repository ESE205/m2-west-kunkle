#Imports neccary Lib

import RPi.GPIO as GPIO

import time

import sys

#GPIO pins on pi
switchPin = 0
LEDPin = 0

#Set Up for GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Setup for LED
GPIO.setup(switchPin, GPIO.OUT, initial=GPIO.LOW)

#Setup for switch
GPIO.setup(LEDPin,GPIO.IN)


#Controls blink behavior
def LEDBlink(rate):
    pass


#Main Method
def main():
    #time stuff
    
    startTime = time.time()
    
    while time.time()- startTime > runTime:
        
        pass
    
main()

