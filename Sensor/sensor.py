#!/usr/bin/python

# Start by importing the libraries we want to use
import RPi.GPIO as GPIO  # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time  # This is the time library, we need this so we can use the sleep function

# Define some variables to be used later on in our script

# This is the message that will be printed when NO moisture is detected
message_dead = "Warning, no moisture detected! Plant death imminent!!! :'("

# This is the message that will be printed when moisture IS detected again
message_alive = "Panic over! Plant has water again :)"

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
channel = 17
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

# This is an infinite loop to keep our script running
while True:
    # Check the sensor value
    if GPIO.input(channel):
        print("LED off")
        print(message_dead)
    else:
        print("LED on")
        print(message_alive)
    
    # Wait for a minute before checking again
    time.sleep(60)
