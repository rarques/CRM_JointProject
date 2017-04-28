Feature: Register a new user
  As a user (person or company)
  I want to create an account with my information
  So I can use the different services of the web page.

  Background: The user wants to register and visits the register page
    Given The user wants to register
    And visits de register page

  Scenario: Register new user
    Given I'm not registered
    When I fill the form with valid information
    And I submit the form
    Then I receive an email confirmation
    And I accept the confirmation

  Scenario: The user is already registered
    Given I'm registered
    When I fill the form with valid information
    And I submit the form
    Then I get an error telling me I'm registered

  Scenario: The user enters incorrect information
    Given I'm not registered
    When I fill the form with invalid information
    And I submit the form
    Then I get an error
