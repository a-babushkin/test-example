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


if __name__ == "__main__":
    cleared_names = clear_names("names.txt")

    for i in cleared_names:
        print(i)
