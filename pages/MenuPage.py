from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class MenuPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    css_customer_login_btn = '[ng-click="customer()"]'
    css_bank_manager_login_btn = '[ng-click="manager()"]'
    class_home_btn = '.home'

    def __init__(self, browser):
        super(MenuPage, self).__init__(browser=browser)
        self.driver.get(self.url)

    def is_main_url(self):
        return self.driver.current_url == self.url

    def open_customer_login_view(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_customer_login_btn).click()

    def open_bank_manager_login_view(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_bank_manager_login_btn).click()

    def back_home(self):
        self.driver.find_element(By.CLASS_NAME, self.class_home_btn)
