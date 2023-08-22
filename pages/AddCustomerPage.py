from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class AddCustomerPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    css_firstName = 'input[ng-model="fName"]'
    css_lastName = 'input[ng-model="lName"]'
    css_postCode = 'input[ng-model="postCd"]'
    save_customer_btn = 'button[type="submit"]'

    def __init__(self, driver):
        super(AddCustomerPage, self).__init__(driver=driver)

    def click_save_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.save_customer_btn).click()

    def add_customer(self, firstName='testeFirst', lastName='testeLast', postCode='37540000'):
        self.driver.find_element(By.CSS_SELECTOR, self.css_firstName).send_keys(firstName)
        self.driver.find_element(By.CSS_SELECTOR, self.css_lastName).send_keys(lastName)
        self.driver.find_element(By.CSS_SELECTOR, self.css_postCode).send_keys(postCode)
        self.click_save_customer()


