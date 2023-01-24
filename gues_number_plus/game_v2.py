"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count





def bisection_predict(number: int = 1) -> int:
    """Угадываем число методом деления пополам

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    l_board=-1 # Расширяем нижнюю границу диапазона, чтобы предотвратить зацикливание алгоритма в случае,
    # когда загаданное число равно 1 (нижняя граница)
    u_board=101 # Расширяем верхнюю границу диапазона, чтобы предотвратить зацикливание алгоритма в случае,
    # когда загаданное число равно 100 (верхняя граница)
    
    # Можно было бы написать if number == l_board и if number == u_board: , но тогда непонятно, считать это 
    # за одну попытку или за две :)) 
    
  
    while True:
        count += 1
        #predict_number = np.random.randint(1, 101)  # предполагаемое число
        predict_number = int((u_board+l_board)/2)
        if number ==  predict_number:
            break  # выход из цикла если угадали
        if number > predict_number:
            l_board=predict_number
        if number < predict_number:
            u_board=predict_number    
        #print(predict_number, '-->', number)    
        
    return count



def score_game(predict_func) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score




if __name__ == "__main__":
    # RUN
    print("Угадываем рандомно :")
    score_game(random_predict)
    print("Делим пополам :")
    score_game(bisection_predict)
