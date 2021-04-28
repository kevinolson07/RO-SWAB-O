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



# 28BYJ-48 steper motor control
def small_motor():
    print("some code")
    delay = .005
    seq = list(range(0,4))
    seq[0] = [1,0,0,0]
    seq[1] = [0,1,0,0]
    seq[2] = [0,0,1,0]
    seq[3] = [0,0,0,1]

    # seq[4] = [1,0,0,0]
    # seq[5] = [0,1,0,0]
    # seq[6] = [0,0,1,0]
    # seq[7] = [0,0,0,1]
    for j in range(100):
        for i in range(0,4):
            GPIO.output(coil_A_1,seq[i][0])
            GPIO.output(coil_A_2,seq[i][1])
            GPIO.output(coil_B_1,seq[i][2])
            GPIO.output(coil_B_2,seq[i][3])
            time.sleep(delay)

# ultrasonic sensor measurement

def measure():
    GPIO.output(GPIO_trigger, False)
    time.sleep(.25)
    GPIO.output(GPIO_trigger, True)
    time.sleep(.00001)
    GPIO.output(GPIO_trigger, False)
    while GPIO.input(GPIO_echo) == 0:
        start = time.time()
    while GPIO.input(GPIO_echo) == 1:
        stop = time.time()

#     GPIO.setup(GPIO_trigger, GPIO.OUT)
#     GPIO.output(GPIO_trigger, GPIO.LOW)
#     time.sleep(.000002)
#     GPIO.output(GPIO_trigger, GPIO.HIGH)
#     time.sleep(.000005)
#     GPIO.setup(GPIO_trigger, GPIO.IN)

    
#     while GPIO.input(GPIO_trigger) == 0:
#         start = time.time()

#     while GPIO.input(GPIO_trigger) == 1:
#         stop = time.time()

    elapsed_time = stop - start
    distance = (elapsed_time * 34000)/2
    return distance


    
#-----------
# Main
#-----------
counter = 0

# values for motor control
Nema_revolutions = 1
Nema_stepsPerRev = 25
# pin used for ultrasonic signal
GPIO_trigger = 16
GPIO_echo = 18
# pins used to control Nema motor
motor_dir1 = 35
motor1 = 36
# Pins used to control 28BYJ-48 stepper motor
coil_A_1 = 33
coil_A_2 = 37
coil_B_1 = 38
coil_B_2 = 40

pins = [GPIO_trigger, motor1, motor_dir1, coil_A_1, coil_A_2, coil_B_1, coil_B_2]
# setting the pin nomenclature to match the Board pinouts
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(pins,GPIO.OUT)
GPIO.setup(GPIO_echo,GPIO.IN)
GPIO.output(motor_dir1, GPIO.LOW)

while 1:
    print(counter)
    distance = measure()
    print(distance, "cm")
    time.sleep(.25)
    if distance >= 40:
        counter += 1
        small_motor()
        if counter >= 6:
            nema_motor()
            print("nema motor function ran!!!!!!!")
            counter = 0
    else:
        counter = 0