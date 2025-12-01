from pages.search_results_page import SearchResultsPage
from pages.home_page import HomePage
from utils.price_parser import parse_price


# TC-009: Calculate Average Price on Page 1
def test_calculate_average_price_on_page_1(page, search_terms):
    search_term = search_terms["default_search_term"]
    home_page = HomePage(page)
    home_page.goto()
    home_page.search_for_product(search_term)
    search_results_page = SearchResultsPage(page)

    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)
    product_cards = search_results_page.get_product_card_data()
    assert len(product_cards) > 0, "No product cards found"
    total_price = 0.0
    for card in product_cards:
        total_price += parse_price(card["price"])
        print(f"Price: {card['price']} -> Parsed: {parse_price(card['price'])}")
        print(f"Total price: {total_price}")

    average_price = total_price / len(product_cards)
    assert (
        average_price > 0
    ), f"Average price should be greater than 0, got ${average_price:.2f}"
    assert (
        average_price < 200
    ), f"Average price ${average_price:.2f} exceeds reasonable maximum of $200"
