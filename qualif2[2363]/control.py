import time


class RobotControl:
    def __init__(self):
        # set some useful constants
        self.distBetweenWheels = 0.12
        self.nTicksPerRevol = 512
        self.wheelDiameter = 0.06

    def avance(self, rb, spd, dist_obstacle):
        """

                input parameters :
                rb : robot object
                spd: speed command of left wheel and right wheel
                dist_obstacle : minimum distance to front obstacle
                duration_max : maximum duration of the move"""

        loop_iteration_time = 0.1  # control at 10 Hz (10 commands/second)
        rb.set_speed(spd, spd)

        while True:
            t0_loop = time.time()

            line = rb.get_centerline_sensors()
            sonars = rb.get_multiple_sonars(['all'])

            if 0 < sonars[0] < dist_obstacle:  # il y a un obstacle en face de nous
                rb.set_speed(0, 0) # on s'arrête avant le mur
                break  # exit from the while loop

            if line[0] > 0.8:  # le robot est trop à gauche
                rb.set_speed(spd - 15, spd + 15)

            elif line[2] > 0.8:  # le robot est trop à droite
                rb.set_speed(spd + 15, spd - 15)

            elif line[1] > 0.8:
                rb.set_speed(spd, spd)

            else:  # plus de ligne blanche

                if sonars[1] * sonars[2] != 0:
                    if abs(sonars[1] - sonars[2]) > 0.08:
                        if sonars[1] > sonars[2]:
                            rb.set_speed(spd - 6, spd + 6)
                        elif sonars[1] < sonars[2]:
                            rb.set_speed(spd + 6, spd - 6)

                    else:
                        rb.set_speed(spd, spd)

            t1_loop = time.time()
            dt_loop = t1_loop - t0_loop
            dt_sleep = loop_iteration_time - dt_loop
            if dt_sleep > 0:
                time.sleep(dt_sleep)
            else:
                print(
                    "too much computation in this loop, increase loop_iter_time or simplify computation ... ")
        # stop the robot
        rb.stop()
