# Библиотека для леммирования
from pymystem3 import Mystem

def text_to_vowpal_wabbit(s):
    # Проверка входных параметров и объявление переменных
    if len(s) < 10:
        raise Exception("Длинна строки меньше 10 символов")
    res = ''
    # Для леммирования
    mystem = Mystem()

    # Добавление модальности - текст
    res = '|text '
    # Леммирование - получаем массив слов
    lemmas = mystem.lemmatize(s)
    for l in lemmas:
        if len(l) > 30:
            # Проверка длинны слова
            raise Exception("Длинна слова больше 30 символов")
        elif len(l)>3:      # Игнорируем знаки препинания, пробелы и так далее
            # Дописывание в результат через пробел
            res = res + l + ' '
    return res
