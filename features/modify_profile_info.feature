Feature: Modify user (person or company) profile information
  # description
  As a user (person or company).
  I want to change my profile information.
  So my information is up to date.

  Background: The user (person or company) is registered in the system previously and is in the profile

  Scenario: User (person) updates profile information
    Given I am registered as person
    And I login
      | username  | password      |
      | used_name | patatapatata1 |
    And I visit the modify as person page
    When I change the form fields that interest me
      | username | email                | country | province           | city         | zip_code | street | phone     | dni       |
      | aragorn  | aragorn@arathorn.sil | gondor  | Campos de pelennor | minas tirith | 06660    | Anor   | 999666333 | 45236834T |
    And I submit the modify person form
    Then I am redirected to my profile page
    And Exists a UserAsPerson with DNI = "45236834T"
