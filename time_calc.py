#!usr/bin/env python
# -*- coding:utf-8 -*-
####################
import os,sys
####################
def launch(calc):
	# ex: D9_M3_Y2017_h13 + D1
	try:
		x1, signe, x2 = calc.split(" ")
	except ValueError:
		raise InputError("don't forget to put spaces only for ' + ' or ' - '")
		
	seconds = {
	"second" : 1,
	"minute" : 60,
	"hour" : 3600,
	"day" : 86400,
	"month" : 2592000,
	"year" : 31104000
	}
	
	x1 = x1.split("_")
	x2 = x2.split("_")
	
	nbr_s = [0,0]
	for argu in x1:
		if argu[0] == 'Y':
			nbr_s[0] += int(argu[1:]) * seconds['year']
		if argu[0] == 'M':
			nbr_s[0] += int(argu[1:]) * seconds['month']
		if argu[0] == 'D':
			nbr_s[0] += int(argu[1:]) * seconds['day']
		if argu[0] == 'h':
			nbr_s[0] += int(argu[1:]) * seconds['hour']
		if argu[0] == 'm':
			nbr_s[0] += int(argu[1:]) * seconds['minute']
		if argu[0] == 's':
			nbr_s[0] += int(argu[1:]) * seconds['second']
	for argu in x2:
		if argu[0] == 'Y':
			nbr_s[1] += int(argu[1:]) * seconds['year']
		if argu[0] == 'M':
			nbr_s[1] += int(argu[1:]) * seconds['month']
		if argu[0] == 'D':
			nbr_s[1] += int(argu[1:]) * seconds['day']
		if argu[0] == 'h':
			nbr_s[1] += int(argu[1:]) * seconds['hour']
		if argu[0] == 'm':
			nbr_s[1] += int(argu[1:]) * seconds['minute']
		if argu[0] == 's':
			nbr_s[1] += int(argu[1:]) * seconds['second']
	print(x1,x2,nbr_s)