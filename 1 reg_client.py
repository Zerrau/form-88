from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

link = "http://localhost:3000"
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
    # Создаем пациента
    add_patient = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/button').click()
    add_lastname = browser.find_element_by_xpath('//*[@id="lastName"]')
    add_lastname.send_keys('Фамилия')
    add_firsname = browser.find_element_by_xpath('//*[@id="firstName"]')
    add_firsname.send_keys('Имя')
    add_partname = browser.find_element_by_xpath('//*[@id="secondName"]')
    add_partname.send_keys('Отчество')
    #
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[4]/div/label').click()
    time.sleep(0.5)
    sex = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[4]/div/div/div/div/div[1]/div[2]/div/input')
    sex.send_keys('Мужчина')
    sex.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[5]/div[1]/label').click()
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[5]/div[1]/div[1]/div/input').send_keys(
        '25071999')
    bdate = browser.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[2]/button')
    bdate.send_keys(Keys.ENTER)
    # Ищем созданного пациента
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys('Фамилия')
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]').click()


finally:
    time.sleep(5)
    browser.quit()
