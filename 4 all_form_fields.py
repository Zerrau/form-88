import datetime
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pywinauto.application import Application

date = datetime.datetime.now()
date_now = date.strftime("%d%m%Y")
date_year = date.strftime("%Y")

# Добавляем расширение
executable_path = "chromedriver.exe"
os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension('CryptoPro.zip')  # Расширение CryptoPro

browser = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
browser.get("http://localhost:3000")

#######################################
browser.implicitly_wait(5)
dbl_click = webdriver.ActionChains

try:
    # Логинимся
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[1]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[2]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[3]/button').click()
    # Создаем пациента
    """browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/button').click()
    browser.find_element_by_xpath('//*[@id="lastName"]').send_keys('Фамилия')
    browser.find_element_by_xpath('//*[@id="firstName"]').send_keys('Имя')
    browser.find_element_by_xpath('//*[@id="secondName"]').send_keys('Отчество')
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[4]/div/label').click()
    sex = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[4]/div/div/div/div/div[1]/div[2]/div/input')
    sex.send_keys('М')
    sex.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[5]/div[1]/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[5]/div[1]/div[1]/div/input').send_keys(
        '25071999')
    b_date = browser.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[2]/button')
    b_date.send_keys(Keys.ENTER)
    patient_successfully = browser.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div')

    assert patient_successfully.text == 'Данные пациента успешно сохранены', 'Patient not registered'"""

    # Ищем созданного пациента
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(
        'Фамилия Имя Отчество')
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]').click()
    browser.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div[3]/div/div/button').click()

    # (1)
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div/div/label').click()
    med_organization = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div/input')
    med_organization.send_keys(
        'Санкт')  # Санкт-Петербургское государственное бюджетное учреждение здравоохранения "Консультативно-диагностическая поликлиника №1 Приморского района"
    med_organization.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/input').send_keys(
        '1234567890')
    data_protocol = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/input')
    data_protocol.send_keys(date_now)
    data_protocol.send_keys(Keys.ENTER)
    date_of_issue = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[2]/div[2]/div[1]/div/div/input')
    date_of_issue.send_keys(date_now)
    date_of_issue.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[3]/div[1]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[3]/div[2]/div/label').click()

    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[1]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[3]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[2]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[4]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[5]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[6]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[7]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[8]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[9]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[10]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[11]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[12]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[13]/div/label').click()
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/div[1]/ul/li[2]').click()
    # (2)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[6]/div[1]/input').send_keys(
        '11111111145')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[9]/div[2]/div[5]/div[1]/textarea').send_keys(
        'МВД СПБ')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[9]/div[2]/div[2]/div[1]/input').send_keys(
        1234)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[9]/div[2]/div[3]/div/input').send_keys(
        '123456')
    date_of_issue = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[9]/div[2]/div[4]/div/div[1]/div/input').send_keys(
        date_now)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[10]/div/input').send_keys(
        '9653214780')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[11]/div/input').send_keys(
        'test@mail.ru')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[1]/div/label').click()
    # Дополнить Район субъекта РФ
    city1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[5]/div[1]/div/input')
    city1.send_keys('п')
    time.sleep(0.5)
    city1.send_keys(Keys.DOWN)
    city1.send_keys(Keys.ENTER)
    street1 = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[6]/div[1]/div/input')
    street1.send_keys('п')
    time.sleep(0.5)
    street1.send_keys(Keys.DOWN)
    street1.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[7]/div/input').send_keys('1')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[8]/div/input').send_keys('1')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[9]/div/input').send_keys(
        '111111')
    # Дополнить Район субъекта РФ
    city2 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[4]/div[1]/div/input')
    city2.send_keys('п')
    time.sleep(0.5)
    city2.send_keys(Keys.DOWN)
    city2.send_keys(Keys.ENTER)
    street2 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[5]/div/div/input')
    street2.send_keys('п')
    time.sleep(0.5)
    street2.send_keys(Keys.DOWN)
    street2.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[6]/div/input').send_keys('1')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[7]/div/input').send_keys('1')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[8]/div/input').send_keys(
        '111111')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[9]/div/input').send_keys(
        '1177746126040')
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/div[1]/ul/li[3]').click()
    # (3)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[1]/div[1]/input').send_keys(
        'Фамилия')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[2]/div/input').send_keys(
        'Имя')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[3]/div/input').send_keys(
        'Отчество')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[4]/div/input').send_keys(
        '11111111145')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[5]/div[2]/div[5]/div/textarea').send_keys(
        'МВД СПБ')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[5]/div[2]/div[2]/div[1]/input').send_keys(
        '1234')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[5]/div[2]/div[3]/div/input').send_keys(
        '123456')
    date_of_issue3 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[5]/div[2]/div[4]/div/div/div/input')
    date_of_issue3.send_keys(date_now)
    date_of_issue3.send_keys(Keys.ENTER)

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[6]/div[2]/div[5]/div[1]/textarea').send_keys(
        'МВД СПБ')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[6]/div[2]/div[2]/div/input').send_keys(
        '1234')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[6]/div[2]/div[3]/div/input').send_keys(
        '123456')
    date_of_issue3_2 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[6]/div[2]/div[4]/div/div/div/input')
    date_of_issue3_2.send_keys(date_now)
    date_of_issue3_2.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[7]/div/input').send_keys(
        '9653214780')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div/div[2]/div[8]/div/input').send_keys(
        'test@mail.ru')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div/div/div[2]/div[1]/div/input').send_keys(
        'A')
    subject_3 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div/div/div[2]/div[2]/div[1]/div/input')
    subject_3.send_keys('Санкт')
    subject_3.send_keys(Keys.DOWN)
    subject_3.send_keys(Keys.ENTER)

    city_3 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div/div/div[2]/div[4]/div[1]/div/input')
    city_3.send_keys('п')
    time.sleep(0.5)
    city_3.send_keys(Keys.DOWN)
    city_3.send_keys(Keys.ENTER)

    street_3 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div/div/div[2]/div[5]/div/div/input')
    street_3.send_keys('п')
    time.sleep(0.5)
    street_3.send_keys(Keys.DOWN)
    street_3.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div/div/div[2]/div[6]/div/input').send_keys(
        '1')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div/div/div[2]/div[7]/div/input').send_keys(
        '111111')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div/div/div[2]/div[8]/div/input').send_keys(
        '1177746126040')
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/div[1]/ul/li[4]').click()
    # (4)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[2]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[1]/div/label').click()
    invalid = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div/input')
    invalid.send_keys('Первая')
    invalid.send_keys(Keys.ENTER)

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[2]/div/label').click()
    period = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div/input')
    period.send_keys('Один')
    period.send_keys(Keys.ENTER)

    date_period = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[3]/div/div[1]/div/input')
    date_period.send_keys(date_now)
    date_period.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div/label').click()

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[5]/div/textarea').send_keys(
        'А')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[6]/div/textarea').send_keys(
        'А')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[7]/div/input').send_keys(
        '50')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[8]/div/label').click()
    term_of_disability = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[8]/div/div/div/div/div[1]/div[2]/div/input')
    term_of_disability.send_keys('6')
    term_of_disability.send_keys(Keys.ENTER)

    date_disability = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/div[2]/div[9]/div/div/div/input')
    date_disability.send_keys(date_now)
    date_disability.send_keys(Keys.ENTER)

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[1]/div/input').send_keys('А')
    Subject_4_1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[2]/div/div/input')
    Subject_4_1.send_keys('Санкт')
    Subject_4_1.send_keys(Keys.DOWN)
    Subject_4_1.send_keys(Keys.ENTER)

    citi_4_1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[4]/div/div/input')
    citi_4_1.send_keys('п')
    citi_4_1.send_keys(Keys.DOWN)
    citi_4_1.send_keys(Keys.ENTER)

    street_4_1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[5]/div/div/input')
    street_4_1.send_keys('п')
    street_4_1.send_keys(Keys.DOWN)
    street_4_1.send_keys(Keys.ENTER)

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[6]/div/input').send_keys('1')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[7]/div/input').send_keys(
        '111111')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[1]/div/input').send_keys(
        'Высшее образование')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[3]/div/input').send_keys(
        'Профессия')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[5]/div/input').send_keys(
        'Основная профессия')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[6]/div/input').send_keys(
        'Квалификация')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[7]/div/input').send_keys('1')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[9]/div/input').send_keys(
        'Cпециальность')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[10]/div/input').send_keys(
        'Должность')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[11]/div/input').send_keys(
        'Место работы')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[12]/div/input').send_keys(
        'Условия и хар.')

    Subject_4_2 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[14]/div/div[1]/div/div/input')
    Subject_4_2.send_keys('Санкт')
    Subject_4_2.send_keys(Keys.DOWN)
    Subject_4_2.send_keys(Keys.ENTER)

    citi_4_2 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[14]/div/div[3]/div/div/input')
    citi_4_2.send_keys('п')
    citi_4_2.send_keys(Keys.DOWN)
    citi_4_2.send_keys(Keys.ENTER)

    street_4_2 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[14]/div/div[4]/div/div/input')
    street_4_2.send_keys('п')
    street_4_2.send_keys(Keys.DOWN)
    street_4_2.send_keys(Keys.ENTER)

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[14]/div/div[5]/div/input').send_keys(
        '1')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[14]/div/div[6]/div/input').send_keys(
        '111111')
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/div[1]/ul/li[5]').click()

    # (5)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[1]/div[2]/div[1]/input').send_keys(
        date_year)

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[1]/textarea').send_keys('A')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[3]/div/textarea').send_keys('A')

    oneDate_5 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[4]/div[2]/div/div/div[1]/div/div/div/input')
    oneDate_5.send_keys(date_now)
    oneDate_5.send_keys(Keys.ENTER)

    endDate_5 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[4]/div[2]/div/div/div[2]/div/div/div/input')
    endDate_5.send_keys(date_now)
    endDate_5.send_keys(Keys.ENTER)

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[4]/div[2]/div/div/div[3]/div/input').send_keys(
        'Простуда')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[4]/div[3]/button').click()

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[5]/div/label').click()

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[6]/div[1]/input').send_keys(
        '908765432123')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[7]/div[2]/div[1]/div/input').send_keys(
        '123')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[7]/div[2]/div[2]/div/input').send_keys(
        '123')

    data_protocol_5 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[7]/div[2]/div[3]/div/div[1]/div/input')
    data_protocol_5.send_keys(date_now)
    data_protocol_5.send_keys(Keys.ENTER)

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[7]/div[5]/div/textarea').send_keys(
        'Тест Тест Тест')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[7]/div[3]/div/label').click()
    recovery_functions_5 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[7]/div[3]/div/div/div/div/div[1]/div[2]/div/input')
    recovery_functions_5.send_keys('полное')
    recovery_functions_5.send_keys(Keys.ENTER)

    achievement_5 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/input')
    achievement_5.send_keys('полное')
    achievement_5.send_keys(Keys.ENTER)

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[1]/div/input').send_keys(
        '123')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[2]/div/input').send_keys(
        '123')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[4]/div/input').send_keys(
        '123')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[7]/div[2]/div/textarea').send_keys(
        'A')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[8]/div[2]/div/textarea').send_keys(
        'A')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[5]/div[2]/div/input').send_keys(
        '123')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[5]/div[3]/div/input').send_keys(
        '123')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[5]/div[4]/div/input').send_keys(
        '123')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[5]/div[5]/div/input').send_keys(
        '123')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[6]/div[1]/div/input').send_keys(
        '123')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[6]/div[2]/div/input').send_keys(
        '123')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[1]/div/input').send_keys(
        'Основное')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[2]/button').click()
    mkb = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[2]/div[2]/div/div/input')
    mkb.send_keys('D00.0')
    mkb.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/button').click()

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[3]/div/input').send_keys(
        'Осложнения')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[4]/div/input').send_keys(
        'Сопутствующие')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[5]/button').click()
    mkb2 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[5]/div[2]/div/div/div[1]/div/input')
    mkb2.send_keys('D00.1')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[5]/div[2]/div/div/div[2]/div/ul/li[2]/ul/li[16]/ul/li[1]/ul/li[2]/a').click()
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[5]/div[2]/div/div/div[3]/button').click()

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[6]/div/input').send_keys(
        'осложнения2')

    prognosis_5 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[7]/div/div/div/div/div[1]/div[2]/div/input')
    prognosis_5.send_keys('благоприятный')
    prognosis_5.send_keys(Keys.ENTER)

    potential_5 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[8]/div/div/div/div/div[1]/div[2]/div/input')
    potential_5.send_keys('высокий')
    potential_5.send_keys(Keys.ENTER)

    rehabilitation_5 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[9]/div/div/div/div/div[1]/div[2]/div/input')
    rehabilitation_5.send_keys('благоприятный')
    rehabilitation_5.send_keys(Keys.ENTER)

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[3]/div[1]/div[2]/div/textarea').send_keys(
        'Рекоменации')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[3]/div[2]/div[2]/div/textarea').send_keys(
        'Рекоменации')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[3]/div[3]/div[2]/div/textarea').send_keys(
        'Рекоменации')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[3]/div[4]/div[2]/div/textarea').send_keys(
        'Рекоменации')

    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div[1]/div/label').click()
    chairman = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div[1]/div/div/div/div/div[1]/div[2]/div/input')
    chairman.click()
    chairman.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div[2]/button').click()
    member = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[4]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/input')
    member.send_keys('Т')
    time.sleep(0.5)
    member.send_keys(Keys.ENTER)

    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/div[1]/ul/li[6]').click()

    # (6)
    a = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div/div[2]/div/input')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'CryptoPro.zip')
    a.send_keys(file_path)

    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/div[1]/ul/li[7]').click()
    # (7)
    # Взаимодействие с всплывающим окном c помощью pywinauto для расширения CryptoPro
    app = Application().Connect(path="nmcades.exe")
    window = app.Dialog
    button = window[u'&Yes']
    button.Click()

finally:
    time.sleep(5000)
    browser.quit()
