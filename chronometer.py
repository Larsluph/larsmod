#!usr/bin/env python
# -*- coding:utf-8 -*-
"basic python chronometer (support laps)"

import os,time

class Chrono:
    def start(self):
        "start the chronometer"
        self.begin = time.perf_counter()

    def stop(self):
        "return a lap"

        lap = time.perf_counter() - self.begin

        hours = lap // 3600
        lap = lap % 3600

        minutes = lap // 60
        seconds = lap % 60

        return [hours, minutes, seconds]