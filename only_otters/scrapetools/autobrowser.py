# std
import time
import threading
from pathlib import Path

# other
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


__folder__ = Path(__file__).parent


DRIVER = None
LOCK = threading.RLock()


def make_driver(headless: bool = True) -> webdriver:
    """
    Creates a selenium driver interface for Chrome.
    You need to install the chromedriver provided by
    Google and make it accessible through PATH to be
    able to use it.
    """
    opt = Options()
    if headless:
        opt.add_argument('--headless')
    opt.add_argument('lang=en')

    driver = webdriver.Chrome(__folder__ / 'chromedriver', chrome_options=opt)

    driver.set_window_size(1920, 1080)

    return driver


def fetch(url: str, wait: int = 0) -> bytes:
    """Fetch the content of the page through the puppet browser."""

    global DRIVER, LOCK

    with LOCK:

        if DRIVER is None:
            DRIVER = make_driver()

        DRIVER.get(url)

        if wait:
            time.sleep(wait)

        return DRIVER.page_source
