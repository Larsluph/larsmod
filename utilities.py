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
        string = str()
        for letter in word:
            string += letter
        result.append(string)
    
    return result
    
def now():
    time.strftime('%A %d %B %Y')
    time.strftime("%H:%M:%S")
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
    
def menu_generator(title, init, inputs, output):
    "generate a menu w/ inputs & outputs"

    os.system("cls")
    
    if type(title) != str or type(init) != list or ( type(inputs) and type(output) ) != list:
        raise TypeError("arguments provided are incorrects")
    
    for x in init:
        exec(x)
        
    print(title)
    
    for x in range(len(inputs)):
        print(str(x+1) + ".", inputs[x])
        
    try:
        choice = int(input("Enter your choice :\n"))
    except ValueError:
        print("your choice must be an integer")
        os.system("pause")
        os.system("cls")
        menu_generator(title, init, inputs, output)

    if choice < 1 or choice > len(inputs):
        print("this option is out of range")
        os.system("pause")
        os.system("cls")
        menu_generator(title, init, inputs, output)
    
    return output[choice-1]