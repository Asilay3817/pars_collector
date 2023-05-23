import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from random import randint

from selenium.webdriver.common.by import By


class Open_rst():

    def select_phone_items(self):
        global result
        o = Options()
        ua = UserAgent.random
        o.add_argument("--headless")
        o.add_argument(f'user-agent={ua}')
        driver = webdriver.Chrome(chrome_options=o)
        # driver.maximize_window()

        uniq_value = set()


        for i in range(1, 5):
            base_url = f'https://re-store.ru/apple-iphone/?page={i}'
            driver.get(base_url)

            time.sleep(randint(3, 7))

            block = driver.find_element(By.CLASS_NAME, 'catalog__products')

            time.sleep(randint(2, 4))

            find_end_page = driver.find_element(By.XPATH, "//button[@class='btn btn--black btn--size-sm btn--full-width']")
            webdriver.ActionChains(driver).move_to_element(find_end_page).perform()
            webdriver.ActionChains(driver).scroll_to_element(find_end_page).perform()

            value = block.find_elements(By.CLASS_NAME, 'product-card__title')
            price = block.find_elements(By.CLASS_NAME, 'product-card__price-new')

            value_list = []
            price_list = []

            for i in value:
                value_list.append(i.text)
            for j in price:
                price_list.append(j.text)

            data = dict(zip(value_list, price_list))
            print(len(data))
        #     x = list(data.items())
        #
        #     for y in x:
        #         uniq_value.add(y)
        # print(len(uniq_value))


rst = Open_rst()
rst.select_phone_items()

