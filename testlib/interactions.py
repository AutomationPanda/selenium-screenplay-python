"""
This module contains web UI interactions for DuckDuckGo.
"""

from screenplay.pattern import Actor, Task
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from testlib.pages import SearchPage, ResultPage


class Load(Task):
    def __init__(self, url: str) -> None:
        self.url = url

    def perform_as(self, actor: Actor) -> None:
        browser: WebDriver = actor.using('browser')
        browser.get(self.url)


class SearchDuckDuckGo(Task):
    def __init__(self, phrase: str) -> None:
        self.phrase = phrase
    
    def perform_as(self, actor: Actor) -> None:
        browser: WebDriver = actor.using('browser')
        search_input = browser.find_element(*SearchPage.SEARCH_INPUT)
        search_input.send_keys(self.phrase + Keys.RETURN)