import tkinter as tk
from gpiozero import Motor
from main import display_char, motor, servo_up, servo_down, read_joystick, configure_buttons
from time import sleep
import threading

def joystick_loop():
    while True:
        read_joystick()
        sleep(0.1)

configure_buttons()

def on_servo_buttonMinus_click():
    servo_down()
    
def on_servo_buttonPlus_click():
    servo_up()
    
def on_motor_buttonPlus_click():
    motor.forward(0.4)
    sleep(1)
    motor.stop()
    
def on_motor_buttonMinus_click():
    motor.backward(0.4)
    sleep(1)
    motor.stop()
    
def on_textbox_button_click():
    input_text = textBox.get()
    for i, char in enumerate(input_text):
        has_next_point = i + 1 < len(input_text) and input_text[i + 1] == '.'
        if char != '.':
            display_char(char, point=has_next_point)
            sleep(0.5)
    display_char(' ')

root = tk.Tk()
root.title("Tp3 partie 3")
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

top_frame = tk.Frame(frame)
top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

textInputButton = tk.Button(top_frame, text="Texte à faire défiler sur les segments :", command=on_textbox_button_click)
textBox = tk.Entry(top_frame, width=30)

textInputButton.pack(side=tk.LEFT)
textBox.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=(10,0))

middle_frame = tk.Frame(frame)
middle_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=(0,5))

servoPlusButton = tk.Button(middle_frame, text="Servo tourne de -45 degres", bg="red", command=on_servo_buttonMinus_click)
servoMinusButton = tk.Button(middle_frame, text="Servo tourne de +45 degres", bg="blue", command=on_servo_buttonPlus_click)

servoMinusButton.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0,30))
servoPlusButton.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(30,0))

bottom_frame = tk.Frame(frame)
bottom_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

motorPlusButton = tk.Button(bottom_frame, text="Moteur tourne en sens +", command=on_motor_buttonPlus_click)
motorMinusButton = tk.Button(bottom_frame, text="Moteur tourne en sens -", command=on_motor_buttonMinus_click)

motorMinusButton.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0,40))
motorPlusButton.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(35,0))

thread = threading.Thread(target=joystick_loop, daemon=True)
thread.start()

root.mainloop()