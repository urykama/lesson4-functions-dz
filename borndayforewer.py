"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


def view(text, correct_answer):
    while True:
        year = input(text)
        # print(year, correct_answer)
        if year == correct_answer:
            print('            И так сойдёт')
            return
        print("      Не верно")


def control():
    view('Ввведите год рождения А.С.Пушкина:', '1799')
    view('В какой день июня родился Пушкин?', '6')

if name == __main__:
    control()