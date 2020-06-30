#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
#number = np.random.randint(1,101)    # загадали число

def game_core_v3(number):
    '''Реализуем алгоритма поиска методом половинного деления.
       Функция принимает загаданное число и возвращает число попыток'''
    lower_limit = 1                             # задаем начальный нижний предел диапазона поиска
    higher_limit = 100                          # задаем начальный верхний предел диапазона поиска
    predict = (lower_limit + higher_limit)//2   # расчитываем число для первой попытки угадывания
    count = 1                                   # счетчик количества попыток
    while number != predict:
        if number > predict:  
            lower_limit = predict + 1  # если загаданное число больше, то сдвигаем нижнюю границу диапазона поиска
        elif number < predict: 
            higher_limit = predict - 1
        predict = (lower_limit + higher_limit)//2  # если загаданное число меньше, то сдвигаем нижнюю границу диапазона поиска
        count+=1
    return(count) # выход из цикла, если угадали



def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# Проверяем
score_game(game_core_v3)


# In[ ]:




