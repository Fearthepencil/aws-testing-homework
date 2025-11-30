def test_browser_opens(page):
    page.goto("https://www.amazon.com")
    assert "Amazon" in page.title()