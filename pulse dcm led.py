import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
TRIG = 23
ECHO = 24
print "Distance Measurment In Progress"
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
print "Waiting for sensor data"

while True:
   
    
    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
          pulse_start = time.time()
    while GPIO.input (ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
#34300=Distance/time/2,     17150=Distance/time,      17150 x time = distance(cm)
    distance = pulse_duration * 17150
    distance = round(distance,0)
    if distance > 2 and distance < 150:
        print "distance",distance,"cm"
    else:
        distance < 150
        GPIO.output(12,1)
        print "LEDON"
        time.sleep(2)
        GPIO.output(12,0)
        print "ledoff"
        time.sleep(2)
        print "led will glow"
   
