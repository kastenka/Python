from bs4 import BeautifulSoup
import urllib.request


class Parser:

    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, file_path='results.txt'):
        self.url = url
        self.file_path = file_path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def save_to_file(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            for index, item in enumerate(self.results):
                file.write(f"{index+1}) {item['title']}\n"
                           f"Description: {item['description']}\n"
                           f"Link: {item['link']}"
                           f"\n\n")

    def parsing(self):
        news = self.html.find_all('div', class_='news-tidings__item')

        for index, item in enumerate(news):
            title = item.find('span', class_='news-helpers_show_mobile-small')
            if title:  # check if there
                description = item.find('div', class_='news-tidings__speech')
                link = item.a
                self.results.append({
                    "title": title.get_text(strip=True),
                    "description": description.get_text(strip=True),
                    "link": link.get('href')
                })

    def run(self):
        self.get_html()
        self.parsing()
        self.save_to_file()

