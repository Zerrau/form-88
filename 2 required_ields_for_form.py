# Use Python 3.7.4 for pywinauto
import datetime
import os
import time

from pywinauto.application import Application
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

date = datetime.datetime.now()
date_now = date.strftime("%d%m%Y")
date_year = date.strftime("%Y")

# Добавляем расширение
executable_path = "chromedriver.exe"
os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension('CryptoPro.zip')  # Расширение CryptoPro

browser = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
browser.get("http://form88.vistamed.ru/")

#######################################
browser.implicitly_wait(5)
dbl_click = webdriver.ActionChains

try:
    # Логинимся
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[1]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[2]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[3]/button').click()
    # Создаем пациента
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/button').click()
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

    assert patient_successfully.text == 'Данные пациента успешно сохранены', 'Patient not registered'

    # Ищем созданного пациента
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(
        'Фамилия Имя Отчество')

    firstDate = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div/input')
    firstDate.send_keys('25.07.1999')
    firstDate.send_keys(Keys.ENTER)

    endDate = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/input')
    endDate.send_keys('25.07.1999')
    endDate.send_keys(Keys.ENTER)

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
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[4]/div[2]/div[2]/div[1]/label').click()
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
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[9]/div[2]/div[4]/div/div[1]/div/input').send_keys(
        date_now)
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
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[9]/div/input').send_keys(
        '111111')
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
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[8]/div/input').send_keys(
        '111111')
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/div[1]/ul/li[3]').click()
    # (3)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div/label').click()
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/div[1]/ul/li[4]').click()
    # (4)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[1]/div[2]/div[1]/div/label').click()
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[7]/div/input').send_keys(
        '111111')
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
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[7]/div[2]/div/textarea').send_keys(
        'A')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div[8]/div[2]/div/textarea').send_keys(
        'A')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[2]/button').click()
    mkb = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[2]/div[2]/div/div/input')
    mkb.send_keys('D00.0')
    mkb.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/button').click()
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
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/div[1]/ul/li[7]').click()

    # (7)
    # Взаимодействие с всплывающим окном c помощью pywinauto для расширения CryptoPro
    app = Application(backend="uia").Connect(path="nmcades.exe")
    window = app.Dialog
    button = window[u'&Yes']
    button.Click()
finally:
    time.sleep(1)
    browser.quit()
