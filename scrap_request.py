import time
import requests, lxml.html
from bs4 import BeautifulSoup
import os

list_medicine = ["dipirona", "diamox", "protetor solar"]
list_links_photos = []


url = "https://www.google.com.br/"
key_search_google = "&tbm=isch&ved=2ahUKEwiO56T85Kz1AhWwOLkGHSqrDqIQ2-cCegQIABAA&oq=dipirona1&gs_lcp=CgNpbWcQAzoHCCMQ7wMQJzoFCAAQgARQkAlYkAlg5A5oAHAAeACAAWSIAboBkgEDMS4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=qRbfYc7uE7Dx5OUPqta6kAo&bih=714&biw=1536&hl=en"


def search_to_url(search: str) -> str:
    keyword_search = search.replace(" ", "+")
    url_ready = url + "search?q=" + keyword_search + key_search_google
    return url_ready


def get_code_from_url(url_ready: str) -> BeautifulSoup:
    page = requests.get(url_ready, time.sleep(3))
    soup = BeautifulSoup(page.text, 'lxml')
    body = soup.find('body')
    return body


def filter_picture(soup: BeautifulSoup):
    img = soup.find_all('img')
    for i in img:
        if 'https://' in i['src']:
            link = i['src']
            print(link)


def save_html(html):
    arquivo = open('arq01.txt', 'w')
    for i in html:
        arquivo.write(str(i))
    arquivo.close()


if __name__ == '__main__':
    asw = input(f"começar? (Y/n)")
    if asw not in ['y', 'Y', '']:
        exit(0)

    filter_picture(get_code_from_url(search_to_url("dipirona")))
