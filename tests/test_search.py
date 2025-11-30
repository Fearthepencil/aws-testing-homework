from pages.home_page import HomePage


# TC-001: Valid product search returns results
def test_amazon_search(page, search_terms):
    search_term = search_terms["default_search_term"]
    home_page = HomePage(page)
    home_page.goto()
    home_page.search_for_product(search_term)
    # check search results page
    assert (
        "/s" in page.url and "wireless+mouse" in page.url
    ), f"Expected search results page, but got {page.url}"

    # check product count
    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)
    product_cards = page.locator('[data-component-type="s-search-result"]')
    assert product_cards.count() > 0, "No product cards found"
    assert (
        product_cards.count() >= 10
    ), f"Expected at least 10 product cards, but got {product_cards.count()}"

    # check first product title
    first_product_title = product_cards.first.locator("h2 span").text_content().lower()
    assert "wireless" in first_product_title or "mouse" in first_product_title

    # take screenshot
    home_page.take_screenshot(f"search_results_{search_term}")


# TC-002: Search with multiple keywords
def test_amazon_search_with_multiple_keywords(page, search_terms):
    search_term = search_terms["alternative_search_terms"][0]
    home_page = HomePage(page)
    home_page.goto()
    home_page.search_for_product(search_term)

    # check search results page
    assert (
        "/s" in page.url and "gaming+keyboard+rgb" in page.url
    ), f"Expected search results page, but got {page.url}"

    # check product count
    # Wait for products to load, then get all of them
    page.wait_for_selector('[data-component-type="s-search-result"]', timeout=5000)
    product_cards = page.locator('[data-component-type="s-search-result"]')
    assert product_cards.count() > 0, "No product cards found"
