# selenium-screenplay-python

This repository contains an example project
using [Selenium WebDriver](https://www.selenium.dev/)
with the [Screenplay Pattern in Python](https://github.com/AutomationPanda/screenplay).

To set up a [virtual environment](https://docs.python.org/3/tutorial/venv.html)
and install project dependencies, run the following on macOS and Linux:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For Windows, run:

```
python3 -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

You must also install [WebDriver executables](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)
for [ChromeDriver (for Chrome)](https://chromedriver.chromium.org/)
and [geckodriver (for Firefox)](https://github.com/mozilla/geckodriver).
They must be on the system PATH variable and thus callable from the command line.

To set the target browser, edit [`config.json`](config.json).
Supported options for `"browser"` include:

* `"Chrome"`
* `"Firefox"`
* `"Headless Chrome"`

To execute tests, run `python -m pytest tests` from the project root directory.
