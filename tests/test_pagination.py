from pages.search_results_page import SearchResultsPage
from pages.home_page import HomePage

def test_pagination(page, search_terms):
    search_term = search_terms["default_search_term"]
    home_page = HomePage(page)  
    home_page.goto()
    home_page.search_for_product(search_term)
    search_results_page = SearchResultsPage(page)

    #click on next page
    page.wait_for_selector('.s-pagination-next', timeout=5000)
    product_titles = search_results_page.getProductTitles()
    search_results_page.goNextPage()
    
    #check page number and URL
    assert search_results_page.currentPageNumber() == "2", f"Expected page 2, but got {search_results_page.currentPageNumber()}"
    assert "page=2" in page.url, f"Expected page=2 in URL, but got {page.url}"
    
    #check product titles
    assert search_results_page.getProductTitles() != product_titles, f"Expected different product titles, but got {search_results_page.getProductTitles()}"

    #check search term
    search_box = page.locator("#twotabsearchtextbox, #nav-bb-search").first
    assert search_box.input_value() == search_term, f"Expected {search_term} in search box, but got {search_box.input_value()}"


def test_pagination_with_multiple_pages(page, search_terms):
    search_term = search_terms["default_search_term"]
    home_page = HomePage(page)  
    home_page.goto()
    home_page.search_for_product(search_term)
    search_results_page = SearchResultsPage(page)

    #click on next page
    page.wait_for_selector('.s-pagination-next', timeout=5000)
    product_titles_page_1 = search_results_page.getProductTitles()
    search_results_page.goNextPage()

    #click on next page
    page.wait_for_selector('.s-pagination-next', timeout=5000)
    product_titles_page_2 = search_results_page.getProductTitles()
    search_results_page.goNextPage()

    #check page number and URL
    assert search_results_page.currentPageNumber() == "3", f"Expected page 3, but got {search_results_page.currentPageNumber()}"
    assert "page=3" in page.url, f"Expected page=3 in URL, but got {page.url}"

    #check product titles
    page_3_titles = search_results_page.getProductTitles()
    assert page_3_titles != product_titles_page_1 and page_3_titles != product_titles_page_2, f"Expected page 3 products to differ from page 1 and 2, but got {page_3_titles}"

    #check search term
    search_box = page.locator("#twotabsearchtextbox, #nav-bb-search").first
    assert search_box.input_value() == search_term, f"Expected {search_term} in search box, but got {search_box.input_value()}"
    