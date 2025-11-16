from behave import given, when, then
from pages.register_page import Register_Page

@given('I am on the registration page')
def step_impl(context):
    # registration_url = f"{context.base_url}customer/account/create/"
    registration_url = context.base_url
    if not hasattr(context, "page") or context.page is None:
        raise RuntimeError("context.page is not initialized")
    
    context.register_page = Register_Page(context.page)
    context.register_page.goto(registration_url)
    


@when('I fill in the registration form with valid data')
def step_fill_registration_form(context):
    for row in context.table:
        first_name = row['user_name']
        password = row['password']
        context.register_page.register(first_name, password)



@given(u'I click the login link')
def step_impl(context):
    context.register_page.submit_form()

@when('I Login the form')
def step_submit_form(context):
    context.register_page.login_form()

@when(u'Verify the Successful authentication')
def step_impl(context):
     context.register_page.successmessage()
    
@given(u'I click the samsung galaxy s6 link')
def step_impl(context):
    context.register_page.clickproduct()

@given(u'I click the Add Cart button')
def step_impl(context):
    context.register_page.clickaddcart()

@given(u'I click ok button in Product added alert pop up')
def step_impl(context):
    context.register_page.clickOkButton()

@given(u'I click the Cart link')
def step_impl(context):
    context.register_page.clickcartlink()

@given(u'I click the Place order button')
def step_impl(context):
    context.register_page.clickplaceorder()

@when(u'I fill in the place order form with valid data')
def step_impl(context):
    for row in context.table:
        first_name = row['user_name']
        country = row['country']
        city = row['city']
        credit_card = row['credit_card']
        month = row['month']
        year = row['year']
        context.register_page.placeorder(first_name, country, city , credit_card , month , year )


@when(u'I click the purchase button')
def step_impl(context):
     context.register_page.clickpurchasebutton()


@when(u'Verify the Thank you for your purchase alert messages')
def step_impl(context):
    context.register_page.thankyoupurchase()

@then(u'Verify the Thank you for your purchase alert message')
def step_impl(context):
    context.register_page.thankyoupurchase()