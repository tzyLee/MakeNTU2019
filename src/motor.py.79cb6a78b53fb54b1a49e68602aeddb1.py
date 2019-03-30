# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

MIN_PULSE_WIDTH = 650
MAX_PULSE_WIDTH = 2350
FREQUENCY = 60

# Helper function to make setting a servo pulse width simpler.
def pulse_width(angle):
    pulse_w = angle * (MAX_PULSE_WIDTH - MIN_PULSE_WIDTH) / 180 + MIN_PULSE_WIDTH
    analog_value = int(float(pulse_w) / 1000000 * FREQUENCY * 4096)
    return analog_value

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(FREQUENCY)

print('Moving servo on channel 0,f press Ctrl-C to quit...')
def rotateMotor(channel, wait, angle):
    pwm.set_pwm(channel, 0, pulse_width(angle))
    time.sleep(wait)

def reset():
    rotateMotor(4, 1, 90)
    rotateMotor(7, 1, 0)
    rotateMotor(11, 1, 0)

if __name__ == '__main__':
    # Channel 0 : 180 = book, 90 = idle
    # Channel 4 : 0 = book, 90 = idle
    # Chennel 3: 180 = idle, flip to 0
    # Channel 7: idle = 0, flip to 180
    
    #rotateMotor(11, 1, 180)
    
    rotateMotor(4, 1, 0)
    rotateMotor(7, 1, 180)
    rotateMotor(11, 1, 180)
    
    #rotateMotor(7, 1, 0)
