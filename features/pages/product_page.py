# from .base_page import Base_Page
# from playwright.sync_api import Page

# class Product_Page(Base_Page):

#     locators = {
#         "samsung_icon": "Samsung galaxy s6"
     
#     }
    
#     def __init__(self, page: Page):
#         super().__init__(page)

#     def clickproduct(self):
#         self.page.get_by_role("link").filter(has_text=self.locators["samsung_icon"]).click()