import RPi.GPIO as gpio 
import time

PIN_1 = 20
PIN_2 = 21

gpio.setmode(gpio.BCM)
gpio.setup(PIN_1, gpio.OUT)
gpio.setup(PIN_2, gpio.OUT)

def moveUp():
    gpio.output(PIN_1, gpio.HIGH)
    gpio.output(PIN_2, gpio.LOW)
    time.sleep(5)
    motorStop()

def moveDown():
    gpio.output(PIN_1, gpio.LOW)
    gpio.output(PIN_2, gpio.HIGH)
    time.sleep(5)
    motorStop()

def motorStop():
    gpio.output(PIN_1, gpio.LOW)
    gpio.output(PIN_2, gpio.LOW)

if __name__ == '__main__':
    while True:
        control = input("Enter motor movement: ")
        if control == 'q':
            moveUp()
        elif control == 'w':
            moveDown()
        elif control == 'x':
            break
