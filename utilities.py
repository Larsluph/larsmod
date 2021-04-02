#!usr/bin/env python3
# -*- coding:utf-8 -*-
"a module w/ useful tools"

import os
import random
import secrets
import time
from typing import Any, Iterable, Union, Optional


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
    "enable to loop through values in a list"
    if not(isinstance(entry, list)):
        raise TypeError("argument must be a list")

    entry.insert(len(entry), entry.pop(0))
    return


def dec2base(n: int, base: int) -> str:
    "convert number {n} from base 10 to base {base}"
    result = ""
    if n == 0:
        result = "0"
    while n != 0:
        r = n % base
        result = str(r) + result
        n = n // base
    return result


def base2dec(n: int, base: int) -> int:
    "convert number {n} from base {base} to base 10"
    result = 0
    power = 0
    while n > 0:
        result += base**power*(n % 10)
        n //= 10
        power += 1
    return result


def strfill(string: Any, length: int, fill: str = " ", before: bool = False):
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


def search(iterable: Iterable, substring: Any) -> list:
    result = list()

    for x in iterable:
        if substring in x:
            result.append(x)

    return result


def find_all(iterable: Iterable, x: Any) -> list:
    "find all occurences of {x} in {iterable}"

    result = []

    if isinstance(iterable, str):
        current = iterable.find(x)
        while current != -1:
            result.append(current)
            current = iterable.find(x, current+1)
    else:
        for i, it in enumerate(iterable):
            if x == it:
                result.append(i)

    return result


def chunks(data: Iterable, chunk_size: int, *, callback: Optional=None, reverse: bool=False):
    "split {data} into n-sized chunks"
    if reverse:
        result = list()
        for i in range(len(data), 0, -chunk_size):
            i_min = i-chunk_size if i > chunk_size else 0
            if callable(callback):
                temp = callback(data[i_min:i])
            else:
                temp = data[i_min:i]
            result.append(temp)
        return result[::-1]
    else:
        return [callback(data[i:i+chunk_size]) if callback(callback) else data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]


def password_generator(length: int, chars: Iterable=None):
    """
    returns a randomly-generated password of length {length} containing only {chars} characters.
    If chars is omitted, character used will be all printable ASCII characters
    """
    if chars == None:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    return ''.join(secrets.choice(chars) for _ in range(length))


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
