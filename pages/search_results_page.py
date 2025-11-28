"""
Amazon Search Results Page Object
"""
from typing import List, Dict
from playwright.sync_api import Page
from loguru import logger
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    """Amazon search results page object"""
    
    # Locators
    RESULTS_CONTAINER = "[data-component-type='s-search-result']"
    PRODUCT_TITLE = "h2 a span"
    PRODUCT_PRICE_WHOLE = ".a-price-whole"
    PRODUCT_PRICE_FRACTION = ".a-price-fraction"
    PRODUCT_RATING = ".a-icon-star-small span"
    PRODUCT_LINK = "h2 a"
    PAGINATION_NEXT = ".s-pagination-next"
    PAGINATION_CURRENT = ".s-pagination-item.s-pagination-selected"
    NO_RESULTS_MESSAGE = ".s-no-results-search-message"
    RESULT_COUNT = ".s-result-count"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def has_results(self) -> bool:
        """Check if search results are displayed"""
        return self.is_element_visible(self.RESULTS_CONTAINER, timeout=10000)
    
    def get_product_count(self) -> int:
        """Get number of products displayed on current page"""
        products = self.page.locator(self.RESULTS_CONTAINER).all()
        count = len(products)
        logger.info(f"Found {count} products on current page")
        return count
    
    def get_current_page_number(self) -> int:
        """Get current pagination page number"""
        try:
            page_num = self.get_text(self.PAGINATION_CURRENT)
            return int(page_num)
        except Exception as e:
            logger.warning(f"Could not get page number: {e}")
            return 1
    
    def go_to_next_page(self):
        """Navigate to next page of results"""
        logger.info(f"Navigating to next page")
        if self.is_element_visible(self.PAGINATION_NEXT):
            self.click(self.PAGINATION_NEXT)
            self.wait_for_load_state()
        else:
            logger.warning("Next page button not found")
    
    def get_all_product_prices(self) -> List[float]:
        """
        Extract all product prices from current page
        
        Returns:
            List of prices as floats
        """
        prices = []
        products = self.page.locator(self.RESULTS_CONTAINER).all()
        
        for product in products:
            try:
                # Try to get price (whole + fraction)
                whole = product.locator(self.PRODUCT_PRICE_WHOLE).first
                fraction = product.locator(self.PRODUCT_PRICE_FRACTION).first
                
                if whole.is_visible():
                    whole_text = whole.inner_text().replace(",", "").replace("$", "").strip()
                    fraction_text = "00"
                    
                    if fraction.is_visible():
                        fraction_text = fraction.inner_text().strip()
                    
                    price = float(f"{whole_text}.{fraction_text}")
                    prices.append(price)
                    logger.debug(f"Extracted price: ${price:.2f}")
            except Exception as e:
                logger.debug(f"Could not extract price from product: {e}")
                continue
        
        logger.info(f"Extracted {len(prices)} prices from page")
        return prices
    
    def get_product_details(self, index: int = 0) -> Dict[str, str]:
        """
        Get details of a specific product by index
        
        Args:
            index: Product index (0-based)
            
        Returns:
            Dictionary with product details
        """
        products = self.page.locator(self.RESULTS_CONTAINER).all()
        
        if index >= len(products):
            logger.error(f"Product index {index} out of range")
            return {}
        
        product = products[index]
        details = {}
        
        try:
            # Get title
            title_elem = product.locator(self.PRODUCT_TITLE).first
            if title_elem.is_visible():
                details['title'] = title_elem.inner_text()
            
            # Get price
            whole = product.locator(self.PRODUCT_PRICE_WHOLE).first
            if whole.is_visible():
                whole_text = whole.inner_text().replace(",", "").replace("$", "").strip()
                fraction = product.locator(self.PRODUCT_PRICE_FRACTION).first
                fraction_text = "00"
                if fraction.is_visible():
                    fraction_text = fraction.inner_text().strip()
                details['price'] = f"${whole_text}.{fraction_text}"
            
            # Get rating
            rating_elem = product.locator(self.PRODUCT_RATING).first
            if rating_elem.is_visible():
                rating_text = rating_elem.get_attribute("aria-label")
                details['rating'] = rating_text
            
            logger.info(f"Product {index} details: {details}")
            
        except Exception as e:
            logger.error(f"Error getting product details: {e}")
        
        return details
    
    def click_product(self, index: int = 0):
        """
        Click on a product to open detail page
        
        Args:
            index: Product index (0-based)
        """
        products = self.page.locator(self.RESULTS_CONTAINER).all()
        
        if index >= len(products):
            logger.error(f"Product index {index} out of range")
            return
        
        product = products[index]
        link = product.locator(self.PRODUCT_LINK).first
        
        if link.is_visible():
            logger.info(f"Clicking product at index {index}")
            link.click()
            self.wait_for_load_state()
    
    def has_no_results(self) -> bool:
        """Check if 'no results' message is displayed"""
        return self.is_element_visible(self.NO_RESULTS_MESSAGE)
    
    def get_result_count_text(self) -> str:
        """Get the result count text (e.g., '1-16 of over 10,000 results')"""
        try:
            return self.get_text(self.RESULT_COUNT)
        except Exception:
            return ""

