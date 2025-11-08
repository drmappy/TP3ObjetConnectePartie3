from gpiozero import LEDCharDisplay, LEDCharFont, Motor, Button
from time import sleep
pin_fact = PiGPIOFactory()


servo = AngularServo(
    17,
    initial_angle=0.0,
    min_angle=0.0,
    max_angle=180.0,
    min_pulse_width=0.0005,
    max_pulse_width=0.0025,
    pin_factory=pin_fact
)

my_font = LEDCharFont({
    ' ': (0, 0, 0, 0, 0, 0, 0),
    'A': (1, 1, 1, 0, 1, 1, 1),
    'B': (1, 1, 1, 1, 1, 1, 1),
    'C': (1, 0, 0, 1, 1, 1, 0),
    'D': (1, 1, 1, 1, 1, 0, 0),
    'E': (1, 0, 0, 1, 1, 1, 1),
    'F': (1, 0, 0, 0, 1, 1, 1),
    'G': (1, 0, 1, 1, 1, 1, 0),
    'H': (0, 1, 1, 0, 1, 1, 1),
    'I': (0, 0, 0, 0, 1, 1, 0),
    'J': (0, 1, 1, 1, 0, 0, 0),
    'K': (1, 0, 1, 0, 1, 1, 1),
    'L': (0, 0, 0, 1, 1, 1, 0),
    'M': (1, 1, 0, 1, 0, 1, 0),
    'N': (1, 1, 1, 0, 1, 1, 0),
    'O': (1, 1, 1, 1, 1, 1, 0),
    'P': (1, 1, 0, 0, 1, 1, 1),
    'Q': (1, 1, 0, 1, 0, 1, 1),
    'R': (1, 1, 0, 1, 1, 1, 1),
    'S': (1, 0, 1, 1, 0, 1, 1),
    'T': (1, 0, 0, 0, 1, 1, 0),
    'U': (0, 1, 1, 1, 1, 1, 0),
    'V': (0, 1, 1, 1, 0, 1, 0),
    'W': (1, 0, 1, 1, 1, 0, 0),
    'X': (1, 0, 0, 1, 0, 0, 1),
    'Y': (0, 1, 0, 1, 0, 1, 1),
    'Z': (1, 1, 0, 1, 1, 0, 1),
    '1': (0, 1, 1, 0, 0, 0, 0),
    '2': (1, 1, 0, 1, 1, 0, 1),
    '3': (1, 1, 1, 1, 0, 0, 1),
    '4': (0, 1, 1, 0, 0, 1, 1),
    '5': (1, 0, 1, 1, 0, 1, 1),
    '6': (1, 0, 1, 1, 1, 1, 1),
    '7': (1, 1, 1, 0, 0, 0, 0),
    '8': (1, 1, 1, 1, 1, 1, 1),
    '9': (1, 1, 1, 1, 0, 1, 1),
    '0': (1, 1, 1, 1, 1, 1, 0),
})

(A, B, C, D, E, F, G, DP) = (20, 21, 19, 13, 6, 16, 12, 26)
display = LEDCharDisplay(A, B, C, D, E, F, G, dp=DP, font=my_font, active_high=False)

motor = Motor(27, 22)
motor.forward()

def red_method():
    print("red")

def blue_method():
    print("blue")

blue = Button(5)
red = Button(25)

blue.when_activated(blue_method)
red.when_activated(red_method)

for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ':
    display.value = char
    sleep(1)
servo.angle = 0.0
sleep(1)
servo.angle = 45.0
sleep(1)
servo.angle = 90.0
sleep(1)
servo.angle = 135.0
sleep(1)
servo.angle = 180.0

display.off()