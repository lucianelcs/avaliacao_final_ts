from selenium.webdriver.common.by import By

from pages.PageObject import PageObject
from pages.MenuPage import MenuPage


class DepositPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    deposit_btn = '[ng-click="deposit()"]'
    deposit_amount_field = '[ng-model="amount"]'
    save_deposit_btn = 'button[type="submit"]'
    success_message = '[ng-show="message"]'
    logout_btn = '[ng-click="byebye()"]'

    def __init__(self, driver):
        super(DepositPage, self).__init__(driver=driver)
        self.driver.get(self.url)

    def deposit_process(self, ):
        self.driver.find_element(By.CSS_SELECTOR, self.deposit_btn).click()
        self.driver.find_element(By.CSS_SELECTOR, self.deposit_amount_field).send_keys("1000")
        self.driver.find_element(By.CSS_SELECTOR, self.save_deposit_btn).click()

    def is_url_deposit_view(self):
        return self.driver.current_url == self.url

    def click_on_deposit_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.save_deposit_btn).click()

    def success_deposit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.success_message)
