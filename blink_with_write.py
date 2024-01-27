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
flags.add_argument("--debug",type = bool, default = False, help="Prints: system time, # iterations,and switch state (boolean)")
#Dictionary to store command line args
args = flags.parse_args()
args = vars(args)

RUNTIME = args["runtime"]
BLINKRATE = args["blinkrate"]
DEBUG = args["debug"]

#Controls blink behavior
def LEDBlink(f,rate=1.0,pin=LEDPin):
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
    if DEBUG:
        print("The start time is: "+startTime)
        iterartions = 1
  
    while time.time()- startTime < runTime:
        #Checks if the switch is on
        if(GPIO.input(switchPin)):
            if DEBUG:
                print("The current time is: "+time.time()+"\nIteration: "+iterations+"\nThe LED is On")
        
            #Blinks
            LEDBlink(f=file)
            
        else:
            if DEBUG:
                print("The current time is: "+time.time()+"\nIteration: "+iterations+"\nThe LED is OFF")
            LEDOff(LEDPin)
        
    

file = ouput()
main(RUNTIME)
GPIO.cleanup()

