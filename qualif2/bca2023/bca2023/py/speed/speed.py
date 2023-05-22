import rob1a_v03 as rob1a  # get the robot code
import control  # robot control functions
import filt # sensors filtering functions
import numpy as np
import time

if __name__ == "__main__":
    rb = rob1a.Rob1A()   # create a robot (instance of Rob1A class)
    rb.set_pseudo ("myAwesomePseudo") # you can define your pseudo here (if not already done)
    ctrl = control.RobotControl() # create a robot controller

    # put your mission code here
    
    rb.full_end() # clean end of simulation