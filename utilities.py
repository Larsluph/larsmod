#!usr/bin/env python
# -*- coding:utf-8 -*-
"a module w/ useful tools"

import time, os, random

def randomlistpicker(usrlist):
	"Pick a random entry in given list"
	
	if type(usrlist) != list:
		print("argument provided is not a list")
	return(usrlist[random.randint(0,len(usrlist)-1)])
	
def menu_generator(title, init, entree, sortie):
	"generate a menu w/ input & output"
	
	os.system("clear")
	indice = 0
	for x in init:
		exec(init[indice])
		indice += 1
	print(title)
	indice = 0
	for x in entree:
		indice += 1
		print(str(indice) + ".", x)
	choix = int(input("Entrez votre choix :\n"))
	for n in range(0, len(entree)):
		if choix == n + 1:
			exec(sortie[n])
	print("BAD INPUT")
	os.system("pause")
	os.system("cls")
	menu_generator(title, init, entree, sortie)