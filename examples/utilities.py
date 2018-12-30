#!usr/bin/env python
# -*- coding:utf-8 -*-
"a module w/ useful tools"

from custom_module import utilities as util

randomlistpicker(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
# >>> 'z'
# >>> 'm'
# >>> 'q'
# >>> 'g'
# >>> 'w'

util.menu_generator("MAIN MENU", [], ["input","print","Quit"], ["input()","print('success!')","quit()"])
