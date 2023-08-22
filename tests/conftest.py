import pytest

from pages.MenuPage import MenuPage


def pytest_addoption(parser):
    parser.addoption("--select_browser", default="chrome", help="Select browser")


@pytest.fixture
def select_browser(request):
    yield request.config.getoption("--select_browser").lower()


@pytest.fixture
def setup(select_browser):
    menu_page = MenuPage(browser=select_browser)
    yield menu_page
    menu_page.close()


@pytest.fixture
def run_all_browser(all_browser):
    menu_page = MenuPage(browser=all_browser)
    yield menu_page
    menu_page.close()
