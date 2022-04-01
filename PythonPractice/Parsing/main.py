from Parser import Parser


def main():
    url = 'https://tech.onliner.by/tag/it-belarus'
    file_path = 'news.txt'
    parser = Parser(url, file_path)
    parser.run()
    print(parser.results)


if __name__ == "__main__":
    main()
