Intro
Hi there! Here is where you can find explanations on how to use this module perfectly!
WARNING - This module is written for Windows in Python3.8. Some things could not work properly.

Chronometer
This chronometer is pretty simple.
You can start it with Chrono.start() and stop it with Chrono.stop()
It will return a list of 3 float corresponding to the chronometer's result : [hours, minutes, seconds]

Decryptor
The decryptor (as said by his own name) can encrypt and decrypt simple cypher algorithms.
For now, there are 4 algorithms :
  alpha - It converts a string into a digit list and vice versa.
  cesar - The cesar algorithm takes a string and shifts all characters to a certain position.
  morse - It enables to translate morse code into letters and vice versa.
  Numpad - ONLY ABLE TO CYPHER - convert a text string to a digit string.

File Manager
The File Manager is used to manage files (thanks Captain Obvious).
  You can remove the prefix or the suffix of multiple files in a given folder (sub-folders excluded) with the functions prefix_delete(path, prefix) and suffix_delete(path, suffix).
  You can also remove the beginning of filenames with char_delete(path, char) that remove filenames up to the first occurrence of "char" (included) and char_nbr_delete(path, char_nbr) that remove filenames up to a certain "char_nbr".

Utilities
The utilities module is composed of some miscellaneous useful functions.
  randomlistpicker(usrlist) return a random entry in the 'usrlist'.
  letter_randomizer(words) take all characters in a string (single word / sentence) or in a list of words and randomize them to return an "anagram"
  now() return a list with [day name, day number, month name, year, hour, minute, second]
  menu_generator(title, init, inputs, output) display a generated menu with a title, inputs and outputs.
  math_calc.launch() enables to launch a python calculator console (works in radians)

Errors
  TypeError - a function may return this error because an arguments' type isn't correct
  FileExistsError - a function in the file_manager may return this error because the modified file had the same name as an existing file
  InputError - a function may return this error because an argument isn't correctly formatted
