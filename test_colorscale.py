# -*- coding: utf-8 -*-
#
# Тестирование функций из star_colors.py с построением цветных шкал.
# Создаёт файл test_colorscale.svg .

from star_colors import *
from PIL import Image, ImageDraw, ImageFont

# Создаём картинку PNG.
width = 800 # ширина
height = 600 # высота
img = Image.new('RGB', (width, height), 'white')
idraw = ImageDraw.Draw(img)

# Рисуем прямоугольник спектральными классов.
sptypes = ('O', 'B', 'A', 'F', 'G', 'K', 'M')
x = 750 # координаты начала рисования
y = 30

# get a font
fnt1 = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 12)
fnt2 = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 10)
idraw.multiline_text((330, 5), 'Спектральные классы', font=fnt1, fill=(0, 0, 0))

for spt in sptypes:
    for sub in range(10):
        spt_s = spt + str(sub) # строка сп. класса
        t = sptype2t(spt_s) # определяем типичную температуру сп. класса
        color = t2rgb(t) # RGB цвет по температуре
        
        idraw.rectangle((x-10, y, x, y+100), fill=color)
        if sub % 10 == 0:
            idraw.line([(x-5, y+100), (x-5, y+105)], fill=128)
        if sub % 5 == 0 or spt_s == 'M9':
            idraw.multiline_text((x-10, y+115), spt_s, font=fnt1, fill=(0, 0, 0))
            idraw.multiline_text((x-13, y+128), str(t), font=fnt2, fill=(0, 0, 0))
        x -= 10

# Рисуем прямоугольник с цветовой шкалой температур.
idraw.multiline_text((300, 200), 'Эффективная температура', font=fnt1, fill=(0, 0, 0))
x = 20 # координаты начала рисования
y = 220
for t in range(1000, 20000, 25):
    color = t2rgb(t) # RGB цвет по температуре

    idraw.rectangle((x, y, x+1, y+100), fill=color)
    if t % 1000 == 0:
        idraw.line([(x, y+100), (x, y+105)], fill=128)
        idraw.multiline_text((x-10, y+115), str(t), font=fnt2, fill=(0, 0, 0))
    x += 1

# Рисуем прямоугольник с цветовой шкалой показателя B-V.
idraw.multiline_text((300, 400), 'Показатель B-V', font=fnt1, fill=(0, 0, 0))
x = 20 # координаты начала рисования
y = 420
for i in range(760):
    bv = 3 - i/200 # от 5 до -5
    t = bv2t(bv)
    color = t2rgb(t) # RGB цвет по температуре

    idraw.rectangle((x, y, x+1, y+100), fill=color)
    if i % 100 == 0:
        idraw.line([(x, y+100), (x, y+105)], fill=128)
        idraw.multiline_text((x-10, y+115), str(round(bv, 1)), font=fnt2, fill=(0, 0, 0))
        idraw.multiline_text((x-13, y+125), str(int(t)), font=fnt2, fill=(0, 0, 0))
    x += 1

img.save('test_colorscale.png')
exit()
