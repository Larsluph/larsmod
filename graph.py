#!usr/bin/env python
# -*- coding:utf-8 -*-
"graph module w/ ONLY console"

import os

def text(colonne,ligne,texte):
	"Display text at a given row, line"
	
	ligne = int(ligne)
	colonne = int(colonne)
	texte = str(texte)
	affichage = ""
	for n in range(ligne):
		affichage += "\n"
	for n in range(colonne):
		affichage += " "
	affichage += texte
	os.system("cls")
	print(affichage)
	input()
