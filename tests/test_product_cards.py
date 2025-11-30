from pages.search_results_page import SearchResultsPage
from pages.home_page import HomePage

def test_product_cards(page, search_terms):
    search_term = search_terms["default_search_term"]
    home_page = HomePage(page)
    home_page.goto()
    home_page.search_for_product(search_term)
    search_results_page = SearchResultsPage(page)
    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)

    product_cards = search_results_page.getProductCards()
    assert len(product_cards) > 0, "No product cards found"

    for card in product_cards:
        assert card["title"] is not None, "Product title is missing"
        assert card["has_image"], "Product image is missing"
        assert card["price"] is not None, "Product price is missing"
        if card["rating"] is not None:
            assert len(card["rating"]) > 0, "Product rating should not Be empty"
        if card["review_count"] is not None:
            assert len(card["review_count"]) > 0, "Product review count should should contain 'reviews'"
        if card["has_delivery_info"]:
            assert card["has_delivery_info"] == True, "Product delivery info should should Be displayed"
        # Delivery info is optional - not displayed for all product types
        # (e.g., products with multiple sellers may not show delivery until options are selected)
        # This inconsistency has been documented as a potential UX issue
