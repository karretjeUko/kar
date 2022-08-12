from machine import Pin, PWM
import utime
import sys
import _thread

led_g = Pin(2, Pin.OUT)
led_r = Pin(1, Pin.OUT)
servo = PWM(Pin(0))
servo.freq(50)
button = Pin(17, Pin.IN, Pin.PULL_DOWN)

speed = 0.002
pin_a = Pin(12, Pin.OUT) #def output pin
pin_b = Pin(13, Pin.OUT)
pin_c = Pin(14, Pin.OUT)
pin_d = Pin(15, Pin.OUT)

pin_a.low() #pins low
pin_b.low()
pin_c.low()
pin_d.low()

rotate_steps_cw = [[0,0,1,1],[0,1,1,0],[1,1,0,0],[1,0,0,1]]

rotate_steps_acw = [[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]]

number_of_steps_cw = 1
number_of_steps_acw = 1

button_cw = Pin(6, Pin.IN, Pin.PULL_DOWN)
button_acw = Pin(16, Pin.IN, Pin.PULL_DOWN)
rotation = "cw"
global button_pressed
button_pressed = False
def button_reader_thread():
    global button_pressed
    while True:
        if button_cw.value() == 1:
            rotation = "cw"
        #if rotation == "cw":
            for step in rotate_steps_cw:
                pin_a.value(step[0])
                pin_b.value(step[1])
                pin_c.value(step[2])
                pin_d.value(step[3])
                utime.sleep(speed)
            number_of_steps_cw +=1
            print(number_of_steps_cw)
        #if rotation == "acw":
            for step in rotate_steps_acw:
                pin_a.value(step[0])
                pin_b.value(step[1])
                pin_c.value(step[2])
                pin_d.value(step[3])
                utime.sleep(speed)
            number_of_steps_acw +=1
            print(number_of_steps_acw)
        #if number_of_steps_acw == 800:
            rotation = "cw"
            number_of_steps_acw = 0
        if button_acw.value() == 1:
            rotation = "acw"
            led-r.value(1)
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)
_thread.start_new_thread(button_reader_thread,())
while True:
    if button_pressed == True :
        for i in range(20):
            led_g.value(1)
            utime.sleep(0.2)
            led_g.value(0)
            utime.sleep(0.2)
            servo.duty_u16(4000)
            utime.sleep(1)
            servo.duty_u16(1800)
            utime.sleep(0.4)
        global button_pressed
        button_pressed = False



        global button_cw_pressed
        button_cw_pressed = False

        rotation = "cw"

       # number_of_steps_cw =1
        #number_of_steps_acw =1

   # while number_of_steps_cw == max_steps_cw:


        #pin_a.low()
        #pin_b.low()
        #pin_c.low()
        #pin_d.low()

        #led.value(0)
       # utime.sleep(3)
