from .base_page import Base_Page
from playwright.sync_api import Page

class Register_Page(Base_Page):

    locators = {
        "first_name": "#loginusername",
        "password": "#loginpassword",
        "submit_button": "#login2",
        "login_link": "Log in",
        "login_button": "Log in",
        "log_out": "Log out",
        "samsung_icon": "Samsung galaxy s6",
        "addcart_button": "Add to cart",
        "cart_link": "Cart",
        "placeorder": "Place Order",
        "first_names": "#name",
        "country": "#country",
        "city": "#city",
        "credit_card": "#card",
        "month": "#month",
        "year": "#year",
        "Purchase": "Purchase"

    }

    ALERT_MESSAGES = {
    "thank_you_purchase": "Thank you for your purchase!",
    "product_added": "Product added."
    }
    
    def __init__(self, page: Page):
        super().__init__(page)

    def register(self, fname: str, password: str):
        data = {
            "first_name": fname,
            "password": password,
            # "confirm_password": password
        }

        for field, value in data.items():
            self.page.locator(self.locators[field]).fill(value)
 
    def submit_form(self):
        self.page.get_by_role("link").filter(has_text=self.locators["login_link"]).click()
       # self.page.get_by_role("link").filter(has_text="Log in").click()

    def login_form(self):
        self.page.get_by_role("button").filter(has_text=self.locators["login_button"]).click()
       # self.page.get_by_role("link").filter(has_text="Log in").click()

    def successmessage(self):
        error_message= self.page.get_by_role("link").filter(has_text=self.locators["log_out"]).text_content()
        assert 'Log out' == error_message

    def clickproduct(self):
        self.page.get_by_role("link").filter(has_text=self.locators["samsung_icon"]).click()
        
    def clickaddcart(self):
        
        self.page.wait_for_timeout(10000)
     
        self.page.get_by_role("link").filter(has_text=self.locators["addcart_button"]).click()
    
    def clickOkButton(self):
    # This function will run when alert appears
        def handle_dialog(dialog):
            alert_text = dialog.message()
            print("Alert:", alert_text)
            assert alert_text == "Product added.", "Alert message mismatch!"
            dialog.accept()
    
    def clickcartlink(self):
        self.page.get_by_role("link", name=self.locators["cart_link"], exact=True).click()

    def clickplaceorder(self):
        self.page.get_by_role("button", name=self.locators["placeorder"], exact=True).click()

    def placeorder(self, first_name: str, country: str, city: str, credit_card: str, month: str, year: str  ):
        data = {
            "first_names": first_name,
            "country": country,
            "city": city,
            "credit_card": credit_card,
            "month": month,
            "year": year
            # "confirm_password": password
        }

        for field, value in data.items():
            self.page.locator(self.locators[field]).fill(value)

    def clickpurchasebutton(self):
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("button", name=self.locators["Purchase"]).click()

    def thankyoupurchase(self):
        expected_text = self.ALERT_MESSAGES["thank_you_purchase"]
    # This function will run when alert appears
        def handle_dialog(dialog):
            alert_text = dialog.message()
            print("Alert:", alert_text)
            assert alert_text == expected_text, f"Expected: {expected_text}, Got: {alert_text}"
        #    assert alert_text == "Thank you for your purchase!", "Alert message mismatch!"
            dialog.accept()