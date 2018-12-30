#!usr/bin/env python
# -*- coding:utf-8 -*-
from custom_module import decryptor as crypt

crypt.cypher.alpha("abcdef")
#  >>> [1, 2, 3, 4, 5, 6]

crypt.cypher.cesar("abcdef", 3)
#  >>> 'defghi'

#########

crypt.decypher.alpha([1, 2, 3, 4, 5, 6])
#  >>> 'abcdef'

crypt.decypher.cesar("defghi", 3)
#  >>> 'abcdef'
