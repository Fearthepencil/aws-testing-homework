"""
Amazon Home Page Object
"""
from playwright.sync_api import Page
from loguru import logger
from pages.base_page import BasePage


class AmazonHomePage(BasePage):
    """Amazon homepage page object"""
    
    # Locators
    SEARCH_INPUT = "#twotabsearchtextbox"
    SEARCH_BUTTON = "#nav-search-submit-button"
    AMAZON_LOGO = "#nav-logo-sprites"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def open(self):
        """Open Amazon homepage"""
        logger.info("Opening Amazon homepage")
        self.goto("/")
        self.wait_for_load_state()
    
    def search_for(self, search_term: str):
        """
        Search for a product
        
        Args:
            search_term: The product search term
        """
        logger.info(f"Searching for: {search_term}")
        self.fill(self.SEARCH_INPUT, search_term)
        self.click(self.SEARCH_BUTTON)
        self.wait_for_load_state()
    
    def is_loaded(self) -> bool:
        """Check if homepage is loaded"""
        return self.is_element_visible(self.SEARCH_INPUT) and \
               self.is_element_visible(self.AMAZON_LOGO)
    
    def get_search_input_value(self) -> str:
        """Get current value in search input"""
        return self.get_attribute(self.SEARCH_INPUT, "value")

