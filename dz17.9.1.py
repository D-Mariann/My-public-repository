def validityInput(input):
    array = input.split()
    try:
        array = list(map(int, array))
    except ValueError:
        return False
    return array


def checkInput(array):
    if array == False:
        print('Введены невалидные данные.')
    if len(array) == 0:
        print("Список пуст. Введите что-нибудь.")


import random
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        x = random.choice(array)
        min = [i for i in array if i < x]
        equal = [i for i in array if i == x]
        max = [i for i in array if i > x]
        sort_array = list(quick_sort(min) + equal + quick_sort(max))
        return sort_array


def bi_search(array, number, start, stop):
    try:
        if start > stop:
            return stop, start
        else:
            mid = (start + stop) // 2
            if number == array[mid]:
                return mid
            elif number < array[mid]:
                x = bi_search(array, number, start, mid - 1)
                return x
            elif number > array[mid]:
                x = bi_search(array, number, mid + 1, stop)
                return x
    except IndexError:
        return False


def neighbor_index(*args, **kwargs):
    if not index:
        print(f'Введенное число выходит за пределы списка. Индекс числа меньше введенного: {len(sort_array)-1}.')
        return app(sort_array, number, quick_sort)
    elif index in range(len(sort_array)):
        return f'Индекс числа, меньше введенного: {(index)-1}, \nиндекс числа большего или равного введенному: {(index)+1}'
    elif len(index) == 2:
        if index[0] == -1:
            print(f'Число {number} отсутствует в списке. Индекс числа больше введенного: {index[1]}.')
        else:
            print(f'Число {number} отсутствует в списке.'
              f'\nИндекс числа, меньше введенного: {index[0]}, индекс числа большего или равного введенному: {index[1]}.')
        return app(sort_array, number, quick_sort)
    elif index == 0:
        return f'Числа, меньше введенного, нет (это минимальное число).\nИндекс числа большего или равного введенному: {(index)+1}'
    elif index == sort_array[-1]:
        return f'Индекс числа, меньше введенного: {(index)-1}. \nЧисла, больше введенного, нет. Это максимальное число.'



def app(sort_array, number, func):
    x = input('Хотите его добавить? ').lower()
    if x in ['yes', 'да']:
        sort_array.append(number)
        sort_array = quick_sort(sort_array)
        print('Число добавлено в список, порядок отсортирован.')
        return sort_array


user_input = input('Введите последовательность целых чисел через пробел: ')
number = int(input('Введите число, которое хотите найти: '))

array = validityInput(user_input)
checkInput(array)
sort_array = quick_sort(array)
index = bi_search(sort_array, number, 0, len(sort_array))
neighbor_index(index, number, sort_array, quick_sort, app)




