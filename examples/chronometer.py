#!usr/bin/env python
# -*- coding:utf-8 -*-
from custom_module import chronometer as chrono
import time

timemeter = chrono.Chrono()
timemeter.start()
# start chronometer

time.sleep(5)

timemeter.stop()
# >>> [0,0,5]
