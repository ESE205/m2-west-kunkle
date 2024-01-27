#Imports neccary Lib

import RPi.GPIO as GPIO

import time

import sys

import argparse as ap

import os



#GPIO pins on pi
switchPin = 16
LEDPin = 15

#Set Up for GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Setup for LED
GPIO.setup(LEDPin, GPIO.OUT, initial=GPIO.LOW)

#Setup for switch
GPIO.setup(switchPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)


#Controls blink behavior
def LEDBlink(rate=1.0,pin=LEDPi,f = file):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(rate)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(rate)
    



def output():
    #Creates sequential outputfiles
    if os.path.exists("outputs"):
        if os.path.exists("outputs/data.txt"):
            files = os.listdir("outputs")
            files.sort()
            nmbr = files[-1]
            nmbr = int(nmbr[nmbr.rindex('a')+1])
            f = open("data%d.txt" % nmbr,w)
            return f
        else:
            f = open("data.txt",w)
            return f
            
    else:
        os.mkdir("outputs")
        ouput()

        
        
    

#Main Method
def main(runTime):
    
    #time stuff
    startTime = time.time()
  
    while time.time()- startTime < runTime:
        
        #Checks if the switch is on
        if(GPIO.input(switchPin)):
            #Blinks
            LEDBlink(f)
            
        else:
            
            LEDOff(LEDPin)
        
        

file = ouput()
main()
GPIO.cleanup()

