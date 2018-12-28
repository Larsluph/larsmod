#!usr/bin/env python
# -*- coding:utf-8 -*-

"a module to manage files easily"

import os
	
def prefix_delete(path, prefix):
	"delete same prefix of mass files in one folder"
	
	files = os.listdir(path) # create a list with all the filenames in folder 'path'
	for current in files:
		if current[:len(prefix)] == prefix:
			os.rename(path + "\\" + current, path + "\\" + current[len(prefix) :])

def suffix_delete(path, suffix):
	"delete same suffix of mass files in one folder"
	
	files = os.listdir(path) # create a list with all the filenames in folder 'path'
	for current in files:
		if os.path.splitext(current)[0][len(os.path.splitext(current)[0]) - len(suffix) :] == suffix:
			os.rename(path + "\\" + current, path + "\\" + os.path.splitext(current)[0][: len(os.path.splitext(current)[0]) - len(suffix)] + os.path.splitext(current)[1])
	
def char_delete(path, char):
	"delete filename up to a certain character"
	
	files = os.listdir(path) # create a list with all the filenames in folder 'path'
	for current in files:
		for index in range(len(current)):
			if x[index] == char:
				os.rename(path + "\\" + current, path + "\\" + current[index+1:])
				break
	
def char_nbr_delete(path, char_nbr):
	"delete filename up to a certain number of character"
	
	files = os.listdir(path) # create a list with all the filenames in folder 'path'
	for current in files:
		for index in range(len(current)):
			if index == char_nbr:
				try:
					os.rename(path + "\\" + current, path + "\\" + current[index+1:])
				except FileExistsError:
					raise ("Unable to rename file '{}' because the file already exists. skipping...".format(current) )
				break
