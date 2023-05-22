import rob1a_v03 as rob1a  # get the robot code
import control  # robot control functions
import filt  # sensors filtering functions
import numpy as np
import time

if __name__ == "__main__":
    rb = rob1a.Rob1A()  # create a robot (instance of Rob1A class)
    rb.set_pseudo("Volato")  # you can define your pseudo here (if not already done)
    ctrl = control.RobotControl()  # create a robot controller

    # print ("No log file")
    # rb.set_log(0)   # do not log data (set to 1 for logging data)
    print("Logging telemetry")
    rb.set_log(1)  # do not log data (set to 1 for logging data)

    # aller tout droit jusqu'à ce que le sonar détecte un obstacle à moins de 0.3 m
    speed = 250
    dist_obstacle = 0.3  # 30cm

    ctrl.avance(rb, speed, dist_obstacle)

    rb.full_end()  # clean end of simulation
