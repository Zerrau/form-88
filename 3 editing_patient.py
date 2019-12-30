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
    edit_firstName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[2]/div/input')
    edit_firstName.click()
    edit_firstName.send_keys(Keys.CONTROL + "a")
    edit_firstName.send_keys(Keys.DELETE)
    edit_firstName.send_keys('Имя 2')
    #
    edit_parthName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[3]/div/input')
    edit_parthName.click()
    edit_parthName.send_keys(Keys.CONTROL + "a")
    edit_parthName.send_keys(Keys.DELETE)
    edit_parthName.send_keys('Отчество 2')
    #
    sex = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[4]/div/div/div/div/div[1]/div[2]/div/input')
    sex.send_keys('Женщина')
    sex.send_keys(Keys.ENTER)

    b_dateEdit = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[5]/div[1]/div[1]/div/input')
    b_dateEdit.click()
    b_dateEdit.send_keys(Keys.CONTROL + "a")
    b_dateEdit.send_keys(Keys.DELETE)
    b_dateEdit.send_keys('12122012')
    b_date = browser.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[2]/button')
    b_date.send_keys(Keys.ENTER)
    patient_successfully = browser.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div')

    assert patient_successfully.text == 'Данные пациента успешно сохранены', 'Patient not changed'
finally:
    time.sleep(5)
    browser.quit()
