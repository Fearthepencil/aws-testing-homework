"""
Amazon Product Detail Page Object
"""
from playwright.sync_api import Page
from loguru import logger
from pages.base_page import BasePage


class ProductDetailPage(BasePage):
    """Amazon product detail page object"""
    
    # Locators
    PRODUCT_TITLE = "#productTitle"
    PRODUCT_PRICE = ".a-price .a-offscreen"
    ADD_TO_CART_BUTTON = "#add-to-cart-button"
    PRODUCT_IMAGE = "#landingImage"
    BREADCRUMB = "#wayfinding-breadcrumbs_feature_div"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def is_loaded(self) -> bool:
        """Check if product detail page is loaded"""
        return self.is_element_visible(self.PRODUCT_TITLE, timeout=10000)
    
    def get_product_title(self) -> str:
        """Get product title"""
        try:
            title = self.get_text(self.PRODUCT_TITLE)
            logger.info(f"Product title: {title}")
            return title.strip()
        except Exception as e:
            logger.error(f"Could not get product title: {e}")
            return ""
    
    def has_add_to_cart_button(self) -> bool:
        """Check if 'Add to Cart' button is present"""
        return self.is_element_visible(self.ADD_TO_CART_BUTTON)
    
    def has_product_image(self) -> bool:
        """Check if product image is displayed"""
        return self.is_element_visible(self.PRODUCT_IMAGE)

