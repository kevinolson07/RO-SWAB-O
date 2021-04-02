import RPi.GPIO as GPIO
import time

revolutions = 1
stepsPerRev = 200
# pins used to control motor
motor_dir1 = 35
motor1 = 36
motor_dir2 = 37
motor2 = 38
pins = [35, 36, 37, 38]
# setting the pin nomenclature to match the Board pinouts
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(pins,GPIO.OUT)


GPIO.output(motor_dir1, GPIO.LOW)
for i in range(revolutions):
    for x in range(stepsPerRev):
        GPIO.output(motor1, GPIO.HIGH)
        time.sleep(.001)
        GPIO.output(motor1, GPIO.LOW)
        time.sleep(.001)