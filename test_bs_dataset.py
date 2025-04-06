# -*- coding: utf-8 -*-
#
# Тест фукнций библиотеки star_colors.py на всём датасете ярких звёзд до 6,5m.
# Используется датасет 'dataset_bright_stars.csv' https://github.com/dyuk108/brightstar_dataset
# Клыков Д.Ю., 2025.

from star_colors import *
import pandas as pd

# Читаем датасет dataset_bright_stars.csv
# Индексы столбцов: 0 - Vmag, 14 - B-V, 21 - SpType, 22 - Teff.
df = pd.read_csv('dataset_bright_stars.csv', usecols=[0, 14, 21, 22])
print('Всего звёзд: ', df.shape[0])

# Проверка всех спектральных классов. Заполняемость датасета 100%.
print('Определение типичной эффективной температуры по сп. классу.')
df['Teff_sptype'] = df['SpType'].apply(sptype2t)
filtered_df = df[df['Teff_sptype'].isnull()]
print('Не определена температура звёзд:', filtered_df.shape[0])