from .base_page import Base_Page
from playwright.sync_api import Page

class Product_Page(Base_Page):

    locators = {
        "samsung_icon": "Samsung galaxy s6",
        "city": "#city",
        "credit_card": "#card",
        "month": "#month",
        "year": "#year",
        "Purchase": "Purchase"
     
    }
    
    def __init__(self, page: Page):
        super().__init__(page)

    def clickproduct(self):
        self.page.get_by_role("link").filter(has_text=self.locators["samsung_icon"]).click()

    def clickpurchasebutton(self):
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("button", name=self.locators["Purchase"]).click()