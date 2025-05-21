import requests
from bs4 import BeautifulSoup


def parsing_beautifulsoup(url):
    """
    뷰티풀 수프로 파싱하는 함수
    :param url: paring할 URL. 여기선 YES24 Link
    :return: BeautifulSoup soup Object
    """

    data = requests.get(url)

    html = data.text
    return BeautifulSoup(html, 'html.parser')


def extract_book_data(soup):
    """
    BeautifulSoup Object에서 book data를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """

    upload_contents = ''
    new_books = soup.select(".goodsTxtInfo")
    url_prefix = "http://www.yes24.com"

def extract_book_data(soup):
    """
    BeautifulSoup Object에서 book data를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """
    upload_contents = ''
    new_books = soup.select(".gd_name")
    url_prefix = "http://www.yes24.com"

    for new_book in new_books:
        book_name = new_book.text.strip()
        url_suffix = new_book['href']
        url = url_prefix + url_suffix

        content = f'<a href="{url}">{book_name}</a><br/>\n'
        upload_contents += content

    return upload_contents
