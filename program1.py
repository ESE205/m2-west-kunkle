#Imports neccary Lib

import RPi.GPIO as GPIO

import time

import sys

import argparse as ap

#GPIO pins on pi
switchPin = 16
LEDPin = 15

#Set Up for GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Setup for LED
GPIO.setup(switchPin, GPIO.OUT, initial=GPIO.LOW)

#Setup for switch
GPIO.setup(LEDPin,GPIO.IN)


#Controls LED behavior
def LEDOn(LEDPIN):
    GPIO.output(LEDPIN,GPIO.HIGH)
    return
    
def LEDOff(LEDPIN):
    GPIO.output(LEDPIN,GPIO.HIGH)
    return

#Main Method
def main():
    #Script runs for 60 seconds
    startTime = time.time()
    while time.time()- startTime < 60.0:
        #Checks if the switch is on
        if(GPIO.input(switchPin)
           #Turns on LED
           LEDOn(LEDPin)
        else:
           LEDOff(LEDPin)
    
    
main()

