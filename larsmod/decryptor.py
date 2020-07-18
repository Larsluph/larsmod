#!usr/bin/env python
# -*- coding:utf-8 -*-
"a module to (de)cypher data"

import os
import random
import time
import string


def cypher_alpha(data: str) -> list:
    if not(isinstance(data, str)):
        raise TypeError("given argument is not a string")

    alpha = string.ascii_lowercase
    alphabet = dict(alpha, range(1, len(alpha)+1))
    result = list()
    for letter in data:
        if letter not in alpha:
            result.append(letter)
        else:
            result.append(alphabet[letter])
    return result


def cypher_cesar(data: str, indice: int) -> str:
    if not(isinstance(data, str) and isinstance(indice, int)):
        raise TypeError("given arguments are incorrect")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in data:
        try:
            index = alphabet.index(letter.lower())
            code = (index + indice) % 26
            result += alphabet[code]
        except:
            result += letter
    return result


def cypher_morse(data: str) -> list:
    if not(isinstance(data, str)):
        raise TypeError("given argument is not a string")

    alphabet = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ' ': ' / '
    }
    result = list()
    for char in data.lower():
        result.append(alphabet[char])

    return result


def cypher_numpad(data: str) -> str:
    if not(isinstance(data, str)):
        raise TypeError("given argument is not a string")

    data = data.lower()
    indice = 0
    final = str()
    while indice != len(data):
        if data[indice] == "a" or data[indice] == "b" or data[indice] == "c":
            final += "2"
        elif data[indice] == "d" or data[indice] == "e" or data[indice] == "f":
            final += "3"
        elif data[indice] == "g" or data[indice] == "h" or data[indice] == "i":
            final += "4"
        elif data[indice] == "j" or data[indice] == "k" or data[indice] == "l":
            final += "5"
        elif data[indice] == "m" or data[indice] == "n" or data[indice] == "o":
            final += "6"
        elif data[indice] == "p" or data[indice] == "q" or data[indice] == "r" or data[indice] == "s":
            final += "7"
        elif data[indice] == "t" or data[indice] == "u" or data[indice] == "v":
            final += "8"
        elif data[indice] == "w" or data[indice] == "x" or data[indice] == "y" or data[indice] == "z":
            final += "9"
        elif data[indice] == " ":
            final += "0"
        else:
            try:
                final += int(data[indice])
            except:
                final += "1"
        indice += 1
    return final


def decypher_alpha(data: list) -> str:
    if not(isinstance(data, list)):
        raise TypeError("given argument is not a list")
    alpha = string.ascii_lowercase
    alphabet = dict(range(1, len(alpha)+1), alpha)
    result = str()
    for digit in data:
        if digit in data:
            result += alphabet[digit]
        else:
            result += digit
    return result


def decypher_cesar(data: str, indice: int) -> str:
    if not(isinstance(data, str) and isinstance(indice, int)):
        raise TypeError("given arguments are incorrect")

    alphabet = string.ascii_lowercase
    result = ""
    for letter in data:
        if letter in alphabet:
            index = alphabet.index(letter.lower())
            code = (index - indice) % 26
            result += alphabet[code]
        else:
            result += letter
    return result


def decypher_morse(data: list) -> str:
    if not(isinstance(data, list)):
        raise TypeError("given argument is not a list")
    alphabet = {
        '.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..': 'd',
        '.': 'e',
        '..-.': 'f',
        '--.': 'g',
        '....': 'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '/': ' '
    }
    result = str()
    for char in data:
        result += alphabet[char]

    return result
