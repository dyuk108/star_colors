# -*- coding: utf-8 -*-
#
# Тестирование функций из star_colors.py с построением цветных шкал.
# Создаёт файл test_colorscale.svg .

from star_colors import *

# Создаём картинку SVG.
width = 800 # ширина
height = 800 # высота
f = open('test_colorscale.svg', 'w')

# заголовок
s = '<svg version="1.1" baseProfile="full" width="' + str(width) + '" height="' +\
str(height) + '" xmlns="http://www.w3.org/2000/svg">\n'

# Рисуем прямоугольник спектральными классов.
sptypes = ('O', 'B', 'A', 'F', 'G', 'K', 'M')
x = 710 # координаты начала рисования
y = 10
for spt in sptypes:
    for sub in range(10):
        spt_s = spt + str(sub) # строка сп. класса
        t = sptype2t(spt_s) # определяем типичную температуру сп. класса
        color = t2rgb(t) # RGB цвет по температуре
        
        s += f'<rect x="{x}" y="{y}" width="10" height="100" stroke="transparent" fill="{color}" stroke-width="0"/>\n'
        if sub % 5 == 0 or spt_s == 'M9':
            s += f'<text x="{x}" y="80" font-size="11">{spt_s}</text>\n'
            s += f'<text x="{x}" y="95" font-size="6">{t}</text>\n'
        x -= 10

# Рисуем прямоугольник с цветовой шкалой температур.
x = 20 # координаты начала рисования
y = 150
for t in range(1000, 19800, 80):
    color = t2rgb(t) # RGB цвет по температуре

    s += f'<rect x="{x}" y="{y}" width="3" height="100" stroke="transparent" fill="{color}" stroke-width="0"/>\n'
    if t % 1000 == 0:
        s += f'<text x="{x}" y="260" font-size="7">{t}</text>\n'
    x += 3


s += '</svg>'
f.write(s)
f.close()