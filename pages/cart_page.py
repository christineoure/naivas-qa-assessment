from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_btn = page.get_by_role("button", name="Cart", exact=True)

    def open(self):
        self.page.wait_for_load_state("networkidle")
        self.cart_btn.click()

    def proceed_to_checkout(self):
        self.page.get_by_role("button", name="Checkout").click()
