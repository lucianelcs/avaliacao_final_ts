from selenium.webdriver.common.by import By

from pages.PageObject import PageObject

class WithDrawlPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    withdrawl_btn = '[ng-click="withdrawl()"]'
    withdrawl_amount_field = '[ng-model="amount"]'
    save_withdrawl_btn = 'button[type="submit"]'
    success_message = '[ng-show="message"]'
    logout_btn = '[ng-click="byebye()"]'

    def __init__(self, driver):
        super(WithDrawlPage, self).__init__(driver=driver)
        self.driver.get(self.url)

    def withdrawl_process(self, ):
        self.driver.find_element(By.CSS_SELECTOR, self.withdrawl_btn).click()
        self.driver.find_element(By.CSS_SELECTOR, self.withdrawl_amount_field).send_keys("1000")
        self.driver.find_element(By.CSS_SELECTOR, self.save_withdrawl_btn).click()

    def is_url_withdrawl_view(self):
        return self.driver.current_url == self.url

    def click_on_withdrawl_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.save_withdrawl_btn).click()

    def success_withdrawl(self):
        self.driver.find_element(By.CSS_SELECTOR, self.success_message)
