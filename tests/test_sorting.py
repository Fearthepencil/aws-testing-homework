from pages.search_results_page import SearchResultsPage
from pages.home_page import HomePage
from utils.price_parser import parse_price


# TC-010: Verify Sort by Price - Low to High
def test_sort_by_price_low_to_high(page, search_terms):
    search_term = search_terms["default_search_term"]
    home_page = HomePage(page)
    home_page.goto()
    home_page.search_for_product(search_term)
    search_results_page = SearchResultsPage(page)
    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)

    # Click on sort By Price - Low to High
    sorted_url = page.locator(
        '#s-result-sort-select option[value="price-asc-rank"]'
    ).get_attribute("data-url")
    page.goto(f"https://www.amazon.com{sorted_url}")

    # Wait for page to load
    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)
    page.wait_for_timeout(2000)

    product_cards = search_results_page.get_product_card_data()
    assert len(product_cards) > 0, "No product cards found"

    # Assert products are in ascending order
    current_price = 0
    for card in product_cards:
        parsed_price = parse_price(card["price"])
        if parsed_price == 0:
            continue
        if parsed_price < current_price:
            assert (
                False
            ), f"Product price is not in ascending order: {card['price']}, previous price was ${current_price}"
        current_price = parsed_price


# TC-011: Verify Sort by Price - High to Low
def test_sort_by_price_high_to_low(page, search_terms):
    search_term = search_terms["default_search_term"]
    home_page = HomePage(page)
    home_page.goto()
    home_page.search_for_product(search_term)
    search_results_page = SearchResultsPage(page)
    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)

    # Click on sort By Price - High to Low
    sorted_url = page.locator(
        '#s-result-sort-select option[value="price-desc-rank"]'
    ).get_attribute("data-url")
    page.goto(f"https://www.amazon.com{sorted_url}")

    # Wait for page to load
    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)
    page.wait_for_timeout(2000)

    product_cards = search_results_page.get_product_card_data()
    assert len(product_cards) > 0, "No product cards found"

    # Assert products are in descending order
    current_price = 100000.00
    for card in product_cards:
        parsed_price = parse_price(card["price"])
        if parsed_price == 0:
            continue
        if parsed_price > current_price:
            assert (
                False
            ), f"Product price is not in descending order: {card['price']}, previous price was ${current_price}"
        current_price = parsed_price
