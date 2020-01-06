import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

link = "http://localhost:3000"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

try:
    # Логинимся
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[1]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[2]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[3]/button').click()

    # Выходим
    browser.find_element_by_xpath('/html/body/div/div/nav/div[2]/button').click()
    into = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/h2').text
    assert into == 'Вход в систему', 'Error exit'

    # Снова логинися
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[1]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[2]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[3]/button').click()
    userName = browser.find_element_by_xpath('/html/body/div/div/nav/div[2]/div').text
    assert userName == 'User User', 'Login failed'
finally:
    browser.quit()
