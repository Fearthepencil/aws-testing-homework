from pages.base_page import BasePage
class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.amazon.com"
    
    def search_for_product(self, product_name):
        search_box = self.page.locator("#twotabsearchtextbox, #nav-bb-search").first
        search_box.fill(product_name)
        search_box.press("Enter")

    def goto(self):
        super().goto(self.url)