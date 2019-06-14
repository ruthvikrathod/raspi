import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
while True:
    GPIO.output(18,1)
    print "ledon"
    time.sleep(1)
    GPIO.output(18,0)
    print "ledoff"
    time.sleep(1)
    GPIO.output(23,1)
    print "ledon"
    time.sleep(1)
    GPIO.output(23,0)
    print "ledoff"
    time.sleep(1)
    GPIO.output(24,1)
    print "ledon"
    time.sleep(1)
    GPIO.output(24,0)
    print "ledoff"
    time.sleep(1)
    GPIO.output(25,1)
    print "ledon"
    time.sleep(1)
    GPIO.output(25,0)
    print "ledoff"
    time.sleep(1)
