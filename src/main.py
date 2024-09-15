#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from lib.log import *
from high_stakes.events import *

open_log("red-awp-left.csv")

def driver_function():
    pass

def autonomous_function():
    intake_1st_stage.set_velocity(525, RPM)
    intake_2nd_stage.set_velocity(525, RPM)
    pid_driver.drive(-1000, True)
    clamp.set(True)
    pid_turner.turn(85, FRAME_HEADING_RELATIVE)
    intake_1st_stage.spin(REVERSE)
    intake_2nd_stage.spin(FORWARD)
    pid_driver.drive(700, True)
    pid_turner.turn(90, FRAME_HEADING_RELATIVE)
    pid_driver.drive(400, True)
    wait(100, MSEC)
    pid_driver.drive(-150, True)
    pid_turner.turn(15, FRAME_HEADING_RELATIVE)
    pid_driver.drive(150, True)


init_event_handling()

# register the competition functions
competition = Competition(driver_function, autonomous_function)