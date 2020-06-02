#!usr/bin/env python
# -*- coding:utf-8 -*-
"basic python chronometer (support laps)"

import os
import time
from collections import namedtuple


class Chrono:
  "stores the start and stop time to compute the time passed between these two"
  time_tuple = namedtuple("chrono_time", "days, hours, minutes, seconds, ms")

  def start(self) -> None:
    "start/reset the chronometer"
    self._begin = time.perf_counter() # stores the begin time
    return None

  def lap(self) -> time_tuple:
    "return a lap"

    lap = time.perf_counter() - self._begin # compute time delta in seconds

    # compute all time units from lap
    ms = round(lap%1 * 1000)
    seconds = round(lap)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return self.time_tuple(days, hours, minutes, seconds, ms) # return a named tuple
