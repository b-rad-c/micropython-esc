# micropython-esc
A simple interface for controlling a simonk esc using the pyboard and micropython.

main.py is setup to assume you have 1 esc plugged in X1 servo input.

##### example
Not much to see here, sample below, see esc.py for documentation.

    from esc import ESC
    esc = ESC(1)
    esc.calibrate()
    esc.throttle(0)
    esc.throttle(50)
    esc.throttle(100)

##### calibration
Only need to run the calibrate method once each time the esc is powered on. This method is for the simonk esc firmware, see your esc documentation.

The MIN_ANGLE and MAX_ANGLE class attributes correspond to the servo angle where my escs begin and stop responding to angle changes to the servo class. Your hardware may differ.
#####wiring and power
Plug your esc connection into the input corresponding to the servo_number you supply when instantiating the ESC class.

Your ESC can power the pyboard if you plug in the red wire from the esc. If connecting more than 1 esc do not connect more power wires than the pyboard can handle. For me (and probably you too) this is 1.

If powering via USB or other external power, do not connect any power wires from any esc.

##### no warranty
No warranty is given or implied with use of this software. I am not responsible for any damage or injury caused by your use of this software. It is your responsibility to verify all information given and that your hardware is compatible with this software.
