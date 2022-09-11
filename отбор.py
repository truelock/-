import numpy as np
import re
# Считаем файл с текстом
text = open ('text.txt', endcoding='utf-8').read()

#  Отформатируем текст
text = text.lower()
text = re.split("[^a-zа-яё]+", text)

#Разделим текст на слова
text = text.split()

#Сохраним модель
file_name = str(input('введите название модели сохранения '))
np.save('{}.npy'.format(file_name), text)

#Pагрузим модель
file_name = str(input('введите название модели зарузки '))
read_dictionary = np.load('{}.npy'.format(file_name)).item()

#Генерируем последователность
length=int(input('Введите длину последовательности'))
def make_words(text):
    for i in range(len(text)-1):
        yield (text[i],text[i+1])

words = make_words(text)
# создадим словарь
dictionary ={}

for text_1,text_2 in words:
    if text_1 in dictionary:
        dictionary[text_1].append(text_1)
