"""
Price calculation utilities
"""
from typing import List
from loguru import logger


class PriceCalculator:
    """Utility class for price calculations"""
    
    @staticmethod
    def calculate_average(prices: List[float]) -> float:
        """
        Calculate average price from a list of prices
        
        Args:
            prices: List of prices as floats
            
        Returns:
            Average price rounded to 2 decimal places
        """
        if not prices:
            logger.warning("Empty price list provided")
            return 0.0
        
        average = sum(prices) / len(prices)
        logger.info(f"Calculated average: ${average:.2f} from {len(prices)} prices")
        return round(average, 2)
    
    @staticmethod
    def parse_price_string(price_str: str) -> float:
        """
        Parse price string to float
        
        Args:
            price_str: Price string (e.g., "$19.99", "19.99", "$1,299.00")
            
        Returns:
            Price as float
        """
        try:
            # Remove currency symbols and commas
            cleaned = price_str.replace("$", "").replace(",", "").strip()
            return float(cleaned)
        except (ValueError, AttributeError) as e:
            logger.error(f"Could not parse price '{price_str}': {e}")
            return 0.0
    
    @staticmethod
    def handle_price_range(price_str: str) -> float:
        """
        Handle price ranges (e.g., "$19.99 - $29.99")
        Returns the lower price
        
        Args:
            price_str: Price string that may contain a range
            
        Returns:
            Lower price as float
        """
        if "-" in price_str:
            # Split by dash and take first price
            parts = price_str.split("-")
            return PriceCalculator.parse_price_string(parts[0])
        return PriceCalculator.parse_price_string(price_str)
    
    @staticmethod
    def format_price_summary(page_num: int, prices: List[float], average: float) -> str:
        """
        Format price summary for console output
        
        Args:
            page_num: Page number
            prices: List of prices
            average: Calculated average
            
        Returns:
            Formatted string for console output
        """
        summary = f"\n{'='*60}\n"
        summary += f"PAGE {page_num} PRICE SUMMARY\n"
        summary += f"{'='*60}\n"
        summary += f"Total products with prices: {len(prices)}\n"
        summary += f"Average price: ${average:.2f}\n"
        summary += f"Lowest price: ${min(prices):.2f}\n" if prices else "Lowest price: N/A\n"
        summary += f"Highest price: ${max(prices):.2f}\n" if prices else "Highest price: N/A\n"
        summary += f"{'='*60}\n"
        return summary

