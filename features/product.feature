Feature: User Registration and Purchase

Background:
    Given I am on the registration page
    And I click the login link
    When I fill in the registration form with valid data:
        | user_name | password |
        | test      | test     |
    And I login the form
    And Verify the Successful authentication 

Scenario: Open Samsung Galaxy S6 Product Page
    Given I click the samsung galaxy s6 link

Scenario: Add product to cart
    Given I click the samsung galaxy s6 link
    And I click the Add Cart button
    And I click ok button in Product added alert pop up

Scenario: Open Cart Page
    Given I click the Cart link

Scenario: Place Order
    Given I click the Cart link
    And I click the Place order button
    When I fill in the place order form with valid data:
        | user_name | country | city | credit_card | month | year |
        | test      | test    | seng | visa        | 10    | 2025 |

Scenario: Verify Purchase Confirmation
    When I click the purchase button
    Then Verify the Thank you for your purchase alert message
     Given I click the samsung galaxy s6 link
    And I click the Add Cart button
    And I click ok button in Product added alert pop up
    And I click the Cart link
    And I click the Place order button
    When I fill in the place order form with valid data:
        | user_name |  country | city | credit_card | month | year |
        | test      |  test    | seng | visa        | 10    | 2025 |