# Отладка. Классический метод отладки PythonDEbugger
import requests
import re


def main(site_url, substring):
    import pdb  # для запуска отладчика
    pdb.set_trace()  # запускаем отладку здесь, pdb.set_trace - стандартный способ, импорт прямо здесь

    site_code = get_site_code(site_url)
    matching_substrings = get_matching_substrings(site_code, substring)
    print("'{} found {} times in {}'".format(
        substring, len(matching_substrings), site_url
    ))


def get_site_code(site_url):
    if not site_url.startswith("http"):
        site_url = "http://" + site_url
    return requests.get(site_url).text


def get_matching_substrings(source, substring):
    return re.findall(substring, source)


main("mail.ru", "script")