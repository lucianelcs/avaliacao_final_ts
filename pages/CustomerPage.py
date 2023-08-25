from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CustomerPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    deposit_menu = '[ng-click="deposit()"]'
    withdrawl_menu = '[ng-click="withdrawl()"]'
    your_name_dropdown_options = 'option[value="3"]'
    css_login_btn = 'button[type="submit"]'

    def __init__(self, driver):
        super(CustomerPage, self).__init__(driver=driver)
        self.driver.get(self.url)

    def is_url_customer_view(self):
        return self.driver.current_url == self.url

    def click_on_deposit_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.deposit_menu).click()

    def click_on_withdrawl_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.withdrawl_menu).click()
