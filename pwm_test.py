
import time
import board
import analogio
import digitalio
import pwmio
import random

led_sys = digitalio.DigitalInOut(board.GP19)
led_sys.direction = digitalio.Direction.OUTPUT

#v_shift = digitalio.DigitalInOut(board.GP21)
#v_shift.direction = digitalio.Direction.OUTPUT
v_shift = pwmio.PWMOut(board.GP21, frequency=10000, duty_cycle=0)
#v_shift.value = True

potentiometer = analogio.AnalogIn(board.GP26)

get_voltage = 5.6 / 65535
led_sys.value = True

while True:

    for i in range(1000):
        # PWM LED up and down
        if i < 500:
            v_shift.duty_cycle = int(i * 2 * 65535 / 1000)  # Up

        else:
            v_shift.duty_cycle = 65535 - int((i - 500) * 2 * 65535 / 1000)  # Down
        time.sleep(0.1)
        #if random.random() < 0.1:
        #    time.sleep(0.25)
        
        voltage = potentiometer.value * get_voltage
        print(voltage)

    #time.sleep(0.1)

