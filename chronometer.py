#!usr/bin/env python
# -*- coding:utf-8 -*-
"basic python chronometer (support laps)"

import os
import time


class Chrono:
  def start(self):
    "start the chronometer"
    self.begin = time.perf_counter()

  def stop(self):
    "return a lap"

    lap = time.perf_counter() - self.begin

    hours = round(lap // 3600)
    lap = lap % 3600

    minutes = round(lap // 60)
    lap = lap % 60

    seconds = round(lap // 1)
    ms = round(lap%1*1000)

    return [hours, minutes, seconds,ms]
