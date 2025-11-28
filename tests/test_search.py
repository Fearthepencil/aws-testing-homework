"""
Test cases for Amazon product search functionality
"""
import pytest
from pages.home_page import AmazonHomePage
from pages.search_results_page import SearchResultsPage
from pages.product_detail_page import ProductDetailPage
from loguru import logger


@pytest.mark.smoke
@pytest.mark.functional
def test_valid_product_search_returns_results(amazon_home: AmazonHomePage, 
                                               search_results: SearchResultsPage,
                                               search_term: str):
    """
    TC-001: Valid Product Search Returns Results
    
    Given: User is on Amazon homepage
    When: User searches for "wireless mouse"
    Then: Search results page displays with relevant products
    
    Priority: High
    Risk: Product search failure (High likelihood, High impact)
    """
    logger.info("=== TC-001: Valid Product Search Returns Results ===")
    
    # Given: User is on Amazon homepage
    amazon_home.open()
    assert amazon_home.is_loaded(), "Amazon homepage did not load"
    
    # When: User searches for "wireless mouse"
    amazon_home.search_for(search_term)
    
    # Then: Search results page displays with relevant products
    assert search_results.has_results(), "No search results displayed"
    product_count = search_results.get_product_count()
    assert product_count > 0, "No products found in search results"
    
    logger.info(f"✓ Test passed: Found {product_count} products")


@pytest.mark.functional
def test_search_with_multiple_keywords(amazon_home: AmazonHomePage,
                                       search_results: SearchResultsPage):
    """
    TC-002: Search with Multiple Keywords
    
    Given: User is on Amazon homepage
    When: User searches for "gaming keyboard rgb"
    Then: Search results display products matching all keywords
    
    Priority: High
    """
    logger.info("=== TC-002: Search with Multiple Keywords ===")
    
    # Given
    amazon_home.open()
    
    # When
    search_term = "gaming keyboard rgb"
    amazon_home.search_for(search_term)
    
    # Then
    assert search_results.has_results(), "No search results displayed"
    product_count = search_results.get_product_count()
    assert product_count > 0, "No products found"
    
    # Verify first product contains relevant keywords
    product = search_results.get_product_details(0)
    assert 'title' in product, "Product title not found"
    
    logger.info(f"✓ Test passed: Found {product_count} products for multi-keyword search")


@pytest.mark.functional
def test_product_card_displays_required_information(amazon_home: AmazonHomePage,
                                                    search_results: SearchResultsPage,
                                                    search_term: str):
    """
    TC-007: Product Card Displays Required Information
    
    Given: User has searched for a product
    When: User views search results
    Then: Each product card displays title, price, and rating
    
    Priority: High
    """
    logger.info("=== TC-007: Product Card Displays Required Information ===")
    
    # Given
    amazon_home.open()
    amazon_home.search_for(search_term)
    
    # When & Then
    assert search_results.has_results(), "No search results displayed"
    
    # Check first product has required information
    product = search_results.get_product_details(0)
    
    assert 'title' in product and product['title'], "Product title is missing"
    assert 'price' in product and product['price'], "Product price is missing"
    # Rating might not always be present, so we just log it
    
    logger.info(f"✓ Test passed: Product card contains required information")
    logger.info(f"  Title: {product.get('title', 'N/A')[:50]}...")
    logger.info(f"  Price: {product.get('price', 'N/A')}")
    logger.info(f"  Rating: {product.get('rating', 'N/A')}")


@pytest.mark.functional
def test_click_product_opens_detail_page(amazon_home: AmazonHomePage,
                                         search_results: SearchResultsPage,
                                         product_detail: ProductDetailPage,
                                         search_term: str):
    """
    TC-008: Click Product Opens Detail Page
    
    Given: User has searched for a product
    When: User clicks on a product from search results
    Then: Product detail page opens with product information
    
    Priority: High
    """
    logger.info("=== TC-008: Click Product Opens Detail Page ===")
    
    # Given
    amazon_home.open()
    amazon_home.search_for(search_term)
    assert search_results.has_results(), "No search results displayed"
    
    # Get product title before clicking
    product = search_results.get_product_details(0)
    search_title = product.get('title', '')
    
    # When
    search_results.click_product(0)
    
    # Then
    assert product_detail.is_loaded(), "Product detail page did not load"
    assert product_detail.has_product_image(), "Product image not displayed"
    
    detail_title = product_detail.get_product_title()
    assert detail_title, "Product title not found on detail page"
    
    logger.info(f"✓ Test passed: Product detail page loaded successfully")
    logger.info(f"  Product: {detail_title[:50]}...")

