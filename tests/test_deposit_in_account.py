import time

import pytest

from pages.CustomerLoginPage import CustomerLoginPage
from pages.CustomerPage import CustomerPage
from pages.DepositPage import DepositPage
from pages.BankManagerLoginPage import BankManagerLoginPage


class test_deposit_in_account:

    def test_deposit_in_customer_account(self, setup):
        menu_page = setup
        menu_page.open_customer_login_view()
        assert menu_page.is_main_url, "Página errada!"
        customer_login_page = CustomerLoginPage(driver=menu_page.driver)
        customer_login_page.click_dropdown_your_name()
        customer_login_page.select_customer()
        customer_login_page.click_on_login()
        customer_page = CustomerPage(driver=menu_page.driver)
        customer_page.click_on_deposit_menu()
        deposit_page = DepositPage(driver=menu_page.driver)
        deposit_page.deposit_process()
        deposit_page.click_on_deposit_button()
        assert deposit_page.success_message, "Deposit Successful"




