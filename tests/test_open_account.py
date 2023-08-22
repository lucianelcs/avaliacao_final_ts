import time

import pytest
from pages.OpenAccountPage import OpenAccountPage
from pages.BankManagerLoginPage import BankManagerLoginPage


class test_open_account:

    def test_open_account_to_customer(self, setup):
        menu_page = setup
        menu_page.open_bank_manager_login_view()
        assert menu_page.is_main_url, "Página errada!"
        manager_page = BankManagerLoginPage(driver=menu_page.driver)
        manager_page.open_new_account_view()
        open_new_account = OpenAccountPage(driver=menu_page.driver)
        open_new_account.open_account()
        time.sleep(3)
