from behave import given, when, then
from pages.product_page import Product_Page


@when(u'I click the purchase buttan')
def step_impl(context):
     context.register_page.clickpurchasebutton()


@when(u'Verify the Thank you for your purchase alert messeges')
def step_impl(context):
    context.register_page.thankyoupurchase()

@then(u'Verify the Thank you for your purchase alert messages')
def step_impl(context):
    context.register_page.thankyoupurchase()