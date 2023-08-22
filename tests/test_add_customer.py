import pytest
from pages.AddCustomerPage import AddCustomerPage
from pages.BankManagerLoginPage import BankManagerLoginPage


class test_add_customer:

    def test_add_new_customer(self, setup):
        menu_page = setup
        menu_page.open_bank_manager_login_view()
        assert menu_page.is_main_url, "Página errada!"
        manager_page = BankManagerLoginPage(driver=menu_page.driver)
        manager_page.open_add_customer_view()
        add_page = AddCustomerPage(driver=menu_page.driver)
        add_page.add_customer()
