import re

def clear_names(file_name: str) -> list:
    """ Принимает имя файла и возвращает список имен, содержащихся в файле"""
    new_names_list = list()
    with open("../data/" + file_name, 'r', -1, 'UTF-8') as names_file:
        names_list = names_file.read().split()
        for name in names_list:
            new_name = ''
            for char in name:
                if char.isalpha():
                    new_name += char
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list


def is_russian_name(name_item: str) -> bool:
    """ Проверка имени на русскость"""
    return bool(re.search('[а-яА-Я]', name_item))


def filter_russian_names(names_list: list) -> list:
    """ Фильтрация русских имен"""
    new_names_list = list()
    for name_item in names_list:
        if is_russian_name(name_item):
            new_names_list.append(name_item)
    return new_names_list

if __name__ == "__main__":
    cleared_names = clear_names("names.txt")

    print(filter_russian_names(cleared_names))


    # for i in cleared_names:
    #     print(i)
