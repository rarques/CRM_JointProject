Feature: Register a new user
  As a user (person or company)
  I want to create an account with my information
  So I can use the different services of the web page.

  Background: The user wants to register and visits the register page
    Given The user visits the register page

  Scenario: Register new user
    Given I'm not registered
    When I fill the form's basic fields
      | username_p | password_p  | repassword_p | email              | name_p |
      | moliva     | napolitanes | napolitanes  | oliva@diei.udl.cat | Marta  |
    And I fill the form's specific fields
      | lastname_p | DNI       | phone     | street      | city     | zipcode | province  | country      |
      | Oliva      | 12345678A | 973123456 | Croissant I | Isengard | 23230   | Enedwaith | Middle Earth |
    And I submit the form
    Then I'm redirected to my profile page

  Scenario: The user is already registered
    Given I'm registered
    When I fill the form's basic fields
    And I fill the form's specific fields
    And I submit the form
    Then I get an error telling me I'm registered

  Scenario: The user enters incorrect information
    Given I'm not registered
    When I fill the form with invalid information
    And I submit the form
    Then I get an error telling me the wrong information
