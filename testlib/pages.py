"""
This module contains page classes for DuckDuckGo pages,
which provide locators for interactions.
"""

from selenium.webdriver.common.by import By


class SearchPage:
    URL = 'https://www.duckduckgo.com'
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')


class ResultPage:
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')
