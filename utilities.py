#!usr/bin/env python3
# -*- coding:utf-8 -*-
"a module w/ useful tools"

import os
import random
import secrets
import time
from typing import Any, Sequence, Union, Optional, List, Dict


def letter_randomizer(words: Union[str, list]) -> list:
    """
    Take all characters in a string (separate words by a space) and randomize them to return an "anagram"
    """

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

    for word in final:
        string = "".join(word)
        for letter in word:
            string += letter
        result.append(string)

    return result


def list_cycle(entry: list) -> None:
    """
    Enable to loop through values in a list
    """
    if not(isinstance(entry, list)):
        raise TypeError("argument must be a list")

    entry.insert(len(entry), entry.pop(0))
    return


def dec2base(n: int, base: int) -> str:
    """
    Convert number {n} from base 10 to base {base}
    """
    result = ""
    if n == 0:
        result = "0"
    while n != 0:
        r = n % base
        result = str(r) + result
        n = n // base
    return result


def base2dec(n: int, base: int) -> int:
    """
    Convert number {n} from base {base} to base 10
    """
    result = 0
    power = 0
    while n > 0:
        result += base**power*(n % 10)
        n //= 10
        power += 1
    return result


def strfill(string: Any, length: int, fill: str = " ", before: bool = False):
    """
    same as str.zfill but more customizable
    """
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


def search(iterable: Sequence, substring: Any) -> list:
    """
    Returns every entry in {Sequence} that contains {substring}
    """
    result = list()

    for x in iterable:
        if substring in x:
            result.append(x)

    return result


def find_all(iterable: Sequence, x: Any) -> list:
    """
    Find all occurences of {x} in {Sequence}
    """

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


def chunks(data: Sequence, chunk_size: int, *, callback: Optional = None, reverse: bool = False):
    """
    Split {data} into n-sized chunks
    """
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
        return [callback(data[i:i+chunk_size])
                if callback(callback)
                else data[i:i+chunk_size]
                for i in range(0, len(data), chunk_size)]


def password_generator(length: int, chars: List = None):
    """
    returns a randomly-generated password of length {length} containing only {chars} characters.
    If chars is omitted, character used will be all printable ASCII characters
    """
    if chars is None:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    return ''.join(secrets.choice(chars) for _ in range(length))


def menu_generator(title: str, inputs: Sequence, output: Optional[Sequence] = None, hidden: Optional[Dict]=None) -> "choice in output":
    """
    Generate a menu w/ inputs & outputs
    """
    if hidden is None:
        hidden = {}

    if not(isinstance(title, str) and isinstance(inputs, list) and isinstance(output, (list, type(None)))):
        raise TypeError("arguments provided are incorrects")

    errors = ["launch loop"]
    while errors:
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

    return inputs[choice-1] if output is None else output[choice-1]


def draw_table(header: list[str], lines: list[list[str]]):
    lines = [header] + lines
    column_size = [0 for i in range(len(header))]
    for line in lines:
        for i, cell in enumerate(line):
            column_size[i] = max(column_size[i], len(cell))

    for i in range(1 + len(lines) * 2):
        if i % 2 == 0:
            print("+", end="")
            for size in column_size:
                print("-" * (size + 1) + "-+", end="")
            print()
        else:
            print("|", end="")
            for data, size in zip(lines[i // 2], column_size):
                print(" " + data.center(size) + " |", end="")
            print()


def clrscr():
    from os import name, system
    system('cls' if name == 'nt' else 'clear')
