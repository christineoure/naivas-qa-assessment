# pages/product_page.py
from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://qa-abcd.naivas.online/"

    def navigate(self):
        self.page.goto(self.url)

    def add_item_to_cart(self, product_name: str):
        product = self.page.get_by_text(product_name, exact=False).first
        product.scroll_into_view_if_needed()
        self.page.get_by_role("button", name="Add").first.click()
