# -*- coding: utf-8 -*-
#
# Тестирование функции определения Teff по сп. классу.
# Использует функции из star_colors.py

from star_colors import sptype2t

sptypes = ('O', 'B', 'A', 'F', 'G', 'K', 'M')

for spt in sptypes:
    for sub in range(10):
        spt_s = spt + str(sub) # строка сп. класса
        print(spt_s, sptype2t(spt_s))