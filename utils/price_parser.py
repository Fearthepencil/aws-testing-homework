def parse_price(price_str) -> float:
    try:
        price = float(price_str.replace("$", "").replace(",", "").strip())
    except (ValueError, AttributeError):
        return 0.0
    return price
