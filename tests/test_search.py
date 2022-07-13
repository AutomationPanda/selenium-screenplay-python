"""
These tests cover DuckDuckGo searches.
"""

import pytest

from screenplay.pattern import Actor
from testlib.interactions import *
from testlib.pages import SearchPage


@pytest.mark.parametrize('phrase', ['panda', 'python', 'parakeet'])
def test_duckduckgo_search(actor: Actor, phrase: str) -> None:
    
    # Arrange
    actor.attempts_to(Load(SearchPage.URL))

    # Act
    actor.attempts_to(SearchDuckDuckGoFor(phrase))

    # Assert
    actor.attempts_to(VerifyResultPageInputValueIs(phrase))
    actor.attempts_to(VerifyResultPageTitleContains(phrase))
    actor.attempts_to(VerifyResultLinksInclude(phrase))
