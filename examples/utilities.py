#!usr/bin/env python
# -*- coding:utf-8 -*-
"a module w/ useful tools"

from custom_module import utilities as util
import string

util.randomlistpicker(list(string.ascii_lowercase))
# >>> 'z'
# >>> 'm'
# >>> 'q'
# >>> 'g'
# >>> 'w'

util.letter_randomizer("this is a sentence")
# >>> ['isht', 'is', 'a', 'eecensnt']

custom_module.calculator.launch()
# >>> Enter calculation...

util.menu_generator("MAIN MENU", [], ["input","print","Quit"], ["input()","print('success!')","quit()"])
