#!usr/bin/env python
# -*- coding:utf-8 -*-
"chronometer w/ laps (for laps just enter stop() other times)"

import os

def start():
	"start Chronometer"
	
	global begin
	begin = [
		int(time.strftime("%H")),
		int(time.strftime("%M")),
		int(time.strftime("%S"))
	]
	print("Le chrono a commencé à",begin[0],"heures",begin[1],"minutes et",begin[2],"secondes.")
	
def stop():
	"stop Chronometer"
	
	global begin
	global end
	end = [
		int(time.strftime("%H")),
		int(time.strftime("%M")),
		int(time.strftime("%S"))
	]
	chrono = [end[0]-begin[0],end[1]-begin[1],end[2]-begin[2]]
	while chrono[2] < 0:
		chrono[2] += 60
		chrono[1] -= 1
	while chrono[1] < 0:
		chrono[1] -= 60
		chrono[0] += 1
	print("Le chrono s'est fini à",end[0],"heures",end[1],"minutes et",end[2],"secondes.")
	print("Le chrono indique",chrono[0],"heures",chrono[1],"minutes et",chrono[2],"secondes.")
	os.system("pause")
	