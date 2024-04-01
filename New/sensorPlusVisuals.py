#!/usr/bin/python
# Start by importing the libraries we want to use
import RPi.GPIO as GPIO  # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time  # This is the time library, we need this so we can use the sleep function
from waterMePlease import waterMePlease

# This is the message that will be printed when NO moisture is detected

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
channel = 17
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

# This is an infinite loop to keep our script running

def change_sensor_state(state):
    if state == "ON":
        GPIO.output(channel, GPIO.HIGH)
    elif state == "OFF":
        waterMePlease()
    else:
        print("Invalid state. Please enter either 'ON' or 'OFF'.")


while True:
    # Check the sensor value
    if GPIO.input(channel):
        print("LED off")
        change_sensor_state("OFF")
        # Check time, if during the eve, shout every 15.
        # After shouting, check for chat back
    else:
        print("LED on")
        change_sensor_state("ON")
    
    # Wait for a minute before checking again
    time.sleep(10)


    