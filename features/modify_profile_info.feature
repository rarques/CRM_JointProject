Feature: Modify user (person or company) profile information
  # description
  As a user (person or company).
  I want to change my profile information.
  So my information is up to date.

  Background: The user (person or company) is registered in the system previously and is in the profile

  Scenario: User (person) updates profile information
    Given I'm registered
    When I change the form fields that interest me
    And I submit the form
    Then I receive an email notification

  Scenario: The user enters invalid information
    Given I'm registered
    When Fields I've tried to modify contain invalid information
    And I submit the form
    Then I get an error telling me the invalid information

  Scenario: User (company) updates profile information
    Given I'm registered
    When I change the form fields that interest me
    And I submit the form
    Then I receive an email notification

  Scenario: The user (company) enters invalid information
    Given I'm registered
    When Fields I've tried to modify contain invalid information
    And I submit the form
    Then I get an error telling me the invalid information
