#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from lib.log import *
from high_stakes.events import *

open_log("red-awp-left.csv")

def driver_function():
    pass

def autonomous_function():
    intake_1st_stage.set_velocity(470, RPM)
    intake_2nd_stage.set_velocity(470, RPM)
    pid_driver.drive(-1000, True)
    clamp.set(True)
    pid_turner.turn(80, FRAME_HEADING_RELATIVE)
    
    reset_odometry()
    
    intake_1st_stage.spin(REVERSE)
    intake_2nd_stage.spin(FORWARD)
    wait(1000, MSEC)
    pid_driver.drive(600, True)
    pid_turner.turn(80, FRAME_HEADING_RELATIVE)
    pid_driver.drive(270, True)
    
    wait(1000, MSEC)
    reset_odometry()
    
    pid_driver.drive(-150, True)
    pid_turner.turn(20, FRAME_HEADING_RELATIVE)
    pid_driver.drive(160, True)

    wait(1000, MSEC)
    reset_odometry()


init_event_handling()

# register the competition functions
competition = Competition(driver_function, autonomous_function)