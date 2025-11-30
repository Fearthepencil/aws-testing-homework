from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def goNextPage(self):
        self.page.locator(".s-pagination-next").click()

    def currentPageNumber(self) -> str:
        current_page = self.page.locator(".s-pagination-selected").text_content()
        return current_page.strip()

    def getProductTitles(self) -> list[str]:
        product_cards = self.page.locator('[data-component-type="s-search-result"]')
        titles = []
        for i in range(product_cards.count()):
            title = product_cards.nth(i).locator("h2 span").text_content()
            titles.append(title.strip())
        return titles

    def getProductCards(self) -> list[dict]:
        product_cards = self.page.locator('[data-component-type="s-search-result"]')
        cards = []
        for i in range(product_cards.count()):
            product_card = product_cards.nth(i)

            # Title
            title_locator = product_card.locator("h2 span")
            title = (
                title_locator.text_content().strip()
                if title_locator.count() > 0
                else None
            )

            # Image
            image_locator = product_card.locator("img.s-image")
            has_image = image_locator.count() > 0

            # Price
            price_locator = product_card.locator(".a-offscreen").first
            price = (
                price_locator.text_content().strip()
                if price_locator.count() > 0
                else "Not available"
            )

            # Rating
            rating_locator = product_card.locator(".a-icon-alt")
            rating = (
                rating_locator.text_content().strip()
                if rating_locator.count() > 0
                else None
            )

            # Review count
            review_locator = product_card.locator('[aria-label*="ratings"]')
            review_count = (
                review_locator.get_attribute("aria-label")
                if review_locator.count() > 0
                else None
            )

            # Delivery info
            delivery_locator = product_card.locator('[data-cy="delivery-block"]')
            has_delivery_info = delivery_locator.count() > 0

            card = {
                "title": title,
                "has_image": has_image,
                "price": price,
                "rating": rating,
                "review_count": review_count,
                "has_delivery_info": has_delivery_info,
            }
            cards.append(card)
        return cards
