#!usr/bin/env python
# -*- coding:utf-8 -*-

"a module to manage files easily"

import os
	
def prefix_delete(path, prefix):
	"delete same prefix of mass files in one folder"
	
	files = os.listdir(path) # create a list with all the filenames in folder 'path'
	
	for current in files:
		if current[:len(prefix)] == prefix:
			try:
				os.rename(path + "\\" + current, path + "\\" + current[len(prefix) :])
			except FileExistsError:
				raise ("Unable to rename file '{}' because the file already exists. skipping...".format(current) )
			break

def suffix_delete(path, suffix):
	"delete same suffix of mass files in one folder"
	
	files = os.listdir(path) # create a list with all the filenames in folder 'path'
	
	for current in files:
		if os.path.splitext(current)[0][len(os.path.splitext(current)[0]) - len(suffix) :] == suffix:
			try:
				os.rename(path + "\\" + current, path + "\\" + os.path.splitext(current)[0][: len(os.path.splitext(current)[0]) - len(suffix)] + os.path.splitext(current)[1])
			except FileExistsError:
				raise ("Unable to rename file '{}' because the file already exists. skipping...".format(current) )
			break
	
def char_delete(path, char):
	"delete filename up to a certain character"
	
	files = os.listdir(path) # create a list with all the filenames in folder 'path'
	
	for current in files:
		for index in range(len(current)):
			if x[index] == char:
				try:
					os.rename(path + "\\" + current, path + "\\" + current[index+1:])
				except FileExistsError:
					raise ("Unable to rename file '{}' because the file already exists. skipping...".format(current) )
				break
	
def char_nbr_delete(path, char_nbr):
	"delete filename up to a certain number of character"
	
	files = os.listdir(path) # create a list with all the filenames in folder 'path'
	
	for current in files:
		try:
			os.rename(path + "\\" + current, path + "\\" + current[char_nbr:])
		except FileExistsError:
			raise ("Unable to rename file '{}' because the file already exists. skipping...".format(current) )
		break
