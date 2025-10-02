import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):

    parser.addoption("--browser_name",
                     action="store",
                     default="chrome",
                     help="Choose browser: chrome or firefox"
                    )
    
    parser.addoption("--language",
                    action="store",
                    default="en",
                    help="Choose language: ar, ca, cs, da, en, de, en-gb, el," \
                    "es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-cn"
                    )

@pytest.fixture(scope="function")
def driver(request):

    browser_name = request.config.getoption("browser_name") # параметр для cmd: задать браузер
    language = request.config.getoption("language")         # параметр для cmd: задать язык

    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"intl.accept_languages": language})
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1600,900")

    firefox_options = FirefoxOptions()
    firefox_options.set_preference("intl.accept_languages", language)

    if browser_name == "chrome":
        print("\nstart chrome driver for test..")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox driver for test..")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield driver
    print("\nquit driver..")
    driver.quit()


@pytest.fixture
def login(driver: webdriver.Chrome | webdriver.Firefox):
    driver.get("")