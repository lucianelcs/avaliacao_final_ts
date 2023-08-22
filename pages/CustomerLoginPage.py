from selenium.webdriver.common.by import By

from pages.PageObject import PageObject
from pages.MenuPage import MenuPage


class CustomerLoginPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    id_dropdown_your_name = 'userSelect'
    your_name_dropdown_options = 'option[value="3"]'
    css_login_btn = 'button[type="submit"]'

    def __init__(self, driver):
        super(CustomerLoginPage, self).__init__(driver=driver)

    def click_dropdown_your_name(self):
        self.driver.find_element(By.ID, self.id_dropdown_your_name).click()

    def is_url_customer_login(self):
        return self.driver.current_url == self.url

    def select_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.your_name_dropdown_options).click()

    def click_on_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_login_btn).click()

