import gspread
from oauth2client.service_account import ServiceAccountCredentials

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree



class Pars():
    def select_kd_value(self):
        # поключаем гугл акаунт и гугл таблицы
        # scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive "]
        # credentials = ServiceAccountCredentials.from_json_keyfile_name('python-pars-kd-f9004d270251.json', scope)
        # client = gspread.authorize(credentials)

        # создаем таблицу и указываем под каким аккаунтом будет работать гугл таблица
        # sheet = client.create('KD')
        # sheet.share('asilaydying3817@gmail.com', perm_type='user', role='writer')

        # поключаем гугл акаунт и гугл таблицы
        scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive "]
        credentials = ServiceAccountCredentials.from_json_keyfile_name('python-pars-kd-f9004d270251.json', scope)
        client = gspread.authorize(credentials)
        # открываем созданную таблицу для записи данных
        sheet = client.open('KD').sheet1

        """запуск необходимого ресурса через selenium"""

        #запускает браузер без отображения графического интерфейса
        options = Options()
        options.add_argument('--headless') #режим запуска без отображения ui
        driver = webdriver.Chrome(options=options)
        base_url = 'https://kdmarket.ru/catalog/apple/'
        driver.get(base_url)
        print("старт")



        # очевидное ожидание в 3сек (чтобы элементы погрузились и стали доступны для взаимодействия
        driver.implicitly_wait(3)
        print("начало записи")



        # начало записи разметки страниц если вылетает ошибка UnicodeEncodeError: 'charmap'
        with open('value_kd.html', mode='a', encoding='utf-8') as f:
            f.write(driver.page_source)


        #начало записи разметки страниц
        # with open("value.html", "w") as file:
        #         file.write(driver.page_source)


        #скролл страницы до отображения футера сайта (в данном случае не используется)
        # action = ActionChains(driver)
        # find_more_elements = driver.find_element(By.XPATH, "//div[@class = 'catalog_section _разъем']")
        # action.move_to_element(find_more_elements).perform()
        # action.scroll_to_element(find_more_elements).perform()
        # print("скролл раздела со всей техникой завершен")


        #присваиваем переменной файл с html кодом страницы
        local = "/Users/asilay/Desktop/study/QA/Parcer/value_kd.html"
        print("данные записаны, файл открыт для получения и фитрации данных")


        #создаем переменную с функцией парсинга html
        html_parser = etree.HTMLParser()
        #создаем переменную в которой хранится локальный файл из которого будем парсить данные используя xpath
        tree = etree.parse(local, html_parser)


        #списки в которые добавляем значения после парсинга файла
        items = []
        price = []

        # списки со значениям которые потребуется дополнительно отфильтровать
        filter_list_items = ['Мобильные телефоны', 'Красота и здоровье', 'Игровые приставки']
        filter_list_price = ['\n        ', 'Гаджеты', 'Для дома', 'Для кухни', 'Цена', 'Серия', 'Планшеты', 'Аудио']

        #берем необходимые данные, фильтруем и разбиваем на два списка
        for value in tree.xpath('//p/text()'):
            if len(value) > 16 and "Данная страница является" not in value:
                items.append(value)
            if len(value) < 10:
                price.append(value)

        # фильтруем данные используя список items от мусора который остался
        def filter_duplicate_items(string_to_check):
            if string_to_check in ll:
                return False
            else:
                return True

        # Применение filter() для удаления повторяющихся строк
        ll = filter_list_items
        out_filter_items = list(filter(filter_duplicate_items, items))
        ll = filter_list_items
        out_filter_items += list(filter(filter_duplicate_items, items))


        # фильтруем данные используя список price от мусора который остался
        def filter_duplicate_price(string_to_check):
            if string_to_check in ll:
                return False
            else:
                return True
        # Применение filter() для удаления повторяющихся строк
        ll = filter_list_price
        out_filter = list(filter(filter_duplicate_price, price))
        ll = filter_list_price
        out_filter += list(filter(filter_duplicate_price, price))


        b = out_filter_items[:118]
        d = out_filter[:118]
        nice = dict(zip(b, d))

        # создаем список содержащий списки ключ:значение из словаря
        item_value_list = [[i,j] for i,j in nice.items()]


        # указываем диапазон заполнения столбцов, в качестве заполнителей выступают списки ключ:значение
        sheet.update("A2:B119", item_value_list)



#создание экземпляра класса и вызов метода класса
pars = Pars()
pars.select_kd_value()





