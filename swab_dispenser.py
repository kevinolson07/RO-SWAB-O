import RPi.GPIO as GPIO
import time

revolutions = 1
stepsPerRev = 25
# pin used for ultrasonic signal
ping = 11
# pins used to control motor
motor_dir1 = 35
motor1 = 36
motor_dir2 = 37
motor2 = 38
pins = [motor1, motor_dir1, motor2, motor_dir2]
# setting the pin nomenclature to match the Board pinouts
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(pins,GPIO.OUT)
GPIO.setup(ping,GPIO.OUT)

while 1:
    GPIO.output(ping, GPIO.LOW)
    time.sleep(.000002)
    GPIO.output(ping, GPIO.HIGH)
    time.sleep(.000005)
    GPIO.output(ping, GPIO.LOW)

    while GPIO.input(ping) == 0:
        start_time = time.time()

    while GPIO.input(ping) == 1:
        end_time = time.time()
        duration = end_time - start_time
        distance = duration * (34000/2)
        print (distance, "cm")
        time.sleep(0.5)

   

GPIO.output(motor_dir1, GPIO.LOW)
for i in range(revolutions):
    for x in range(stepsPerRev):
        GPIO.output(motor1, GPIO.HIGH)
        time.sleep(.001)
        GPIO.output(motor1, GPIO.LOW)
        time.sleep(.001)