#!usr/bin/env python
# -*- coding:utf-8 -*-

"a module to manage files easily"

import os

def prefix_delete(path: str, prefix: str) -> None:
  "delete same prefix of mass files in one folder"

  if not( isinstance(path,str) and isinstance(prefix,str) ):
    raise TypeError("arguments' types are not valid")

  files = os.listdir(path) # create a list with all the filenames in folder 'path'

  for current in files:
    if current[:len(prefix)] == prefix:
      try:
        os.rename(path + "\\" + current, path + "\\" + current[len(prefix) :])
      except FileExistsError:
        print(f"Unable to rename file '{current}' because the file already exists. skipping...")

  return

def suffix_delete(path: str, suffix: str) -> None:
  "delete same suffix of mass files in one folder"

  if not( isinstance(path,str) and isinstance(suffix,str) ):
    raise TypeError("arguments' types are not valid")

  files = os.listdir(path) # create a list with all the filenames in folder 'path'

  for current in files:
    if os.path.splitext(current)[0][len(os.path.splitext(current)[0]) - len(suffix) :] == suffix:
      try:
        os.rename(path + "\\" + current, path + "\\" + os.path.splitext(current)[0][: len(os.path.splitext(current)[0]) - len(suffix)] + os.path.splitext(current)[1])
      except FileExistsError:
        print(f"Unable to rename file '{current}' because the file already exists. skipping...")

  return

def char_delete(path: str, substring: str) -> None:
  "delete filename up to a certain substring"

  if not( isinstance(path,str) and isinstance(substring,str) ):
    raise TypeError("arguments' types are not valid")

  files = os.listdir(path) # create a list with all the filenames in folder 'path'

  for current in files:            # for each file in the folder
    if char in current:            #   only check those with the char in the filename
      index = current.index(char)  #   if the char is in it then get the index of the first occurence
      try:                         #     and try to rename it
        os.rename(path + "\\" + current, path + "\\" + current[index+len(substring):])
      except FileExistsError:
        print(f"Unable to rename file '{current}' because the file already exists. skipping...")

  return

def char_nbr_delete(path: str, char_nbr: int) -> None:
  "delete filename up to a certain number of character"

  if not( isinstance(path,str) and isinstance(char_nbr,int) ):
    raise TypeError("arguments' types are not valid")

  files = os.listdir(path) # create a list with all the filenames in folder 'path'

  for current in files:
    try:
      os.rename(path + "\\" + current, path + "\\" + current[char_nbr:])
    except FileExistsError:
      print(f"Unable to rename file '{current}' because the file already exists. skipping...")

  return

def search(path: str,keyword: str,subfolder: bool =False) -> list:
  "serach for {keyword} in the folder {path}"

  if not( isinstance(path,str) and isinstance(keyword,str) and isinstance(subfolder,bool) ):
    raise TypeError("arguments' types are not valid")

  files = os.listdir(path)
  search_results = []

  if subfolder:
    raise NotImplementedError

  else:
    for filename in files:
      if keyword in filename:
        search_results.append(f"{path}\\{filename}")

    return search_results
