import RPi.GPIO as GPIO
import time



#------------
# Functions
#------------


# Nema 17 motor control
def nema_motor():
    for i in range(Nema_revolutions):
        for x in range(Nema_stepsPerRev):
            GPIO.output(motor1, GPIO.HIGH)
            time.sleep(.001)
            GPIO.output(motor1, GPIO.LOW)
            time.sleep(.001)


# values for motor control
Nema_revolutions = 1
Nema_stepsPerRev = 25
motor_dir1 = 35
motor1 = 36
pins = [motor_dir1, motor1]

GPIO.setmode(GPIO.BOARD)    
GPIO.setup(pins,GPIO.OUT)
GPIO.setup(GPIO_echo,GPIO.IN)
GPIO.output(motor_dir1, GPIO.LOW)

# -------
# Main
# -------
nema_motor()