from selenium.webdriver.common.by import By

from pages.PageObject import PageObject
from pages.MenuPage import MenuPage


class WithDrawnPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    withdrawn_btn = '[ng-click="withdrawl()"]'
    withdrawn_amount_field = '[ng-model="amount"]'
    save_withdrawn_btn = 'button[type="submit"]'
    logout_btn = '[ng-click="byebye()"]'

    def __init__(self, browser):
        super(MenuPage, self).__init__(browser=browser)
        self.driver.get(self.url)

    def is_url_withdrawn_view(self):
        return self.driver.current_url == self.url

    def withdrawn_process(self):
        self.driver.find_element(By.CSS_SELECTOR, self.withdrawn_btn).click()
        self.driver.find_element(By.CSS_SELECTOR, self.withdrawn_amount_field).send_keys("500")
        self.driver.find_element(By.CSS_SELECTOR, self.save_withdrawn_btn).click()
