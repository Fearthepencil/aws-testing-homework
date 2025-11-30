import pytest
import json
from playwright.sync_api import sync_playwright, Browser

@pytest.fixture(scope="session")
def browser():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser):

    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
    )
    page = context.new_page()
    
    yield page

    context.close()

@pytest.fixture(scope="session")
def search_terms():
    with open("test_data/search_terms.json", "r") as f:
        return json.load(f)