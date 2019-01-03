#!usr/bin/env python
# -*- coding:utf-8 -*-

import custom_module

custom_module.decryptor.cypher.alpha("abcdef")
#  >>> [1, 2, 3, 4, 5, 6]

custom_module.decryptor.decypher.alpha([1, 2, 3, 4, 5, 6])
#  >>> 'abcdef'

#########

custom_module.decryptor.cypher.cesar("abcdef", 3)
#  >>> 'defghi'

custom_module.decryptor.decypher.cesar("defghi", 3)
#  >>> 'abcdef'

#########

custom_module.decryptor.cypher.morse("sos")
# >>> ['...', '---', '...']

custom_module.decryptor.cypher.morse('... --- ...'.split(" ")] )
# >>> 'sos'