#!usr/bin/env python3
# -*- coding:utf-8 -*-
"a module w/ useful tools"

import os
import random
import time
from typing import Iterable, Union


def letter_randomizer(words: Union[str, list]) -> list:
    'take all characters in a string (separate words by a space) and randomize them to return an "anagram"'

    if not(isinstance(words, (str, list))):
        raise TypeError(
            "argument must be a string (sentence or single word) or a list of words (order will be kept)")

    if type(words) == str:
        words = words.split(" ")

    result = list()

    for word in words:
        result.append(list(word))

    for word in result:
        random.shuffle(word)

    final = result.copy()
    result = list()
    string = str()

    for word in final:
        string = "".join(word)
        for letter in word:
            string += letter
        result.append(string)

    return result


def list_cycle(entry: list) -> None:
    "enable to loop through multiple custom values in a list"
    if not(isinstance(entry, list)):
        raise TypeError("argument must be a list")

    entry.insert(len(entry), entry.pop(0))
    return


def now() -> list:
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


def dec2base(n: int, base: int) -> str:
    result = ""
    if n == 0:
        result = "0"
    while n != 0:
        r = n % base
        result = str(r) + result
        n = n // base
    return result


def base2dec(n: int, base: int) -> int:
    result = 0
    power = 0
    while n > 0:
        result += base**power*(n % 10)
        n //= 10
        power += 1
    return result


def strfill(string: str, length: int, fill: str = " ", before: bool = False):
    "same as zfill but more customizable"
    sub = str()
    if not(isinstance(string, str)):
        string = repr(string)
    assert isinstance(string, str)
    length = length - len(string)

    i = 0
    while len(sub) < length:
        sub += fill[i % len(fill)]
        i += 1

    if before:
        string = sub + string
    else:
        string = string + sub

    return string


def search(iterable: Iterable, substring: str) -> list:
    result = list()

    for x in iterable:
        if substring in x:
            result.append(x)

    return result


def find_all(string: Union[str, bytes], substring: Union[str, bytes]) -> list:
    "find all occurences of {substring} in {string}"
    result = []
    current = string.find(substring)
    while current != -1:
        result.append(current)
        current = string.find(substring, current+1)

    return result


def password_generator(length: int, chars: Iterable = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
    "returns a randomly-generated password of length {length} containing only {chars} characters"
    gen = str()
    for _ in range(length):
        gen += chars[random.randint(0, len(chars)-1)]
    return gen


def menu_generator(title: str, inputs: list, output: list, hidden: dict = {}) -> "choice in output":
    "generate a menu w/ inputs & outputs"
    if not(isinstance(title, str) and isinstance(inputs, list) and isinstance(output, list)):
        raise TypeError("arguments provided are incorrects")

    errors = ["launch loop"]
    while errors != []:
        errors = []
        os.system("cls")

        print(title.upper())

        for x in range(len(inputs)):
            print(str(x+1) + ".", inputs[x])

        choice = input("\nEnter your choice :\n")

        try:
            choice = int(choice)
        except ValueError:
            if choice in hidden:
                return hidden[choice]
            else:
                print("your choice must be an integer")
                os.system("pause")
                errors.append("not int")
                continue

        if choice in hidden:
            return hidden[choice]
        elif choice < 1 or choice > len(inputs):
            print("this option is out of range")
            os.system("pause")
            errors.append("OOB")
            continue

    return output[choice-1]
