from bs4 import BeautifulSoup
import urllib.request as request


def parse_site(url):
    req = request.urlopen(url)
    html = req.read()
    soup = BeautifulSoup(html, 'html.parser')
    parse_object = soup.find_all('div', class_='news-tidings__item')
    return parse_object


def write_to_file(func):
    def wrapped(data, filename='results.txt'):
        result = func(data)
        with open(filename, 'w', encoding='utf-8') as file:
            for index, item in enumerate(result):
                file.write(f"{index+1}) {item['title']}\n"
                           f"Description: {item['description']}\n"
                           f"Link: {item['link']}"
                           f"\n\n")
        return result
    return wrapped


@write_to_file
def get_data(url):
    results = []
    news = parse_site(url)

    for index, item in enumerate(news):
        title = item.find('span', class_='news-helpers_show_mobile-small')
        if title:  # check if there
            description = item.find('div', class_='news-tidings__speech')
            link = item.a
            results.append({
                "title": title.get_text(strip=True),
                "description": description.get_text(strip=True),
                "link": link.get('href')
            })
    return results


def main():
    url = 'https://tech.onliner.by/tag/it-belarus'
    parse_data = get_data(url)


if __name__ == "__main__":
    main()
