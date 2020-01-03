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
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]').click()
    browser.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div[2]/button').click()
    # Проверяем на сохранение
    lastName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[1]/div/input').get_attribute('value')
    assert lastName == 'Фамилия', 'LastName does not match'
    firstName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[2]/div/input').get_attribute('value')
    assert firstName == 'Имя', 'FirstName does not match'
    PatrName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[3]/div/input').get_attribute('value')
    assert PatrName == 'Отчество', 'PatrName does not match'
    sex = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[4]/div/div/div/div/div[1]/div[1]')
    assert sex.text == 'Мужчина', 'Sex does not match'
    birthDate = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[5]/div/div/div/input').get_attribute(
        'value')
    assert birthDate == '25.07.1999', 'birthDate does not match'
    browser.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[2]/button').click()
    assert patient_successfully.text == 'Данные пациента успешно сохранены', 'Patient not registered'

finally:
    time.sleep(5)
    browser.quit()
