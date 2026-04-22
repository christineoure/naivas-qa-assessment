import pytest
from playwright.sync_api import Page, expect
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_naivas_demo_purchase_journey(page: Page):
    # 1. Setup
    page.set_viewport_size({"width": 1920, "height": 1080})
    product_p = ProductPage(page)
    cart_p = CartPage(page)

    # 2. Add Products
    product_p.navigate()
    product_p.add_item_to_cart("Hoodie")
    
    # On redirect, go home for the next item
    product_p.navigate() 
    product_p.add_item_to_cart("Shoes")

    # 3. Open Cart & Checkout
    cart_p.open()
    cart_p.proceed_to_checkout()

    # 4. Fill Details (Shipping & Billing)
    page.fill("#first-name", "Christine")
    page.fill("#last-name", "Oure")
    page.fill("#address", "Nairobi, CBD")
    page.click("#continue")

    # 5. Payment & Finish
    page.click("#finish")

    # 6. Screenshots
    expect(page.locator(".complete-header")).to_contain_text("THANK YOU")
    page.screenshot(path="screenshots/purchase_complete.png")
