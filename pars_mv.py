import time
from selenium import webdriver
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from random import randint

from selenium.webdriver.common.by import By
o = Options()
ua = UserAgent.random
o.add_argument("--headless")
o.add_argument(f'user-agent={ua}')
driver = webdriver.Chrome(chrome_options=o)
# driver.maximize_window()
big_data = []

class Open_mv():

    def select_phone_items(self):
        global result

        for i in range(1, 8):
            base_url = f'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=iphone-914/tolko-v-' \
                       f'nalichii=da?showCount=12&page={i}'
            driver.get(base_url)

            time.sleep(randint(2, 4))

            try:
                d = driver.find_element(By.XPATH, "//div[@class='listing-view-switcher__pointer listing-view-switcher__pointer--list']")
                result = d.is_enabled()
                if result == True:
                    driver.find_element(By.XPATH,
                                        "(//button[@class='button button--light button--only-icon button--with-icon"
                                        " ng-star-inserted'])[2]").click()
            except NoSuchElementException as ex:
                pass

            value = 'Apple iPhone'
            price = 'price__main-value'
            self.sorted_items(value, price)

    def select_ipad_items(self):
        global result

        for i in range(1, 8):
            base_url = f'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/' \
                       f'category=planshety-apple-927/tolko-v-nalichii=da?showCount=12&page={i}'
            driver.get(base_url)

            time.sleep(randint(2, 4))

            try:
                d = driver.find_element(By.XPATH, "//div[@class='listing-view-switcher__pointer listing-view-switcher__pointer--list']")
                result = d.is_enabled()
                if result == True:
                    driver.find_element(By.XPATH,
                                        "(//button[@class='button button--light button--only-icon button--with-icon"
                                        " ng-star-inserted'])[2]").click()
            except NoSuchElementException as ex:
                pass

            value = 'Apple iPad'
            price = 'price__main-value'
            self.sorted_items(value, price)

    def select_mac_items(self):
        global result

        for i in range(1, 8):
            base_url = f'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/' \
                       f'brand=apple/tolko-v-nalichii=da?reff=menu_main&showCount=12&page={i}'
            driver.get(base_url)

            time.sleep(randint(2, 4))

            try:
                d = driver.find_element(By.XPATH, "//div[@class='listing-view-switcher__pointer listing-view-switcher__pointer--list']")
                result = d.is_enabled()
                if result == True:
                    driver.find_element(By.XPATH,
                                        "(//button[@class='button button--light button--only-icon button--with-icon"
                                        " ng-star-inserted'])[2]").click()
            except NoSuchElementException as ex:
                pass

            value = 'Apple MacBook Pro'
            price = 'price__main-value'
            self.sorted_items(value, price)

    def select_watch_items(self):
        global result

        for i in range(1, 8):
            base_url = f'https://www.mvideo.ru/gadzhety-64/smart-chasy-400/f/category=apple-watch-2948/' \
                       f'brand=apple/tolko-v-nalichii=da?showCount=12&page={i}'
            driver.get(base_url)

            time.sleep(randint(2, 4))

            try:
                d = driver.find_element(By.XPATH, "//div[@class='listing-view-switcher__pointer listing-view-switcher__pointer--list']")
                result = d.is_enabled()
                if result == True:
                    driver.find_element(By.XPATH,
                                        "(//button[@class='button button--light button--only-icon button--with-icon"
                                        " ng-star-inserted'])[2]").click()
            except NoSuchElementException as ex:
                pass

            value = 'Смарт-часы Apple'
            price = 'price__main-value'
            self.sorted_items(value, price)

    def select_headphones_items(self):
        global result

        for i in range(1, 4):
            base_url = f'https://www.mvideo.ru/naushniki-54/naushniki-3967/f/brand=apple/' \
                       f'tolko-v-nalichii=da/tip-podklucheniya=bluetooth?showCount=12&page={i}'
            driver.get(base_url)

            time.sleep(randint(2, 4))

            try:
                d = driver.find_element(By.XPATH, "//div[@class='listing-view-switcher__pointer listing-view-switcher__pointer--list']")
                result = d.is_enabled()
                if result == True:
                    driver.find_element(By.XPATH,
                                        "(//button[@class='button button--light button--only-icon button--with-icon"
                                        " ng-star-inserted'])[2]").click()
            except NoSuchElementException as ex:
                pass

            value = 'Apple AirPods'
            price = 'price__main-value'
            self.sorted_items(value, price)

    def sorted_items(self, value_items, value_price):
        # uniq_value = set()


        block = driver.find_element(By.CLASS_NAME, 'plp__card-grid')


        find_end_page = driver.find_element(By.XPATH, "//div[@class='show-more']")
        webdriver.ActionChains(driver).move_to_element(find_end_page).perform()
        webdriver.ActionChains(driver).scroll_to_element(find_end_page).perform()

        value = block.find_elements(By.PARTIAL_LINK_TEXT, value_items)
        price = block.find_elements(By.CLASS_NAME, value_price)

        # поиск необходиммых значений
        value_list = []
        price_list = []

        for i in value:
            value_list.append(i.text)
        for j in price:
            price_list.append(j.text)

        data = dict(zip(value_list, price_list))

        for i in list(data.items()):
            big_data.append(i)







# # поключаем гугл акаунт и гугл таблицы
# scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive "]
# credentials = ServiceAccountCredentials.from_json_keyfile_name('python-pars-kd-f9004d270251.json', scope)
# client = gspread.authorize(credentials)
# # открываем созданную таблицу для записи данных
# sheet = client.open('KD').sheet1
# list_to_upload = []
# for item in big_data:
#     for k, v in item.items():
#         list_to_upload.append([k, v])
#
# sheet.update("C3:D250", list_to_upload)






mv = Open_mv()
mv.select_phone_items()
mv.select_ipad_items()
mv.select_mac_items()
mv.select_watch_items()
mv.select_headphones_items()
for i in big_data:
    print(i)




