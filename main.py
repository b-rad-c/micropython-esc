from esc import ESC
import time
import pyb


led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
led4 = pyb.LED(4)

led1.on()

motor1 = ESC(1)
motor2 = ESC(2)

motor1.calibrate()
motor2.calibrate()

led2.on()


time.sleep(3)

motor1.throttle(50)
motor2.throttle(50)

led3.on()
time.sleep(1)

motor1.throttle(0)
motor2.throttle(0)

led4.on()


def adjust(**kwargs):
    left = kwargs.get('l')
    right = kwargs.get('r')
    if left is not None:
        motor1.throttle(left)
    if right is not None:
        motor2.throttle(right)


def off():
    motor1.throttle(0)
    motor2.throttle(0)
