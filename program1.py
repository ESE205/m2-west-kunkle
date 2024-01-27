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
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Setup for switch
GPIO.setup(15,GPIO.OUT,initial=GPIO.LOW)


#Controls LED behavior
def LEDOn(pin):
    GPIO.output(pin,GPIO.HIGH)
    
def LEDOff(pin):
    GPIO.output(pin,GPIO.LOW)
    

#Main Method
def main():
    #Script runs for 30 seconds
    startTime = time.time()
    
    while time.time()- startTime < 30.0:
        
        #Checks if the switch is on
        if(GPIO.input(switchPin)):
            
           #Turns on LED
            LEDOn(LEDPin)
            
        else:
            
            LEDOff(LEDPin)
          
          
        
    
    
main()
GPIO.cleanup()

