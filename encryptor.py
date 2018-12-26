#!usr/bin/env python
# -*- coding:utf-8 -*-
"a module to (de)cypher data"

import time, os, random

class cypher:
	"a class to cypher data"
	
	def alpha(data):
		"cypher alphabet string to integer list (support spaces)"
		
		if not(type(data) == str): # error if data not a string
			raise TypeError("given argument is not a string")
		alphabet = {
			"a" : 1,
			"b" : 2,
			"c" : 3,
			"d" : 4,
			"e" : 5,
			"f" : 6,
			"g" : 7,
			"h" : 8,
			"i" : 9,
			"j" : 10,
			"k" : 11,
			"l" : 12,
			"m" : 13,
			"n" : 14,
			"o" : 15,
			"p" : 16,
			"q" : 17,
			"r" : 18,
			"s" : 19,
			"t" : 20,
			"u" : 21,
			"v" : 22,
			"w" : 23,
			"x" : 24,
			"y" : 25,
			"z" : 26,
			" " : " "
		}
		result = list()
		for letter in data:
			result.append(alphabet[letter])
		return result
		
	def cesar(data, indice):
		"cypher cesar encryption (str to str)"
		
		if not(type(data) == str and type(indice) == int):
			raise TypeError("given arguments are incorrect")
		
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		result = ""
		for letter in data:
			index = 0
			for x in alphabet:
				if x == letter:
					code = index + indice
					while code < 0:
						code += 26
					result += alphabet[code]
				index += 1
		return result
	
class decypher:
	"a class to decypher data"
	
	def alpha(data):
		"decypher integer list to alphabet string (support spaces)"
		
		if not(type(data) == list):
			raise TypeError("argument given is not a list")
		alphabet = {
			1 : "a",
			2 : "b",
			3 : "c",
			4 : "d",
			5 : "e",
			6 : "f",
			7 : "g",
			8 : "h",
			9 : "i",
			10 : "j",
			11 : "k",
			12 : "l",
			13 : "m",
			14 : "n",
			15 : "o",
			16 : "p",
			17 : "q",
			18 : "r",
			19 : "s",
			20 : "t",
			21 : "u",
			22 : "v",
			23 : "w",
			24 : "x",
			25 : "y",
			26 : "z",
			" " : " "
		}
		result = str()
		for digit in data:
			result += alphabet[str(digit)]
		return result
	
	def cesar(data, indice):
		"decypher cesar encryption"
		
			if not(type(data) == str and type(indice) == int):
				raise TypeError("given arguments are incorrect")
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		result = ""
		for letter in data:
			index = 0
			for x in alphabet:
				if x == letter:
					code = index - indice
					while code < 0:
						code += 26
					result += alphabet[code]
				index += 1
		return result
	