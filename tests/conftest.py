import pytest
from selenium import webdriver
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
