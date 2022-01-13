import time
from selenium import webdriver
import os
import pandas as pd

url = "https://www.drogaraia.com.br/"

df = pd.read_csv(os.getcwd() + "\\medicines.csv")
df.columns = ['medicines']

list_medicines = [i for i in df['medicines']]


def search_to_url(search: str) -> str:
    keyword_search = search.replace(" ", "%20")
    url_ready = url + "busca?q=" + keyword_search
    print(url_ready)
    return url_ready


def save_img_local(search: str):
    os.mkdir(os.getcwd() + f"\\imagens_drogaraia\\{'xarelto'}")
    for i in range(1, 2):
        driver.find_element_by_xpath(f'//*[@id="products"]/div[{i}]/div/figure/div/a/picture/img').screenshot(
            os.path.dirname(os.path.realpath(__file__)) + f'\\imagens_drogaraia\\{"xarelto"}\\{"xarelto"}{i}.png')


if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")

    driver = webdriver.Chrome(executable_path='chromedriver_win32\\chromedriver.exe', chrome_options=options)

    for medicines in list_medicines:
        driver.get(search_to_url(medicines))

        files = [arquivo for _, arquivo, _ in os.walk(os.getcwd() + '\\imagens_drogaraia')]

        if medicines in files[0]:
            print(f"Ja existe pasta {medicines}")
        else:
            save_img_local(medicines)
