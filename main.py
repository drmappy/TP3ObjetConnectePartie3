from gpiozero import LEDCharDisplay, LEDCharFont, Motor, Button, AngularServo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory 
import RPi.GPIO as GPIO
from ADC_Composant import * # Assurez-vous qu’il soit présent 
import sys
SERVO_MINIMAL_ANGLE=0.0
SERVO_MAXIMUM_ANGLE=180.0
SERVO_TICK_ANGLE=45.0
servo_angle=SERVO_MINIMAL_ANGLE
MIN_PULSE_WIDTH=0.0005
MAX_PULSE_WIDTH=0.0025

SERVO_PIN=18

SEVEN_SEGMENT_DISPLAY_PINS = [20, 21, 19, 13, 6, 16, 12, 26]
(SEVEN_SEGMENT_DISPLAY_PIN_A, SEVEN_SEGMENT_DISPLAY_PIN_B, SEVEN_SEGMENT_DISPLAY_PIN_C, SEVEN_SEGMENT_DISPLAY_PIN_D, SEVEN_SEGMENT_DISPLAY_PIN_E, SEVEN_SEGMENT_DISPLAY_PIN_F, SEVEN_SEGMENT_DISPLAY_PIN_G, SEVEN_SEGMENT_DISPLAY_PIN_DP) = (20, 21, 19, 13, 6, 16, 12, 26)

MOTOR_PIN_1=27
MOTOR_PIN_2=22

BLUE_BUTTON_PIN=25
RED_BUTTON_PIN=5

adc = ADC_Composant()

if(adc.detecteI2C(0x4b)): 
    adc = ADS7830() 
else: 
    sys.exit("I2C non connecté sur votre Pi et/ou ADS7830")

GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setwarnings(False)

for pin in SEVEN_SEGMENT_DISPLAY_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

GPIO.setup(SEVEN_SEGMENT_DISPLAY_PIN_DP, GPIO.OUT)

pin_fact = PiGPIOFactory()

servo = AngularServo(
    SERVO_PIN,
    initial_angle=servo_angle,
    min_angle=SERVO_MINIMAL_ANGLE,
    max_angle=SERVO_MAXIMUM_ANGLE,
    min_pulse_width=MIN_PULSE_WIDTH,
    max_pulse_width=MAX_PULSE_WIDTH,
    pin_factory=pin_fact
)
motor = Motor(MOTOR_PIN_1, MOTOR_PIN_2)
def servo_down():
    global servo_angle, servo
    if servo_angle - SERVO_TICK_ANGLE < SERVO_MINIMAL_ANGLE:
        servo_angle = SERVO_MAXIMUM_ANGLE
    else:
        servo_angle -= SERVO_TICK_ANGLE
    servo.angle = servo_angle
    display_servo_angle()

def servo_up():
    global servo_angle, servo
    if servo_angle + SERVO_TICK_ANGLE > SERVO_MAXIMUM_ANGLE:
        servo_angle = SERVO_MINIMAL_ANGLE
    else:
        servo_angle += SERVO_TICK_ANGLE
    servo.angle = servo_angle
    display_servo_angle()
    
def display_servo_angle():
    if servo_angle == 0:
        display_char(int(1))
        return
    display_char(int(6 - 180 / servo_angle))

# Move button initialization to the global scope
blue = Button(BLUE_BUTTON_PIN)
red = Button(RED_BUTTON_PIN)

# Configure button actions
def configure_buttons():
    blue.when_pressed = servo_up
    red.when_pressed = servo_down

# Call this function to set up buttons
configure_buttons()

my_font = LEDCharFont({
    ' ': (0, 0, 0, 0, 0, 0, 0, 0),
    'A': (1, 1, 1, 0, 1, 1, 1, 0),
    'B': (1, 1, 1, 1, 1, 1, 1, 0),
    'C': (1, 0, 0, 1, 1, 1, 0, 0),
    'D': (1, 1, 1, 1, 1, 0, 0, 0),
    'E': (1, 0, 0, 1, 1, 1, 1, 0),
    'F': (1, 0, 0, 0, 1, 1, 1, 0),
    'G': (1, 0, 1, 1, 1, 1, 0, 0),
    'H': (0, 1, 1, 0, 1, 1, 1, 0),
    'I': (0, 0, 0, 0, 1, 1, 0, 0),
    'J': (0, 1, 1, 1, 0, 0, 0, 0),
    'K': (1, 0, 1, 0, 1, 1, 1, 0),
    'L': (0, 0, 0, 1, 1, 1, 0, 0),
    'M': (1, 1, 0, 1, 0, 1, 0, 0),
    'N': (1, 1, 1, 0, 1, 1, 0, 0),
    'O': (1, 1, 1, 1, 1, 1, 0, 0),
    'P': (1, 1, 0, 0, 1, 1, 1, 0),
    'Q': (1, 1, 0, 1, 0, 1, 1, 0),
    'R': (1, 1, 0, 1, 1, 1, 1, 0),
    'S': (1, 0, 1, 1, 0, 1, 1, 0),
    'T': (1, 0, 0, 0, 1, 1, 0, 0),
    'U': (0, 1, 1, 1, 1, 1, 0, 0),
    'V': (0, 1, 1, 1, 0, 1, 0, 0),
    'W': (1, 0, 1, 1, 1, 0, 0, 0),
    'X': (1, 0, 0, 1, 0, 0, 1, 0),
    'Y': (0, 1, 0, 1, 0, 1, 1, 0),
    'Z': (1, 1, 0, 1, 1, 0, 1, 0),
    '0':(1, 1, 1, 1, 1, 1, 0, 0),
    '1':(0, 1, 1, 0, 0, 0, 0, 0),
    '2':(1, 1, 0, 1, 1, 0, 1, 0),
    '3':(1, 1, 1, 1, 0, 0, 1, 0),
    '4':(0, 1, 1, 0, 0, 1, 1, 0),
    '5':(1, 0, 1, 1, 0, 1, 1, 0),
    '6':(1, 0, 1, 1, 1, 1, 1, 0),
    '7':(1, 1, 1, 0, 0, 0, 0, 0),
    '8':(1, 1, 1, 1, 1, 1, 1, 0),
    '9':(1, 1, 1, 1, 0, 1, 1, 0),
})

display = LEDCharDisplay(SEVEN_SEGMENT_DISPLAY_PIN_A, SEVEN_SEGMENT_DISPLAY_PIN_B, SEVEN_SEGMENT_DISPLAY_PIN_C, SEVEN_SEGMENT_DISPLAY_PIN_D, SEVEN_SEGMENT_DISPLAY_PIN_E, SEVEN_SEGMENT_DISPLAY_PIN_F, SEVEN_SEGMENT_DISPLAY_PIN_G, font=my_font, active_high=False)

def read_joystick():
    global servo, motor
    trigger_x = adc.lectureAnalogique(0)
    trigger_y = adc.lectureAnalogique(1)
    SOUTH = trigger_y < 55 and trigger_x >= 55 and trigger_x <= 200
    NORTH = trigger_y > 200 and trigger_x >= 55 and trigger_x <= 200
    WEST = trigger_x > 200 and trigger_y >= 55 and trigger_y <= 200
    EAST = trigger_x < 55 and trigger_y >= 55 and trigger_y <= 200
    if WEST:
        servo_up()
    elif EAST:
        servo_down()
    elif SOUTH:
        motor.backward(0.4)
        sleep(1)
        motor.stop()
    elif NORTH :
        motor.forward(0.4)
        sleep(1)
        motor.stop()        

def display_char(char, point = False):
    global display
    char = str(char)
    char = char.upper()
    if point:
        GPIO.output(SEVEN_SEGMENT_DISPLAY_PIN_DP, GPIO.LOW)
    else:
        GPIO.output(SEVEN_SEGMENT_DISPLAY_PIN_DP, GPIO.HIGH)
    display.value = char


    

if __name__ == "__main__":

    boolean_value = False
    for char in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ':
        boolean_value = not boolean_value
        #A. B C. D
        display_char(char=char, point=boolean_value)
        read_joystick()
        sleep(1)

    display.off()