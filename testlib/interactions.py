"""
This module contains web UI interactions for DuckDuckGo.
"""

from screenplay.pattern import Actor, Task, Question
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from testlib.pages import SearchPage, ResultPage


# Questions

class InputValueOf(Question[str]):
    def __init__(self, by: By, query: str) -> None:
        self.by = by
        self.query = query
    
    def request_as(self, actor: Actor) -> str:
        browser: WebDriver = actor.using('browser')
        input = browser.find_element(self.by, self.query)
        value = input.get_attribute('value')
        return value


class TextListFor(Question[list[str]]):
    def __init__(self, by: By, query: str) -> None:
        self.by = by
        self.query = query

    def request_as(self, actor: Actor) -> list[str]:
        browser: WebDriver = actor.using('browser')
        links = browser.find_elements(self.by, self.query)
        titles = [link.text for link in links]
        return titles


class Title(Question[str]):
    def request_as(self, actor: Actor) -> str:
        browser: WebDriver = actor.using('browser')
        return browser.title


# Tasks

class Load(Task):
    def __init__(self, url: str) -> None:
        self.url = url

    def perform_as(self, actor: Actor) -> None:
        browser: WebDriver = actor.using('browser')
        browser.get(self.url)


class SearchDuckDuckGoFor(Task):
    def __init__(self, phrase: str) -> None:
        self.phrase = phrase
    
    def perform_as(self, actor: Actor) -> None:
        browser: WebDriver = actor.using('browser')
        search_input = browser.find_element(*SearchPage.SEARCH_INPUT)
        search_input.send_keys(self.phrase + Keys.RETURN)


class VerifyResultPageInputValueIs(Task):
    def __init__(self, phrase: str) -> None:
        self.phrase = phrase

    def perform_as(self, actor: Actor) -> None:
        value = actor.asks_for(InputValueOf(*ResultPage.SEARCH_INPUT))
        assert value == self.phrase


class VerifyResultPageTitleContains(Task):
    def __init__(self, phrase: str) -> None:
        self.phrase = phrase

    def perform_as(self, actor: Actor) -> None:
        title = actor.asks_for(Title())
        assert self.phrase in title


class VerifyResultLinksInclude(Task):
    def __init__(self, phrase: str) -> None:
        self.phrase = phrase

    def perform_as(self, actor: Actor) -> None:
        titles = actor.asks_for(TextListFor(*ResultPage.RESULT_LINKS))
        matches = [t for t in titles if self.phrase.lower() in t.lower()]
        assert len(matches) > 0
