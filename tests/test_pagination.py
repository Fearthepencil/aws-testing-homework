"""
Test cases for Amazon search results pagination
"""
import pytest
from pages.home_page import AmazonHomePage
from pages.search_results_page import SearchResultsPage
from loguru import logger


@pytest.mark.pagination
@pytest.mark.functional
def test_navigate_to_page_2(amazon_home: AmazonHomePage,
                            search_results: SearchResultsPage,
                            search_term: str):
    """
    TC-005: Pagination - Navigate to Page 2
    
    Given: User has searched for a product and is on page 1
    When: User clicks "Next" or page 2
    Then: Page 2 of search results is displayed
    
    Priority: High
    """
    logger.info("=== TC-005: Navigate to Page 2 ===")
    
    # Given
    amazon_home.open()
    amazon_home.search_for(search_term)
    assert search_results.has_results(), "No search results on page 1"
    
    page_1_count = search_results.get_product_count()
    logger.info(f"Page 1 has {page_1_count} products")
    
    # When
    search_results.go_to_next_page()
    
    # Then
    current_page = search_results.get_current_page_number()
    assert current_page == 2, f"Expected page 2, but got page {current_page}"
    
    assert search_results.has_results(), "No search results on page 2"
    page_2_count = search_results.get_product_count()
    assert page_2_count > 0, "No products on page 2"
    
    logger.info(f"✓ Test passed: Successfully navigated to page 2")
    logger.info(f"  Page 2 has {page_2_count} products")


@pytest.mark.pagination
@pytest.mark.functional
def test_navigate_to_page_3(amazon_home: AmazonHomePage,
                            search_results: SearchResultsPage,
                            search_term: str):
    """
    TC-006: Pagination - Navigate to Page 3
    
    Given: User has searched for a product and is on page 1
    When: User navigates to page 3
    Then: Page 3 of search results is displayed
    
    Priority: High
    """
    logger.info("=== TC-006: Navigate to Page 3 ===")
    
    # Given
    amazon_home.open()
    amazon_home.search_for(search_term)
    assert search_results.has_results(), "No search results on page 1"
    
    # When - Navigate to page 2
    search_results.go_to_next_page()
    assert search_results.get_current_page_number() == 2, "Failed to reach page 2"
    
    # When - Navigate to page 3
    search_results.go_to_next_page()
    
    # Then
    current_page = search_results.get_current_page_number()
    assert current_page == 3, f"Expected page 3, but got page {current_page}"
    
    assert search_results.has_results(), "No search results on page 3"
    page_3_count = search_results.get_product_count()
    assert page_3_count > 0, "No products on page 3"
    
    logger.info(f"✓ Test passed: Successfully navigated to page 3")
    logger.info(f"  Page 3 has {page_3_count} products")

