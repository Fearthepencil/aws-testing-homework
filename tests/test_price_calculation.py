"""
Test cases for price calculation across pagination
This test suite calculates and logs average prices for the first 3 pages
"""
import pytest
from pages.home_page import AmazonHomePage
from pages.search_results_page import SearchResultsPage
from utils.price_calculator import PriceCalculator
from loguru import logger


@pytest.mark.price_calculation
def test_calculate_average_price_page_1(amazon_home: AmazonHomePage,
                                        search_results: SearchResultsPage,
                                        search_term: str):
    """
    TC-009: Calculate Average Price on Page 1
    
    Given: User has searched for a product
    When: User is on page 1 of search results
    Then: System calculates and logs average price of all products on page 1
    
    Priority: High (Required by homework task)
    """
    logger.info("=== TC-009: Calculate Average Price - Page 1 ===")
    
    # Given
    amazon_home.open()
    amazon_home.search_for(search_term)
    assert search_results.has_results(), "No search results on page 1"
    
    # When
    prices = search_results.get_all_product_prices()
    
    # Then
    assert len(prices) > 0, "No prices found on page 1"
    
    calculator = PriceCalculator()
    average = calculator.calculate_average(prices)
    
    # Log to console as required by homework
    summary = calculator.format_price_summary(1, prices, average)
    print(summary)
    logger.info(summary)
    
    assert average > 0, "Average price should be greater than 0"
    logger.info(f"✓ Test passed: Page 1 average price calculated: ${average:.2f}")


@pytest.mark.price_calculation
def test_calculate_average_price_page_2(amazon_home: AmazonHomePage,
                                        search_results: SearchResultsPage,
                                        search_term: str):
    """
    TC-010: Calculate Average Price on Page 2
    
    Given: User has searched for a product
    When: User navigates to page 2 of search results
    Then: System calculates and logs average price of all products on page 2
    
    Priority: High (Required by homework task)
    """
    logger.info("=== TC-010: Calculate Average Price - Page 2 ===")
    
    # Given
    amazon_home.open()
    amazon_home.search_for(search_term)
    assert search_results.has_results(), "No search results on page 1"
    
    # Navigate to page 2
    search_results.go_to_next_page()
    assert search_results.get_current_page_number() == 2, "Failed to reach page 2"
    
    # When
    prices = search_results.get_all_product_prices()
    
    # Then
    assert len(prices) > 0, "No prices found on page 2"
    
    calculator = PriceCalculator()
    average = calculator.calculate_average(prices)
    
    # Log to console as required by homework
    summary = calculator.format_price_summary(2, prices, average)
    print(summary)
    logger.info(summary)
    
    assert average > 0, "Average price should be greater than 0"
    logger.info(f"✓ Test passed: Page 2 average price calculated: ${average:.2f}")


@pytest.mark.price_calculation
def test_calculate_average_price_page_3(amazon_home: AmazonHomePage,
                                        search_results: SearchResultsPage,
                                        search_term: str):
    """
    TC-011: Calculate Average Price on Page 3
    
    Given: User has searched for a product
    When: User navigates to page 3 of search results
    Then: System calculates and logs average price of all products on page 3
    
    Priority: High (Required by homework task)
    """
    logger.info("=== TC-011: Calculate Average Price - Page 3 ===")
    
    # Given
    amazon_home.open()
    amazon_home.search_for(search_term)
    assert search_results.has_results(), "No search results on page 1"
    
    # Navigate to page 2
    search_results.go_to_next_page()
    assert search_results.get_current_page_number() == 2, "Failed to reach page 2"
    
    # Navigate to page 3
    search_results.go_to_next_page()
    assert search_results.get_current_page_number() == 3, "Failed to reach page 3"
    
    # When
    prices = search_results.get_all_product_prices()
    
    # Then
    assert len(prices) > 0, "No prices found on page 3"
    
    calculator = PriceCalculator()
    average = calculator.calculate_average(prices)
    
    # Log to console as required by homework
    summary = calculator.format_price_summary(3, prices, average)
    print(summary)
    logger.info(summary)
    
    assert average > 0, "Average price should be greater than 0"
    logger.info(f"✓ Test passed: Page 3 average price calculated: ${average:.2f}")


@pytest.mark.price_calculation
def test_calculate_all_three_pages_combined(amazon_home: AmazonHomePage,
                                            search_results: SearchResultsPage,
                                            search_term: str):
    """
    TC-012: Calculate Average Price Across All 3 Pages (Combined)
    
    Given: User has searched for a product
    When: User collects prices from pages 1, 2, and 3
    Then: System calculates overall average and logs summary
    
    Priority: Medium
    """
    logger.info("=== TC-012: Calculate Combined Average - All 3 Pages ===")
    
    all_prices = []
    calculator = PriceCalculator()
    
    # Given
    amazon_home.open()
    amazon_home.search_for(search_term)
    
    # Collect prices from page 1
    assert search_results.has_results(), "No search results on page 1"
    page_1_prices = search_results.get_all_product_prices()
    all_prices.extend(page_1_prices)
    avg_1 = calculator.calculate_average(page_1_prices)
    
    # Collect prices from page 2
    search_results.go_to_next_page()
    page_2_prices = search_results.get_all_product_prices()
    all_prices.extend(page_2_prices)
    avg_2 = calculator.calculate_average(page_2_prices)
    
    # Collect prices from page 3
    search_results.go_to_next_page()
    page_3_prices = search_results.get_all_product_prices()
    all_prices.extend(page_3_prices)
    avg_3 = calculator.calculate_average(page_3_prices)
    
    # Calculate overall average
    overall_average = calculator.calculate_average(all_prices)
    
    # Log comprehensive summary
    summary = f"\n{'='*60}\n"
    summary += f"COMBINED PRICE SUMMARY - ALL 3 PAGES\n"
    summary += f"{'='*60}\n"
    summary += f"Search term: '{search_term}'\n"
    summary += f"Total products analyzed: {len(all_prices)}\n"
    summary += f"\n"
    summary += f"Page 1 - Products: {len(page_1_prices)}, Avg: ${avg_1:.2f}\n"
    summary += f"Page 2 - Products: {len(page_2_prices)}, Avg: ${avg_2:.2f}\n"
    summary += f"Page 3 - Products: {len(page_3_prices)}, Avg: ${avg_3:.2f}\n"
    summary += f"\n"
    summary += f"OVERALL AVERAGE PRICE: ${overall_average:.2f}\n"
    summary += f"Lowest price found: ${min(all_prices):.2f}\n"
    summary += f"Highest price found: ${max(all_prices):.2f}\n"
    summary += f"{'='*60}\n"
    
    print(summary)
    logger.info(summary)
    
    assert len(all_prices) > 0, "No prices collected"
    assert overall_average > 0, "Overall average should be greater than 0"
    
    logger.info(f"✓ Test passed: Combined average calculated: ${overall_average:.2f}")

