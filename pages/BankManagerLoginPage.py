from selenium.webdriver.common.by import By

from pages.PageObject import PageObject
from pages.MenuPage import MenuPage


class BankManagerLoginPage(MenuPage):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    css_add_customer_btn = '[ng-click="addCust()"]'
    css_open_account_btn = '[ng-click="openAccount()"]'
    css_customers_btn = '[ng-click="showCust()"]'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)
        self.driver.get(self.url)

    def is_url_bank_manager_login(self):
        return self.driver.current_url == self.url

    def open_add_customer_view(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_add_customer_btn).click()

    def open_new_account_view(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_open_account_btn).click()

    def search_customer_view(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_customers_btn).click()
