import time

from selenium.webdriver.common.by import By

from pages.PageObject import PageObject
from pages.MenuPage import MenuPage


class OpenAccountPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
    id_customerName_dropdown = 'userSelect'
    customerName_dropdown_options = 'option.ng-binding[value="1"]'
    id_currency_dropdown = 'currency'
    currency_dropdown_options = 'option[value="Dollar"]'
    process_btn = 'button[type="submit"]'

    def __init__(self, driver):
        super(OpenAccountPage, self).__init__(driver=driver)

    def is_url_open_account(self):
        return self.driver.current_url == self.url

    def open_account(self):
        self.driver.find_element(By.ID, self.id_customerName_dropdown).click()
        self.driver.find_element(By.CSS_SELECTOR, self.customerName_dropdown_options).click()
        self.driver.find_element(By.ID, self.id_currency_dropdown).click()
        self.driver.find_element(By.CSS_SELECTOR, self.currency_dropdown_options).click()
        self.driver.find_element(By.CSS_SELECTOR, self.process_btn).click()
