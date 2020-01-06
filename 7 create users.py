import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

link = 'http://localhost:3000/#/admin'
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

try:
    # Логинимся
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[1]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[2]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[3]/button').click()

    # Создаем пользователя Организация
    browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/button[3]').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div/div/div[3]/div/div[2]/div/form/div[1]/div[1]/div/input').send_keys(
        'Организация')
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div/div/div[3]/div/div[2]/div/form/div[1]/div[2]/div/input').send_keys(
        'Организация')
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div/div/div[3]/div/div[2]/div/form/div[1]/div[3]/div/input').send_keys(
        'Организация')

    organization = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div/div/div[3]/div/div[2]/div/form/div[1]/div[5]/div/div/div/div/div[1]/div[2]/div/input')
    organization.send_keys('спб')
    time.sleep(0.5)
    organization.send_keys(Keys.ENTER)

    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div/div/div[3]/div/div[2]/div/form/div[1]/div[8]/div/input').send_keys(
        'Организация')
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div/div/div[3]/div/div[2]/div/form/div[1]/div[9]/div/div/input').send_keys(
        'Организация')
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div/div/div[3]/div/div[2]/div/form/div[1]/div[10]/div/div/input').send_keys(
        'Организация')
    browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[3]/div/div[2]/div/form/div[2]/button').click()

    save_1 = browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div').text
    assert save_1 == 'Данные пользователя успешно сохранены', 'User not registered'

finally:
    time.sleep(2)
    browser.quit()
