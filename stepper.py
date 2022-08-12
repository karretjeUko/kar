from machine import Pin, PWM
import utime
import sys
import _thread
servo = PWM(Pin(0))
servo.freq(50)
led_r = Pin(1, machine.Pin.OUT)
led_g = Pin(2, machine.Pin.OUT)

button = Pin(16, Pin.IN, Pin.PULL_DOWN)

print("hello world")

global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed

    while True:
        led_r.value(1)


        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)
_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True :
        #led_r.value(1)
        for i in range(10):
            led_g.value(1)
            utime.sleep(0.3)
            led_g.value(0)
            utime.sleep(0.3)
            servo.duty_u16(4000)
            utime.sleep(0.5)
            servo.duty_u16(1800)
            utime.sleep(0.5)

        global button_pressed
        button_pressed = False
