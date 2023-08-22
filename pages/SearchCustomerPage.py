import time

from selenium.webdriver.common.by import By

from pages.PageObject import PageObject
from pages.MenuPage import MenuPage


class SearchCustomerPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    css_search_customer = 'input[ng-model="searchCustomer"]'
    css_result_search_customer = 'tr td[class="ng-binding"]'
    delete_btn = '[ng-click="deleteCust(cust)"]'

    def __init__(self, driver):
        super(SearchCustomerPage, self).__init__(driver=driver)

    def is_url_search_customer(self):
        return self.driver.current_url == self.url

    def search_customer(self, customerName='Harry'):
        self.driver.find_element(By.CSS_SELECTOR, self.css_search_customer).send_keys(customerName)
        return self.driver.find_element(By.CSS_SELECTOR, self.css_result_search_customer).is_displayed()

    def delete_customer(self, customerName='Neville'):
        self.driver.find_element(By.CSS_SELECTOR, self.css_search_customer).send_keys(customerName)
        self.driver.find_element(By.CSS_SELECTOR, self.delete_btn).click()
