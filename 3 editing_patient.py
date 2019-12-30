import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

link = 'http://localhost:3000/'
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

try:
    # Логинимся
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[1]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[2]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[3]/button').click()
    # Ищем созданного ранее пациента
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys('Фамилия')
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]').click()
    browser.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div[2]/button').click()
    # Изменяем данные
    edit_lastName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[1]/div/input')
    edit_lastName.click()
    edit_lastName.send_keys(Keys.CONTROL + "a")
    edit_lastName.send_keys(Keys.DELETE)
    edit_lastName.send_keys('Фамилия 2')
    #
    edit_lastName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[2]/div/input')
    edit_lastName.click()
    edit_lastName.send_keys(Keys.CONTROL + "a")
    edit_lastName.send_keys(Keys.DELETE)
    edit_lastName.send_keys('Имя 2')
    #
    edit_lastName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[3]/div/input')
    edit_lastName.click()
    edit_lastName.send_keys(Keys.CONTROL + "a")
    edit_lastName.send_keys(Keys.DELETE)
    edit_lastName.send_keys('Отчество 2')
    #
    12.12.2012
    #
    #


finally:
    time.sleep(5)
    browser.quit()
