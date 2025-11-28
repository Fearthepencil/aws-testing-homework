"""
Pytest configuration and fixtures
"""
import pytest
from playwright.sync_api import Page, Browser
from pages.home_page import AmazonHomePage
from pages.search_results_page import SearchResultsPage
from pages.product_detail_page import ProductDetailPage
from utils.logger import logger


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }


@pytest.fixture(scope="function")
def page(page: Page):
    """
    Page fixture with extended timeout
    """
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(30000)
    yield page


@pytest.fixture(scope="function")
def amazon_home(page: Page) -> AmazonHomePage:
    """
    Amazon homepage page object fixture
    """
    logger.info("Initializing Amazon Home Page")
    return AmazonHomePage(page)


@pytest.fixture(scope="function")
def search_results(page: Page) -> SearchResultsPage:
    """
    Search results page object fixture
    """
    logger.info("Initializing Search Results Page")
    return SearchResultsPage(page)


@pytest.fixture(scope="function")
def product_detail(page: Page) -> ProductDetailPage:
    """
    Product detail page object fixture
    """
    logger.info("Initializing Product Detail Page")
    return ProductDetailPage(page)


@pytest.fixture(scope="function")
def search_term():
    """
    Default search term for tests
    """
    return "wireless mouse"


def pytest_configure(config):
    """Configure pytest markers"""
    config.addinivalue_line(
        "markers", "smoke: Quick smoke tests"
    )
    config.addinivalue_line(
        "markers", "functional: Functional test cases"
    )
    config.addinivalue_line(
        "markers", "pagination: Pagination-related tests"
    )
    config.addinivalue_line(
        "markers", "price_calculation: Price calculation tests"
    )

