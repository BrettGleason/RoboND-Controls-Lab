# Copyright (C) 2017 Electric Movement Inc.
# All Rights Reserved.

# Author: Brandon Kinman


class PIDController:
    def __init__(self, kp = 0.0, ki = 0.0, kd = 0.0, max_windup = 10):
        self.kp_ = float(kp)
        self.ki_ = float(ki)
        self.kd_ = float(kd)

        # Set max windup
        self.max_windup_ = float(max_windup)

        # Store relvant data
        self.set_point_ = 0.0
        self.error_sum_ = 0.0
        self.last_error_ = 0.0

        # Control effort history
        self.u_p = [0]
        self.u_i = [0]
        self.u_d = [0]

    def reset(self):
        self.set_point_ = 0.0
        self.kp_ = 0.0
        self.ki_ = 0.0
        self.kd_ = 0.0
        self.error_sum_ = 0.0
        self.last_error_ = 0.0
        self.last_windup_ = 0.0

    def setTarget(self, target):
        #TODO
        pass

    def setKP(self, kp):
        #TODO
        pass

    def setKI(self, ki):
        #TODO
        pass

    def setKD(self, kd):
        #TODO
        pass

    def setMaxWindup(self, max_windup):
        #TODO
        pass

    def update(self, measured_value, timestamp):
        #TODO
        pass


