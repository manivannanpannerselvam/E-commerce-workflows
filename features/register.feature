Feature: Register Feature

  Scenario: New User Registration
    Given I am on the registration page
    And I click the login link
    When I fill in the registration form with valid data:
        | user_name |  password |
        | test       |  test    |
    And I login the form
    And Verify the Successful authentication 
    Given I click the samsung galaxy s6 link
    And I click the Add Cart button
    And I click ok button in Product added alert pop up
    And I click the Cart link
    And I click the Place order button
    When I fill in the place order form with valid data:
        | user_name |  country | city | credit_card | month | year |
        | test      |  test    | seng | visa        | 10    | 2025 |
    And I click the purchase button
    And Verify the Thank you for your purchase alert messages

   
