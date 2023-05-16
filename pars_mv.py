import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from lxml import etree


# o = Options()
# ua = UserAgent.random
# o.add_argument("--headless")
# o.add_argument(f'user-agent={ua}')
# driver = webdriver.Chrome(chrome_options=o)
# base_url = 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=iphone-914'
# driver.get(base_url)
#
# time.sleep(11)
#
# with open('value_mv.html', 'w', encoding='utf-8') as f:
#     f.write(driver.page_source)

local = "/Users/asilay/Desktop/study/QA/Parcer/value_mv.html"
#создаем переменную с функцией парсинга html
html_parser = etree.HTMLParser(encoding='utf-8')
#создаем переменную в которой хранится локальный файл из которого будем парсить данные используя xpath
tree = etree.parse(local, html_parser)

#списки в которые добавляем значения после парсинга файла
items = []
price = []

for value in tree.xpath('//a/text()'):
    if "Смартфон Apple iPhone" not in value:
        continue
    else:
        items.append(value)

for value in tree.xpath('//span/text()'):
    if len(value)<=11:
        price.append(value)

print(items)
print(price)

# driver.close()
# driver.quit()




