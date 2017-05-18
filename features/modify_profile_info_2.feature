Feature: Modify user (person or company) profile information
  # description
  As a user (person or company).
  I want to change my profile information.
  So my information is up to date.

  Background: The user (person or company) is registered in the system previously and is in the profile

  Scenario: The user enters invalid information
    Given I am registered as person
    And I login
      | username  | password      |
      | used_name | patatapatata1 |
    And I visit the modify as person page
    When Fields I've tried to modify contain invalid information
      | username | email                | country | province           | city         | zip_code | street | phone     | dni       |
      | aragorn  | aragorn#arathorn-sil | gondor  | Campos de pelennor | minas tirith | 06660    | Anor   | 999666333 | 45236834T |
    And I submit the modify person form
    Then I get an error telling me the invalid information