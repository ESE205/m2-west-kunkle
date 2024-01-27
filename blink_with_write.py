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

#Command Line Arguments
flags = ap.ArgumentParser(description="Use the --runtime flag to duration the script will run (default is 60) \n")
flags.add_argument("--runtime",type = float, default = 30.0, help="Duration the script will run in seconds (float)")
flags.add_argument("--blinkrate",type = float, default = 1.0, help="Set the blink rate of the LED in seconds (float)")
flags.add_argument("--debug",type = bool, defualt = False, help="Prints: system time, # iterations,and switch state (boolean)")
#Dictionary to store command line args
args = flags.parse_args()
args = vars(args)

#Controls blink behavior
def LEDBlink(rate=1.0,pin=LEDPin,f = file):
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
main(runTime)
GPIO.cleanup()

