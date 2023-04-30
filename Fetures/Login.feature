Feature: Login to Sauce Demo

  Scenario: Successful login
    Given I am on the login page
    When I enter my username "standard_user"
    And I enter my password "secret_sauce"
    And I click the login button
    Then I should be on the products page
    And I should see the products title "Products"

  Scenario: Failed login
    Given I am on the login page
    When I enter an invalid username "invalid_user"
    And I enter an invalid password "invalid_password"
    And I click the login button
    Then I should see an error message "Epic sadface: Username and password do not match any user in this service"