"""
This module contains shared fixtures.
"""

import json
import pytest

from screenplay.pattern import Actor
from selenium.webdriver import Chrome, ChromeOptions, Firefox
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def config(scope='session') -> dict:

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config: dict) -> WebDriver:

    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = Firefox()
    elif config['browser'] == 'Chrome':
        b = Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = ChromeOptions()
        opts.add_argument('headless')
        b = Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()


@pytest.fixture
def actor(browser: WebDriver) -> Actor:

    # Create the Actor
    a = Actor()

    # Add the Ability to use Selenium WebDriver
    a.can_use(browser=browser)

    # Return the Actor instance
    return a
