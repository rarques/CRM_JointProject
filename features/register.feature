Feature: Register a new user
  As a user (person or company)
  I want to create an account with my information
  So I can use the different services of the web page.

  Background: The user wants to register and visits the register page
    Given There are product categories in the data base

  Scenario: Register new person user
    Given I'm not registered
    And I visit the register as person page
    When I fill the form's basic fields
      | username | password    | repassword  | email            | phone     |
      | moliva   | napolitanes | napolitanes | moliva@gmail.com | 973123456 |
    And I fill the form's specific fields
      | street      | city     | zip_code | province  | country      | DNI       |
      | Croissant I | Isengard | 23230    | Enedwaith | Middle Earth | 12345678A |
    And I select the categories I'm interested in
      | category      |
      | Keyboard      |
      | Graphic cards |
    And I submit the form
    Then I'm redirected to my profile page
    And Exists a UserAsPerson with DNI = 12345678A

  Scenario: Register new company user
    Given I'm not registered
    And I visit the register as company page
    When I fill the form's basic fields
      | username | password      | repassword    | email         | phone     |
      | sirius   | i<3croissants | i<3croissants | sir@gmail.com | 973123456 |
    And I fill the form's specific fields
      | street      | city     | zip_code | province  | country      | CIF       |
      | Croissant I | Isengard | 23230    | Enedwaith | Middle Earth | 98765432Z |
    And I select the categories I'm interested in
      | category      |
      | Keyboard      |
      | Graphic cards |
    And I submit the form
    Then I'm redirected to my profile page
    And Exists a UserAsCompany with CIF = 98765432Z

  Scenario: The user is already registered
    Given I'm registered
    And I visit the register as company page
    When I fill the form's basic fields
      | username  | password | repassword | email           | phone     |
      | used_name | password | password   | random@mail.com | 666666666 |
    And I fill the form's specific fields
      | street      | city     | zip_code | province  | country      | CIF       |
      | Croissant I | Isengard | 23230    | Enedwaith | Middle Earth | 12345678A |
    And I submit the form
    Then I get an error telling me I'm registered
