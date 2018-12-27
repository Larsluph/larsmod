#!usr/bin/env python
# -*- coding:utf-8 -*-

"a module to manage files easily"

import os
	
def prefix_delete(path, prefix):
	"delete same prefix of mass files in one folder"
	
	files = os.listdir(path) # create a list with all the filenames in folder 'path'
	for x in files:
		if x[:len(prefix)] == prefix:
			os.rename(path + "\\" + x, path + "\\" + x[len(prefix) :])

def suffix_delete(path, suffix):
	"delete same suffix of mass files in one folder"
	
	fichiers = os.listdir(path) # create a list with all the filenames in folder 'path'
	for x in fichiers:
		if os.path.splitext(x)[0][len(os.path.splitext(x)[0]) - len(suffix) :] == suffix:
			os.rename(path + "\\" + x, path + "\\" + os.path.splitext(x)[0][: len(os.path.splitext(x)[0]) - len(suffix)] + os.path.splitext(x)[1])
	
def char_delete(path, char):
	"delete filename up to a certain character"
	
	fichiers = os.listdir(path) # create a list with all the filenames in folder 'path'
	for x in fichiers:
		for index in range(len(x)):
			if x[index] == char:
				os.rename(path + "\\" + x, path + "\\" + x[index+1:])
				break
	
def char_nbr_delete(path, char_nbr):
	"delete filename up to a certain number of character"
	
	fichiers = os.listdir(path) # create a list with all the filenames in folder 'path'
	for x in fichiers:
		for index in range(len(x)):
			if index == char_nbr:
				try:
					os.rename(path + "\\" + x, path + "\\" + x[index+1:])
				except FileExistsError:
					print("Le fichier %s existe déjà!\nskipping..." % (x))
				break

''' In progress

def shift_filename_folder(path):
	"shift the first letter of each word in all of the filenames in one folder"
	
	filelist = os.listdir(path) # create a list with all the filenames in folder 'path'
	for file in filelist:
		filename = file.split(" ")
		new_file = list()
		new_filename = str()

		print(filelist, file, filename, new_file, new_filename)

		for word in filename:
			try:
				word = word[0].upper() + word[1:].lower()
			except:
				pass
			new_file.append(word)
		new_filename = " ".join(new_file)
		os.rename(path + "\\" + file, path + "\\" + new_filename)
'''
