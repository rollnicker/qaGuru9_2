import pytest
from selene import browser


@pytest.fixture
def open_page():
    browser.open('https://google.com')

@pytest.fixture
def set_window(open_page):
    browser.config.window_height = 1280
    browser.config.window_width = 720