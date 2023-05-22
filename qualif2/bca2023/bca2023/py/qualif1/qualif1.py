import rob1a_v03 as rob1a  # get the robot code
import control  # robot control functions
import filt # sensors filtering functions
import time

if __name__ == "__main__":
    rb = rob1a.Rob1A()   # create a robot (instance of Rob1A class)
    rb.set_pseudo ("myAwesomePseudo") # you can define your pseudo here
    ctrl = control.RobotControl() # create a robot controller

    print ("No log file")
    rb.set_log(0)   # do not log data (set to 1 for logging data)

    print ("Go !!!")
    speed_left = 900 # set speed on 10 bits [0 1023]
    speed_right = speed_left # same speed on both wheels, straight line (perfect robot)
    dist_obstacle = 0.30 # stops at 30 cm of a front obstacle
    duration_max = 60.0 # set a max duration of 1 minute
    ctrl.test_move_until_obstacle (rb,speed_left,speed_right,dist_obstacle,duration_max)
    print ("End of motion")

    rb.full_end() # clean end of simulation
