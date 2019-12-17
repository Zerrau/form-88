from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

link = 'http://localhost:3000'
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

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
    med = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div/input')
    med.send_keys(
        'Санкт')  # Санкт-Петербургское государственное бюджетное учреждение здравоохранения "Консультативно-диагностическая поликлиника №1 Приморского района"
    med.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/form/div/div[2]/div/fieldset/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/input').send_keys(
        '1234567890')

finally:
    time.sleep(5)
    browser.quit()
