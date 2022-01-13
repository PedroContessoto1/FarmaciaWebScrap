import time

from selenium import webdriver
import os
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

url = "https://www.google.com.br/"
key_search_google = "&tbm=isch&ved=2ahUKEwiO56T85Kz1AhWwOLkGHSqrDqIQ2-cCegQIABAA&oq=dipirona1&gs_lcp" \
                    "=CgNpbWcQAzoHCCMQ7wMQJzoFCAAQgARQkAlYkAlg5A5oAHAAeACAAWSIAboBkgEDMS4xmAEAoAEBqg" \
                    "ELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=qRbfYc7uE7Dx5OUPqta6kAo&bih=714&biw=1536&hl=en "

df = pd.read_csv(os.getcwd() + "\\medicines.csv")
df.columns = ['medicines']

list_medicines = [i for i in df['medicines']]
num_list = len(list_medicines)


def search_to_url(search: str) -> str:
    search = search.lower()
    keyword_search = search.replace(" ", "+")
    url_ready = url + "search?q=" + keyword_search + key_search_google
    return url_ready


def percentage_donwload(num_list: int, num_for: int) -> str:
    return " % " + "%.2f" % (num_for * 100 / num_list)


def crop_image(path: str):
    img = Image.open(path)
    w, h = img.size
    img.crop((0, 45, w, h)).save(path)


def save_img_local(search: str):
    search = search.lower()
    os.mkdir(os.getcwd() + f"\\imagens_google\\{search}")
    for i in range(1, 15):
        try:
            if EC.element_to_be_clickable('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img'):
                driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img').click()
                if EC.presence_of_element_located(
                        '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img'):
                    driver.find_element_by_xpath(
                        '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').screenshot(
                        os.path.dirname(os.path.realpath(__file__)) + f'\\imagens_google\\{search}\\{search}{i}.png')
                    crop_image(
                        os.path.dirname(os.path.realpath(__file__)) + f'\\imagens_google\\{search}\\{search}{i}.png')
        except:
            continue
    return f"donwload do {search} feito"


if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    acc = 0

    driver = webdriver.Chrome(executable_path='chromedriver_win32\\chromedriver.exe', chrome_options=options)

    for medicines in list_medicines:
        acc += 1
        driver.get(search_to_url(medicines))
        files = [arquivo for _, arquivo, _ in os.walk(os.getcwd() + '\\imagens_google')]
        if medicines in files[0]:
            print(f"Ja existe pasta {medicines}{percentage_donwload(num_list, acc)}")
        else:
            print(save_img_local(medicines) + percentage_donwload(num_list, acc))
