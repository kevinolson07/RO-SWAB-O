import RPi.GPIO as GPIO
import time



#------------
# Functions
#------------


# Nema 17 motor control
def nema_motor():
    for i in range(revolutions):
        for x in range(stepsPerRev):
            GPIO.output(motor1, GPIO.HIGH)
            time.sleep(.001)
            GPIO.output(motor1, GPIO.LOW)
            time.sleep(.001)

# 28BYJ-48 steper motor control
def small_motor():
    print("some code")

# ultrasonic sensor measurement
def measure():
    GPIO.output(GPIO_trigger, GPIO.LOW)
    time.sleep(.000002)
    GPIO.output(GPIO_trigger, GPIO.HIGH)
    time.sleep(.000005)
    GPIO.setup(GPIO_trigger, GPIO.IN)

    
    while GPIO.input(GPIO_echo) == 0:
        start = time.time()

    while GPIO.input(GPIO_echo) == 1:
        stop = time.time()

    elapsed_time = stop - start
    distance = (elapsed * 34300)/2
    return distance


    
#-----------
# Main
#-----------
revolutions = 1
stepsPerRev = 200
# pin used for ultrasonic signal
GPIO_trigger = 11
# pins used to control motor
motor_dir1 = 35
motor1 = 36
motor_dir2 = 37
motor2 = 38
pins = [GPIO_trigger, motor1, motor_dir1, motor2, motor_dir2]
# setting the pin nomenclature to match the Board pinouts
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(pins,GPIO.OUT)
GPIO.output(motor_dir1, GPIO.LOW)

measure():

