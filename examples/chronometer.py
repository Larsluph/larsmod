#!usr/bin/env python
# -*- coding:utf-8 -*-
from custom_module import chronometer as chrono
import time

chrono_start = chrono.start()
# >>> [17,50,42]

time.sleep(5)

chrono_end = chrono.stop(chrono_start)
# >>> ( [17,50,47] , [0,0,5] )
