from pages.base_page import BasePage


class ProductDetailPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def get_product_title(self) -> str:
        title_locator = self.page.locator("span#productTitle").first
        return title_locator.text_content().strip()

    def get_product_price(self) -> str:
        price_selectors = [
            ".a-price .a-offscreen",
            "#priceblock_ourprice",
            "#priceblock_dealprice",
            ".a-price-whole",
        ]

        for selector in price_selectors:
            price_locator = self.page.locator(selector).first
            if price_locator.count() > 0:
                return price_locator.text_content().strip()

        return "Price not available"

    def get_product_availability(self) -> str:
        availability_locator = self.page.locator("#availability").first
        if availability_locator.count() > 0:
            return availability_locator.text_content().strip()
        return "Availability not shown"

    def is_product_detail_page(self) -> bool:
        # Check for product title and either Add to Cart or product images
        has_title = self.page.locator("#productTitle").count() > 0
        has_key_element = (
            self.has_add_to_cart_button()
            or self.page.locator("#landingImage, #imgBlkFront").count() > 0
        )
        return has_title and has_key_element

    def has_product_images(self) -> bool:
        # Checking for main image
        image_locator = self.page.locator("#landingImage, #imgBlkFront")
        return image_locator.count() > 0

    def has_add_to_cart_button(self) -> bool:
        add_to_cart_selectors = [
            "#add-to-cart-button",
            "input[name='submit.add-to-cart']",
            "#buy-now-button",
            "input[id*='add-to-cart']",
            "button:has-text('Add to Cart')",
            "input[value='Add to Cart']",
        ]

        for selector in add_to_cart_selectors:
            if self.page.locator(selector).count() > 0:
                return True

        return False
