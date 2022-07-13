"""
These tests cover DuckDuckGo searches.
"""

from screenplay.pattern import Actor
from testlib.pages import SearchPage
from testlib.interactions import *


def test_duckduckgo_search(actor: Actor) -> None:
    
    actor.attempts_to(Load(SearchPage.URL))
    actor.attempts_to(SearchDuckDuckGo('panda'))
