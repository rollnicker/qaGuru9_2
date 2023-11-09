import random

import pytest
from selene.support.shared import browser
from selene import be, have

def test_search(set_window):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_negative_search(set_window):
    browser.element('[name="q"]').should(be.blank).type('1md9c ne4bc0 q 3 k').press_enter()
    browser.element('#extabar #result-stats').should(have.text('Результатов: примерно 0'))
    #browser.element('.uzjuFc[role = "heading"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))
