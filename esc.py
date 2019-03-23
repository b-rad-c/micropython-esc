import pyb


class ESC:

    MIN_ANGLE = -33
    MAX_ANGLE = 31

    def __init__(self, servo_number):
        """
        Object to control a brushless motor via esc
        :param servo_number: (int) the pyboard servo input, must be 1 - 4
        """
        self.servo_number = servo_number
        self.servo = pyb.Servo(self.servo_number)
        self.power = 0

        # used by throttle method to convert power from 0 - 100 to angle sent to servo object
        self.throttle_interval = abs(self.MAX_ANGLE - self.MIN_ANGLE) / 100

    def calibrate(self):
        """
        calibration for simonk esc
        :return: None
        """
        self.servo.angle(-90, 1250)
        pyb.delay(1250)
        self.servo.angle(90, 100)
        pyb.delay(100)
        self.throttle(0)

    def throttle(self, power):
        """
        set the throttle of the esc
        :param power: (int) 0 - 100
        :return: None
        """
        self.servo.angle(int(self.MIN_ANGLE + self.throttle_interval * power), 0)
