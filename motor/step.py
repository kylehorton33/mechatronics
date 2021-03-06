#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
import os

## Initialize input pins for ULN2003A
GPIO.setmode(GPIO.BOARD)

IN1=18 # IN1
IN2=22 # IN2
IN3=24 # IN3
IN4=26 # IN4

# ??
time = 0.001

# Setup Pins
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

def Step1():
    GPIO.output(IN4, True)
    sleep (time)
    GPIO.output(IN4, False)

def Step2():
    GPIO.output(IN4, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

def Step3():
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN3, False)

def Step4():
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)

def Step5():
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN2, False)

def Step6():
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

def Step7():
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN1, False)

def Step8():
    GPIO.output(IN4, True)
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN1, False)

def left(step):	
	for i in range (step):   
		Step1()
		Step2()
		Step3()
		Step4()
		Step5()
		Step6()
		Step7()
		Step8()
		print "Step left: ",i

def right(step):
	for i in range (step):
		Step8()
		Step7()
		Step6()
		Step5()
		Step4()
		Step3()
		Step2()
		Step1()  
		print "Step right: ",i	

while(True):
	steps = raw_input("How many steps? (e.g. Left,4):\n")
	dir,step = steps.split(",")
	try:
		n_step = int(step)
	except:
		print("not a number")
		continue
	if dir.lower() == "left":
		left(n_step)
	if dir.lower() == "right":
		right(n_step)

GPIO.cleanup()
