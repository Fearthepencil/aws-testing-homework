from pages.home_page import HomePage

def test_amazon_search(page, search_terms):
    search_term = search_terms["default_search_term"]
    home_page = HomePage(page)
    home_page.goto()
    home_page.search_for_product(search_term)
    page.wait_for_timeout(5000)
    #check search results page
    assert "/s?" in page.url, f"Expected search results page, but got {page.url}"
    
    #check product count
    product_cards = page.locator('[data-component-type="s-search-result"]')
    assert product_cards.count() > 0, "No product cards found"
    assert product_cards.count() >= 10, f"Expected at least 10 product cards, but got {product_cards.count()}"

    #check first product title
    first_product_title = product_cards.first.locator('h2 span').text_content().lower()
    assert "wireless" in first_product_title or "mouse" in first_product_title
    
    #take screenshot
    home_page.take_screenshot(f"search_results_{search_term}")