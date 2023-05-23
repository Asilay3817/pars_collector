import time
from selenium import webdriver
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from random import randint

from selenium.webdriver.common.by import By


class Open_mv():

    def select_phone_items(self):
        global result
        o = Options()
        ua = UserAgent.random
        # o.add_argument("--headless")
        o.add_argument(f'user-agent={ua}')
        driver = webdriver.Chrome(chrome_options=o)
        driver.maximize_window()

        uniq_value = set()
        big_data = []

        for i in range(1, 3):
            base_url = f'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=iphone-914/tolko-v-' \
                       f'nalichii=da?showCount=12&page={i}'
            driver.get(base_url)

            time.sleep(randint(3, 7))

            try:
                d = driver.find_element(By.XPATH, "//div[@class='listing-view-switcher__pointer listing-view-switcher__pointer--list']")
                result = d.is_enabled()
                print(result)
                if result == True:
                    driver.find_element(By.XPATH,
                                        "(//button[@class='button button--light button--only-icon button--with-icon"
                                        " ng-star-inserted'])[2]").click()
            except NoSuchElementException as ex:
                pass


            block = driver.find_element(By.CLASS_NAME, 'plp__card-grid')

            time.sleep(randint(2, 4))

            find_end_page = driver.find_element(By.XPATH, "//div[@class='show-more']")
            webdriver.ActionChains(driver).move_to_element(find_end_page).perform()
            webdriver.ActionChains(driver).scroll_to_element(find_end_page).perform()


            value = block.find_elements(By.PARTIAL_LINK_TEXT, 'Apple iPhone')
            price = block.find_elements(By.CLASS_NAME, 'price__main-value')

            value_list = []
            price_list = []

            for i in value:
                value_list.append(i.text)
            for j in price:
                price_list.append(j.text)

            data = dict(zip(value_list, price_list))
            x = list(data.items())

            for y in x:
                uniq_value.add(y)



        # # поключаем гугл акаунт и гугл таблицы
        # scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive "]
        # credentials = ServiceAccountCredentials.from_json_keyfile_name('python-pars-kd-f9004d270251.json', scope)
        # client = gspread.authorize(credentials)
        # # открываем созданную таблицу для записи данных
        # sheet = client.open('KD').sheet1
        #
        # list_to_upload = []
        #
        # for item in big_data:
        #     for k, v in item.items():
        #         list_to_upload.append([k, v])
        #
        # sheet.update("C3:D250", list_to_upload)






mv = Open_mv()
mv.select_phone_items()




