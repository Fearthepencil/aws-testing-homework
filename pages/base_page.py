"""
Base Page Object - Common functionality for all pages
"""
from playwright.sync_api import Page, expect
from loguru import logger


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.amazon.com"
    
    def goto(self, path: str = ""):
        """Navigate to a specific path"""
        url = f"{self.base_url}{path}"
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)
    
    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()
    
    def wait_for_load_state(self, state: str = "networkidle"):
        """Wait for page to reach a specific load state"""
        self.page.wait_for_load_state(state)
    
    def take_screenshot(self, name: str):
        """Take a screenshot and save it"""
        screenshot_path = f"screenshots/{name}.png"
        self.page.screenshot(path=screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path
    
    def is_element_visible(self, selector: str, timeout: int = 5000) -> bool:
        """Check if element is visible"""
        try:
            self.page.wait_for_selector(selector, timeout=timeout, state="visible")
            return True
        except Exception:
            return False
    
    def click(self, selector: str):
        """Click an element"""
        logger.debug(f"Clicking element: {selector}")
        self.page.click(selector)
    
    def fill(self, selector: str, text: str):
        """Fill input field with text"""
        logger.debug(f"Filling '{selector}' with: {text}")
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        """Get text content of an element"""
        return self.page.locator(selector).inner_text()
    
    def get_attribute(self, selector: str, attribute: str) -> str:
        """Get attribute value of an element"""
        return self.page.locator(selector).get_attribute(attribute)

