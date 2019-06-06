import re
# Библиотека для леммирования
from pymystem3 import Mystem

def text_to_vowpal_wabbit(s):
    # Проверка входных параметров и объявление переменных
    if len(s) < 30:
        raise Exception("Длинна строки меньше 30 символов")
    res = ''
    # Для леммирования
    mystem = Mystem()

    # Добавление модальности - текст
    res = '|text '
    # Леммирование - получаем массив слов
    lemmas = mystem.lemmatize(s)

    for l in lemmas:
        l_strip = l.strip()

        if (
            # Пропуск слишком коротких слов
            len(l_strip) > 3
            # Проверка на наличие русских букв
            and re.match("^[А-Яа-я]*$", l_strip)
            # Проверка длинны слова
            and len(l_strip) < 30
        ):
            # Пропуск слишком длинных слов
            res = res + l_strip + ' '
        
    return res
