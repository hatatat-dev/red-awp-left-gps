#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from lib.log import *
from high_stakes.events import *

open_log("manual.csv")


init_event_handling()
