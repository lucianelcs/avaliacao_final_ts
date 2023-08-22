import time

import pytest
from pages.SearchCustomerPage import SearchCustomerPage
from pages.BankManagerLoginPage import BankManagerLoginPage


class test_add_customer:

    def test_search_customer(self, setup):
        menu_page = setup
        menu_page.open_bank_manager_login_view()
        assert menu_page.is_main_url, "Página errada!"
        manager_page = BankManagerLoginPage(driver=menu_page.driver)
        manager_page.search_customer_view()
        search_page = SearchCustomerPage(driver=menu_page.driver)
        search_page.search_customer()
