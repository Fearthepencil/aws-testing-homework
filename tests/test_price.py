from pages.search_results_page import SearchResultsPage
from pages.home_page import HomePage
from utils.price_parser import parse_price


# TC-009: Calculate Average Price on First Three Pages
def test_calculate_average_price_on_first_three_pages(page, search_terms):
    search_term = search_terms["default_search_term"]
    home_page = HomePage(page)
    home_page.goto()
    home_page.search_for_product(search_term)
    search_results_page = SearchResultsPage(page)

    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)
    page.wait_for_timeout(2000)
    product_cards = search_results_page.get_product_card_data()
    assert len(product_cards) > 0, "No product cards found"

    prices = [parse_price(card["price"]) for card in product_cards]
    valid_prices = [p for p in prices if p > 0]
    assert len(valid_prices) > 0, "No valid prices found on Page 1"

    average_price_page_1 = sum(valid_prices) / len(valid_prices)
    assert (
        average_price_page_1 > 0
    ), f"Average price should be greater than 0, got ${average_price_page_1:.2f}"
    assert (
        average_price_page_1 < 200
    ), f"Average price ${average_price_page_1:.2f} exceeds reasonable maximum of $200"

    print(
        f"\nPAGE 1 - Products: {len(valid_prices)}, Average: ${average_price_page_1:.2f}"
    )

    # Navigate to Page 2
    page.wait_for_selector(".s-pagination-next", timeout=5000)
    search_results_page.go_next_page()
    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)
    page.wait_for_timeout(2000)
    product_cards = search_results_page.get_product_card_data()

    assert len(product_cards) > 0, "No product cards found on Page 2"
    prices = [parse_price(card["price"]) for card in product_cards]
    valid_prices = [p for p in prices if p > 0]
    assert len(valid_prices) > 0, "No valid prices found on Page 2"

    average_price_page_2 = sum(valid_prices) / len(valid_prices)
    assert (
        average_price_page_2 > 0
    ), f"Average price should be greater than 0, got ${average_price_page_2:.2f}"
    assert (
        average_price_page_2 < 200
    ), f"Average price ${average_price_page_2:.2f} exceeds reasonable maximum of $200"

    print(
        f"PAGE 2 - Products: {len(valid_prices)}, Average: ${average_price_page_2:.2f}"
    )

    # Navigate to Page 3
    page.wait_for_selector(".s-pagination-next", timeout=5000)
    search_results_page.go_next_page()
    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)
    page.wait_for_timeout(2000)
    product_cards = search_results_page.get_product_card_data()

    assert len(product_cards) > 0, "No product cards found on Page 3"
    prices = [parse_price(card["price"]) for card in product_cards]
    valid_prices = [p for p in prices if p > 0]
    assert len(valid_prices) > 0, "No valid prices found on Page 3"

    average_price_page_3 = sum(valid_prices) / len(valid_prices)
    assert (
        average_price_page_3 > 0
    ), f"Average price should be greater than 0, got ${average_price_page_3:.2f}"
    assert (
        average_price_page_3 < 200
    ), f"Average price ${average_price_page_3:.2f} exceeds reasonable maximum of $200"

    print(
        f"PAGE 3 - Products: {len(valid_prices)}, Average: ${average_price_page_3:.2f}\n"
    )
