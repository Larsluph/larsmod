#!usr/bin/env python
# -*- coding:utf-8 -*-

"a module to manage files easily"

import os
import zipfile

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

def search(path: str, keyword: str, subfolder: bool = False) -> list:
  "serach for {keyword} in the folder {path}"

  if not( isinstance(path,str) and isinstance(keyword,str) and isinstance(subfolder,bool) ):
    raise TypeError("arguments' types are not valid")

  search_results = []

  if subfolder:
    raise NotImplementedError
    # files = list_tree_path(path)

  else:
    files = os.listdir(path)

  for filename in files:
    if keyword in filename:
      search_results.append(f"{path}\\{filename}")

    return search_results

def copy(source_path: str, target_path: str, replace: bool = False) -> None:
  if not(isinstance(source_path,str) and isinstance(target_path,str)):
    raise TypeError("arguments' types are not valid")

  if not os.path.exists(source_path):
    raise FileNotFoundError()

  if os.path.exists(target_path):
    if replace:
      pass
    else:
      raise FileExistsError("set replace to True if you want to replace")
  else:
    os.system(f"mkdir {os.path.dirname(target_path)}")

  source_file = open(source_path,mode='rb')
  target_file = open(target_path,mode='wb')

  size = divmod(os.path.getsize(source_file),1024)

  for i in range(size[0]):
    target_file.write(source_file.read(i*1024))
  else:
    target_file.write(source_file.read(size[1]))

  source_file.close()
  target_file.close()
  return

def delete(source_path: str) -> None:
  with open(source_path,mode='w'):
    pass
  os.remove(source_path)
  return

def move(source_path: str, target_path: str) -> None:
  copy(source_path,target_path)
  delete(source_path)
  return

def zip_files(files: list, target_path: str) -> None:
  with zipfile.ZipFile(target_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file:
    for file in files:
      zip_file.write(file)

  return

def unzip_file(zip_path: str, target_path: str) -> "list with extracted files":
  with zipfile.ZipFile(zip_path, mode='r') as zip_file:
    zip_file.extractall(target_path)

  return zip_file.namelist()
