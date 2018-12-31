#!usr/bin/env python
# -*- coding:utf-8 -*-

"a module to manage files easily"

from custom_module import file_manager as fm


path = "/usr/media/"
"""
 |- roadtrip_picture1_USA.png
 |- roadtrip_picture2_USA.png
 |- roadtrip_picture3_USA.png
 |- roadtrip_picture4_USA.png
 -- roadtrip_picture5_USA.png
"""

fm.prefix_delete(path, "roadtrip_")
"""
/usr/media/
 |- picture1_USA.png
 |- picture2_USA.png
 |- picture3_USA.png
 |- picture4_USA.png
 -- picture5_USA.png
"""
	
fm.suffix_delete(path, "_USA")
"""
/usr/media/
 |- picture1.png
 |- picture2.png
 |- picture3.png
 |- picture4.png
 -- picture5.png
"""

fm.char_delete(path, "i")
"""
/usr/media/
 |- cture1.png
 |- cture2.png
 |- cture3.png
 |- cture4.png
 -- cture5.png
"""

fm.char_nbr_delete(path, 5)
"""
/usr/media/
 |- 1.png
 |- 2.png
 |- 3.png
 |- 4.png
 -- 5.png
"""
