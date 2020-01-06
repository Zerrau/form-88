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
    # Ищем созданного ранее пациента
    browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(
        'Фамилия Имя Отчество')
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
    patient_successfully = patient_successfully.text
    assert patient_successfully == 'Данные пациента успешно сохранены', 'Patient not changed'

    # Проверяем на сохранение
    FIO = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/input')
    FIO.send_keys(Keys.CONTROL + "a")
    FIO.send_keys(Keys.DELETE)
    browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(
        'Фамилия 2 Имя 2 Отчество 2')

    firstDate = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div/input')
    firstDate.send_keys('12.12.2012')
    firstDate.send_keys(Keys.ENTER)

    endDate = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/input')
    endDate.send_keys('12.12.2012')
    endDate.send_keys(Keys.ENTER)

    # Блок проверки на правильное сохранение данных
    browser.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div[2]/button').click()
    lastName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[1]/div/input').get_attribute('value')
    assert lastName == 'Фамилия 2', 'LastName does not match'
    firstName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[2]/div/input').get_attribute('value')
    assert firstName == 'Имя 2', 'FirstName does not match'
    patrName = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[3]/div/input').get_attribute('value')
    assert patrName == 'Отчество 2', 'PatrName does not match'
    sex = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[4]/div/div/div/div/div[1]/div[1]')
    assert sex.text == 'Женщина', 'Sex does not match'
    birthDate = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[1]/fieldset/div[5]/div/div/div/input').get_attribute(
        'value')
    assert birthDate == '12.12.2012', 'birthDate does not match'
    browser.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div[2]/div/form/div[2]/button').click()
    assert patient_successfully == 'Данные пациента успешно сохранены', 'Patient not registered'
finally:
    time.sleep(5)
    browser.quit()
