# чаще функция определяется с параметрами - нам важно передать какие-то значения внутрь функции


# передаём в функцию строку и получаем обратно список
def split_tags(tag_string):
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())
    return tag_list


string = "python, coursera, mooc"
print(split_tags(string))  # ['python', 'coursera', 'mooc']

# выпадет ошибка - функция ожидает параметр и не знает, что делать, если его нет
print(split_tags())  # TypeError: split_tags() missing 1 required positional argument: 'tag_string'
