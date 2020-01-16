import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

link = "http://form88.vistamed.ru/"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

try:
    # Логинимся
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[1]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[2]/input').send_keys('user')
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[3]/button').click()

    # Переход по кнопке Вперед
    Next = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[3]/button')
    Next.click()
    patient = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[1]/div[1]').text
    assert patient == 'Список пациентов', 'Error next page'
    time.sleep(1)
    Next.click()
    patient = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[1]/div[1]').text
    assert patient == 'Список пациентов', 'Error next page'

    # Переход по кнопке Назад
    back = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/button')
    back.click()
    patient = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[1]/div[1]').text
    assert patient == 'Список пациентов', 'Error back page'
    time.sleep(1)
    back.click()
    patient = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[1]/div[1]').text
    assert patient == 'Список пациентов', 'Error back page'

    # Переход на последнюю страницу
    page_99 = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/span[1]/div/input')
    page_99.send_keys(Keys.CONTROL + 'a')
    page_99.send_keys(Keys.DELETE)
    page_99.send_keys('99')
    page_99.send_keys(Keys.ENTER)
    patient = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[1]/div[1]').text
    assert patient == 'Список пациентов', 'Error last page'

    # Переход на первую страницу
    page_0 = browser.find_element_by_xpath(
        '/html/body/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/span[1]/div/input')
    page_0.send_keys(Keys.CONTROL + 'a')
    page_0.send_keys(Keys.DELETE)
    page_0.send_keys('0')
    page_0.send_keys(Keys.ENTER)
    patient = browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[1]/div[1]').text
    assert patient == 'Список пациентов', 'Error first page'
finally:
    time.sleep(1)
    browser.quit()
