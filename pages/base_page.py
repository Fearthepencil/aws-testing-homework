class BasePage:

    def __init__(self, page):
        self.page = page
    
    def goto(self, url):
        self.page.goto(url)

    def take_screenshot(self, filename):
        self.page.screenshot(path=f"screenshots/{filename}.png")