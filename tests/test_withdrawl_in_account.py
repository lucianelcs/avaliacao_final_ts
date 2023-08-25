
import pytest

from pages.CustomerLoginPage import CustomerLoginPage
from pages.CustomerPage import CustomerPage
from pages.WithDrawlPage import WithDrawlPage


class test_withdrawl_in_account:
    def test_withdrawl_in_customer_account(self, setup):
        menu_page = setup
        menu_page.open_customer_login_view()
        assert menu_page.is_main_url, "Página errada!"
        customer_login_page = CustomerLoginPage(driver=menu_page.driver)
        customer_login_page.click_dropdown_your_name()
        customer_login_page.select_customer()
        customer_login_page.click_on_login()
        customer_page = CustomerPage(driver=menu_page.driver)
        customer_page.click_on_withdrawl_menu()
        withdrawl_page = WithDrawlPage(driver=menu_page.driver)
        withdrawl_page.withdrawl_process()
        withdrawl_page.click_on_withdrawl_button()
        assert withdrawl_page.success_message, "Transaction successful"
