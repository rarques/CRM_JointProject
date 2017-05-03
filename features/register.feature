Feature: Register a new user
  As a user (person or company)
  I want to create an account with my information
  So I can use the different services of the web page.

  Background: The user wants to register and visits the register page

  Scenario: Register new person user
    Given I'm not registered
    And I visit the register as person page
    When I fill the form's basic fields
      | username | password    | repassword  | email            | phone     |
      | moliva   | napolitanes | napolitanes | moliva@gmail.com | 973123456 |
    And I fill the form's specific fields
      | street      | city     | zip_code | province  | country      | DNI       |
      | Croissant I | Isengard | 23230    | Enedwaith | Middle Earth | 12345678A |
    And I submit the form
    Then I'm redirected to my profile page
    And Exists a UserAsPerson with DNI = 12345678A

#  Scenario: Register new company user
#    Given I'm not registered
#    And I visit the register as company page
#    When I fill the form's basic fields
#      | username | password      | repassword    | email         | phone     |
#      | sirius   | i<3croissants | i<3croissants | sir@gmail.com | 973123456 |
#    And I fill the form's specific fields
#      | street      | city     | zipcode | province  | country      | cif       |
#      | Croissant I | Isengard | 23230   | Enedwaith | Middle Earth | 12345678A |
#    And I submit the form
#    Then I'm redirected to my profile page
#    And I see my personal information
#
#  Scenario: The user is already registered
#    Given I'm registered
#    And I visit the register as person page
#      | username  | password | repassword | email           | phone     |
#      | used_name | password | password   | random@mail.com | 666666666 |
#    When I fill the form's basic fields
#      | street      | city     | zipcode | province  | country      | cif       |
#      | Croissant I | Isengard | 23230   | Enedwaith | Middle Earth | 12345678A |
#    And I fill the form's specific fields
#    And I submit the form
#    Then I get an error telling me I'm registered
#
#  Scenario: The user enters incorrect information
#    Given I'm not registered
#    And I visit the register as person page
#    When I fill the form with invalid information
#    And I submit the form
#    Then I get an error telling me the wrong information
