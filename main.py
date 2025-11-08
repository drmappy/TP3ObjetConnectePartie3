from gpiozero import LEDCharDisplay, LEDCharFont, Motor, Button, AngularServo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory 
import RPi.GPIO as GPIO

SERVO_MINIMAL_ANGLE=0.0
SERVO_MAXIMUM_ANGLE=180.0
SERVO_TICK_ANGLE=45.0
SERVO_ANGLE=SERVO_MINIMAL_ANGLE
MIN_PULSE_WIDTH=0.0005
MAX_PULSE_WIDTH=0.0025

SERVO_PIN=17

SEVEN_SEGMENT_DISPLAY_PINS = [20, 21, 19, 13, 6, 16, 12, 26]

MOTOR_PIN_1=27
MOTOR_PIN_2=22

BLUE_BUTTON_PIN=25
RED_BUTTON_PIN=5

GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setwarnings(False)

for pin in SEVEN_SEGMENT_DISPLAY_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

pin_fact = PiGPIOFactory()

servo = AngularServo(
    SERVO_PIN,
    initial_angle=SERVO_ANGLE,
    min_angle=SERVO_MINIMAL_ANGLE,
    max_angle=SERVO_MAXIMUM_ANGLE,
    min_pulse_width=MIN_PULSE_WIDTH,
    max_pulse_width=MAX_PULSE_WIDTH,
    pin_factory=pin_fact
)
motor = Motor(MOTOR_PIN_1, MOTOR_PIN_2)

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
    'A.': (1, 1, 1, 0, 1, 1, 1, 1),
    'B.': (1, 1, 1, 1, 1, 1, 1, 1),
    'C.': (1, 0, 0, 1, 1, 1, 0, 1),
    'D.': (1, 1, 1, 1, 1, 0, 0, 1),
    'E.': (1, 0, 0, 1, 1, 1, 1, 1),
    'F.': (1, 0, 0, 0, 1, 1, 1, 1),
    'G.': (1, 0, 1, 1, 1, 1, 0, 1),
    'H.': (0, 1, 1, 0, 1, 1, 1, 1),
    'I.': (0, 0, 0, 0, 1, 1, 0, 1),
    'J.': (0, 1, 1, 1, 0, 0, 0, 1),
    'K.': (1, 0, 1, 0, 1, 1, 1, 1),
    'L.': (0, 0, 0, 1, 1, 1, 0, 1),
    'M.': (1, 1, 0, 1, 0, 1, 0, 1),
    'N.': (1, 1, 1, 0, 1, 1, 0, 1),
    'O.': (1, 1, 1, 1, 1, 1, 0, 1),
    'P.': (1, 1, 0, 0, 1, 1, 1, 1),
    'Q.': (1, 1, 0, 1, 0, 1, 1, 1),
    'R.': (1, 1, 0, 1, 1, 1, 1, 1),
    'S.': (1, 0, 1, 1, 0, 1, 1, 1),
    'T.': (1, 0, 0, 0, 1, 1, 0, 1),
    'U.': (0, 1, 1, 1, 1, 1, 0, 1),
    'V.': (0, 1, 1, 1, 0, 1, 0, 1),
    'W.': (1, 0, 1, 1, 1, 0, 0, 1),
    'X.': (1, 0, 0, 1, 0, 0, 1, 1),
    'Y.': (0, 1, 0, 1, 0, 1, 1, 1),
    'Z.': (1, 1, 0, 1, 1, 0, 1, 1)
})

(SEVEN_SEGMENT_DISPLAY_PIN_A, SEVEN_SEGMENT_DISPLAY_PIN_B, SEVEN_SEGMENT_DISPLAY_PIN_C, SEVEN_SEGMENT_DISPLAY_PIN_D, SEVEN_SEGMENT_DISPLAY_PIN_E, SEVEN_SEGMENT_DISPLAY_PIN_F, SEVEN_SEGMENT_DISPLAY_PIN_G, SEVEN_SEGMENT_DISPLAY_PIN_DP) = (20, 21, 19, 13, 6, 16, 12, 26)
display = LEDCharDisplay(SEVEN_SEGMENT_DISPLAY_PIN_A, SEVEN_SEGMENT_DISPLAY_PIN_B, SEVEN_SEGMENT_DISPLAY_PIN_C, SEVEN_SEGMENT_DISPLAY_PIN_D, SEVEN_SEGMENT_DISPLAY_PIN_E, SEVEN_SEGMENT_DISPLAY_PIN_F, SEVEN_SEGMENT_DISPLAY_PIN_G, dp=SEVEN_SEGMENT_DISPLAY_PIN_DP, font=my_font, active_high=False)

def display_char(char, point = False):
    char = str(char)
    char = char.upper()
    if point:
        char += '.'
    display.value = char

def red_method():
    if(SERVO_ANGLE - SERVO_TICK_ANGLE < SERVO_MINIMAL_ANGLE):
        SERVO_ANGLE -= SERVO_TICK_ANGLE
    else:
        SERVO_ANGLE = SERVO_MAXIMUM_ANGLE
    servo.angle = SERVO_ANGLE
    motor.backward()
    

def blue_method():
    if(SERVO_ANGLE + SERVO_TICK_ANGLE > SERVO_MAXIMUM_ANGLE):
        SERVO_ANGLE += SERVO_TICK_ANGLE
    else:
        SERVO_ANGLE = SERVO_MINIMAL_ANGLE
    servo.angle = SERVO_ANGLE
    motor.forward()
    


blue = Button(BLUE_BUTTON_PIN)
red = Button(RED_BUTTON_PIN)

blue.when_pressed = blue_method
red.when_pressed = red_method

boolean_value = False
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ':
    boolean_value = not boolean_value
    display_char(char=char, point=boolean_value)
    sleep(1)

display.off()