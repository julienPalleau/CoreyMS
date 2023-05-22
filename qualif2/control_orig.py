import time


class RobotControl:
    def __init__(self):
        # set some useful constants
        self.distBetweenWheels = 0.12
        self.nTicksPerRevol = 512
        self.wheelDiameter = 0.06

    def test_move_until_obstacle(self, rb, speed_left, speed_right, dist_obstacle, duration_max):
        """
        Example of test function to check if the robot moves and stops on front obstacle

        input parameters :
        rb : robot object
        speed_left : speed command of left wheel
        speed_right : speed command of right wheel
        dist_obstacle : minimu distance to front obstacle
        duration_max : maximum duration of the move

        output paremeters :
        None
        """
        loop_iter_time = 0.1  # control at 10 Hz (10 commands/second)
        t_start = time.time()
        while True:
            t0loop = time.time()
            if (time.time() - t_start) > duration_max:
                break  # max time reached , escape the loop ...
            df = rb.get_sonar("front")  # get distance from front sonar
            if df > 0.0:
                print("front sonar distance = %.2f m" % (df))  # debug : print front distance on terminal
            if 0.0 < df < dist_obstacle:
                break  # obstacle at less than 25 cm , escape the loop ...
            # forward motion
            rb.set_speed(speed_left, speed_right)
            # end of loop
            t1loop = time.time()
            dt_sleep = loop_iter_time - (t1loop - t0loop)
            if dt_sleep > 0:
                time.sleep(dt_sleep)  # wait to have perfect loop duration
            else:
                print("too much computation in this loop, increase loop_iter_time or simplify computation ... ")
                # stop the robot
        rb.stop()
