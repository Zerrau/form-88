from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import datetime

date_now = datetime.datetime.now()
date_now = date_now.strftime("%d%m%Y")

link = 'http://localhost:3000'
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)


class JavascriptExecutor(object):
    pass


try:
    # Логинимся
    login = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[1]/input')
    login.send_keys('user')
    passwrd = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[2]/input')
    passwrd.send_keys('user')
    into = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[3]/button').click()
    # Ищем созданного пациента
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys('Фамилия')
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
finally:
    time.sleep(5)
    browser.quit()
