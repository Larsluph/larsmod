#!usr/bin/env python
# -*- coding:utf-8 -*-
"chronometer w/ laps"

import os

def start():
	"return the system's time (needed to stop the chrono)"
	begin = [
		int(time.strftime("%H")), # fetch system's hour
		int(time.strftime("%M")), # .............. minutes
		int(time.strftime("%S"))  # .............. seconds
	]
	return begin
	
def stop(begin):
	"return a lap"
	
	end = [
		int(time.strftime("%H")), # fetch system's hour
		int(time.strftime("%M")), # .............. minutes
		int(time.strftime("%S"))  # .............. seconds
	]
	chrono = [ # calculating the time difference between begin and end
		end[0] - begin[0],
		end[1] - begin[1],
		end[2] - begin[2]
	]
	while chrono[2] < 0: # time can't be negative so reformating
		chrono[2] += 60
		chrono[1] -= 1
	while chrono[1] < 0:
		chrono[1] -= 60
		chrono[0] += 1
	return end, chrono
	
