import time
import re

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from random import randint

from selenium.webdriver.common.by import By


class Open_dn():

    def select_phone_items(self):
        global result
        o = Options()
        ua = UserAgent.random
        o.add_argument("--headless")
        o.add_argument(f'user-agent={ua}')
        driver = webdriver.Chrome(chrome_options=o)
        # driver.maximize_window()

        uniq_value = set()

        for i in range(1,8):
            base_url = f'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/?stock=now&brand=apple&p={i}&mode=tile'
            driver.get(base_url)

            time.sleep(randint(4, 8))

            # try:
            #     d = driver.find_element(By.XPATH, "//label[@for='mode-tile-D2T6']")
            #     result = d.is_selected()
            #     print(result)
            #     if result == False:
            #         driver.find_element(By.XPATH, "//label[@for='mode-tile-D2T6']").click()
            # # except NoSuchElementException as ex:
            # #     pass


            block = driver.find_element(By.XPATH, "//div[@class='catalog-products view-tile']")

            time.sleep(randint(3, 4))

            find_end_page = driver.find_element(By.CLASS_NAME, "pagination-widget__show-more-btn")
            webdriver.ActionChains(driver).move_to_element(find_end_page).perform()
            webdriver.ActionChains(driver).scroll_to_element(find_end_page).perform()

            value = block.find_elements(By.XPATH, "//span[contains(text(), 'Apple iPhone')] ")
            price = block.find_elements(By.XPATH, "//div[@class='product-buy__price-wrap product-buy__price-wrap_interactive']")

            value_list = []
            price_list = []

            for i in value:
                value_list.append(i.text[14:48])

            for j in price:
                if len(j.text)>33:
                    price_list.append(j.text[0:9])
                else:
                    price_list.append(j.text[0:8])


            data = dict(zip(value_list, price_list))
            print(len(data))

            # x = list(data.items())
            #
            # for y in x:
            #     uniq_value.add(y)







dn = Open_dn()
dn.select_phone_items()