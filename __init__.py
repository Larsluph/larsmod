#!usr/bin/env python
# -*- coding:utf-8 -*-
"a package by Larsluph w/ useful modules"

import os

from . import (chronometer, decryptor, file_manager, math_calc, networking,
               utilities)

if os.name == "nt":
  from . import notifications_nt as notifications
elif os.name == "posix":
  raise NotImplementedError
