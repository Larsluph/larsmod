#!usr/bin/env python
# -*- coding:utf-8 -*-

import custom_module

custom_module.decryptor.cypher_alpha("abcdef")
#  >>> [1, 2, 3, 4, 5, 6]

custom_module.decryptor.decypher_alpha([1, 2, 3, 4, 5, 6])
#  >>> 'abcdef'

#########

custom_module.decryptor.cypher_cesar("abcdef", 3)
#  >>> 'defghi'

custom_module.decryptor.decypher_cesar("defghi", 3)
#  >>> 'abcdef'

#########

custom_module.decryptor.cypher_morse("sos")
# >>> ['...', '---', '...']

custom_module.decryptor.cypher_morse('... --- ...'.split(" ")] )
# >>> 'sos'