#!usr/bin/env python
# -*- coding:utf-8 -*-
"a module w/ useful tools"

import time, os, random

def randomlistpicker(usrlist):
	"Pick a random entry in given list"
	
	if type(usrlist) != list:
		raise TypeError("argument provided is not a list")
		
	return(usrlist[random.randint(0,len(usrlist)-1)])
	
def menu_generator(title, init, inputs, output):
	"generate a menu w/ inputs & outputs"

	os.system("cls")
	
	if type(title) != str or type(init) != list or ( type(inputs) and type(output) ) != list:
		raise TypeError("arguments provided are incorrects")
	
	indice = 0
	
	for x in init:
		exec(str(init[indice]))
		indice += 1
		
	print(title)
	
	indice = 0
	for x in inputs:
		indice += 1
		print(str(indice) + ".", x)
		
	try:
		choice = int(input("Enter your choice :\n"))
	except ValueError:
		print("your choice must be an integer")
		os.system("pause")
		os.system("cls")
		menu_generator(title, init, inputs, output)
	
	for n in range(0, len(inputs)):
		if choice == n + 1:
			exec(output[n])
			
	if choice < 1 or choice > len(inputs):
		print("this option isn't in the menu")
		os.system("pause")
		os.system("cls")
		menu_generator(title, init, inputs, output)
