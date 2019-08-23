def input_args(*args):
    arg_list = []
    for x in args:
        arg_list.append(x)  # создаем список из полученных аргументов, которые переводим в тип данных str
        arg_list.sort(key=len)  # сортируем список по длине
    return arg_list[-1]  # возвращаем последний элемент списка, который после сортировки должен иметь максимальную длину


print(input_args('1', 'dasd', 'da', 'fdfsdsdfsdfsdfsdfsdfsdfsdfs', 'v', 'zzzzcwqdfwe'))