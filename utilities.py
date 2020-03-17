#!usr/bin/env python
# -*- coding:utf-8 -*-
"a module w/ useful tools"

import random, os, time

def randomlistpicker(usrlist):
  "Pick a random entry in given list"

  if type(usrlist) != list:
    raise TypeError("argument provided is not a list")

  return(usrlist[random.randint(0,len(usrlist)-1)])

def letter_randomizer(words):
  'take all characters in a string (separate words by a space) and randomize them to return an "anagram"'

  if not(type(words) == str or type(words) == list):
    raise TypeError("argument must be a string (sentence or single word) or a list of words (order will be kept)")

  if type(words) == str:
    words = words.split(" ")

  result = list()

  for word in words:
    result.append(list(word))

  for word in result:
    random.shuffle(word)

  final = result
  result = list()
  string = str()

  for word in final:
    string = "".join(word)
    for letter in word:
      string += letter
    result.append(string)

  return result

def list_cycle(entry):
  "enable to loop through multiple custom values in a list"
  if type(entry) != list:
    raise TypeError("argument must be a list")

  entry.insert(len(entry),entry.pop(0))
  return 0

def now():
  # time.strftime('%A %d %B %Y')
  # time.strftime("%H:%M:%S")
  final = [
    time.strftime('%A'),
    time.strftime('%d'),
    time.strftime('%B'),
    time.strftime('%Y'),
    time.strftime("%H"),
    time.strftime("%M"),
    time.strftime("%S")
  ]
  return final

def dec2base(n,base):
  result = ""
  if n == 0:
    result = "0"
  while n != 0:
    r = n % base
    result = str(r) + result
    n = n // base
  return result

def base2dec(n,base):
  result = 0
  power = 0
  while n > 0:
    result += base**power*(n%10)
    n //= 10
    power += 1
  return result

def find_all(string,substring):
  result = set()
  current = string.find(substring)
  while current != -1:
    result.add(current)
    current = string.find(substring,current+1)

  return result

def menu_generator(title, inputs, output, hidden={}):
  "generate a menu w/ inputs & outputs"
  if type(title) != str or ( type(inputs) and type(output) ) != list:
    raise TypeError("arguments provided are incorrects")

  errors = ["launch loop"]
  while errors != []:
    errors = []
    os.system("cls")

    print(title.upper())

    for x in range(len(inputs)):
      print(str(x+1) + ".", inputs[x])

    choice = input("Enter your choice :\n")

    try:
      choice = int(choice)
    except ValueError:
      if choice in hidden:
        return hidden[choice]
      else:
        print("your choice must be an integer")
        os.system("pause")
        errors.append("not int")

    if choice in hidden:
      return hidden[choice]
    elif choice < 1 or choice > len(inputs):
      print("this option is out of range")
      os.system("pause")
      errors.append("OOB")

  return output[choice-1]
