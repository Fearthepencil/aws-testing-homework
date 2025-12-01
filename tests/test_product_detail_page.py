from pages.search_results_page import SearchResultsPage
from pages.product_detail_page import ProductDetailPage
from pages.home_page import HomePage


# TC-008: Click Product Opens Detail Page
def test_click_product_opens_detail_page(page, search_terms):
    search_term = search_terms["default_search_term"]
    home_page = HomePage(page)
    home_page.goto()
    home_page.search_for_product(search_term)
    search_results_page = SearchResultsPage(page)
    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)

    product_cards = search_results_page.get_product_card_data()
    assert len(product_cards) > 0, "No product cards found"
    product_card = product_cards[0]

    # click on the first product card
    page.locator('[data-component-type="s-search-result"]').first.locator(
        "a h2,h2 a"
    ).click()
    product_detail_page = ProductDetailPage(page)
    page.wait_for_url("**/dp/**", timeout=5000)

    # assertions - Product detail page
    assert "/dp/" in page.url, "Expected product detail page URL"
    assert product_detail_page.is_product_detail_page(), "Product detail page not found"
    assert product_detail_page.has_product_images(), "Product images not found"
    assert product_detail_page.has_add_to_cart_button(), "Add to Cart button not found"
    assert (
        product_detail_page.get_product_title() == product_card["title"]
    ), "Product title does not match"
    assert (
        product_detail_page.get_product_price() == product_card["price"]
    ), "Product price does not match"

    product_detail_page.take_screenshot(f"product_detail_page_{product_card['title']}")
