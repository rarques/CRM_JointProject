Feature: Modify user (person or company) profile information
  # description
  As a user (person or company).
  I want to change my profile information.
  So my information is up to date.

  Background: The user (person or company) is registered in the system previously and is in the profile

  Scenario: User (person) updates profile information
    Given I am registered
    And I visit the modify as person page
    When I change the form fields that interest me
      | username | email                | country | province           | city         | zip_code | street | phone     | DNI       |
      | aragorn  | aragorn@arathorn.sil | gondor  | Campos de pelennor | minas tirith | 06660    | Anor   | 999666333 | 45236834T |
    And I submit the modify person form
    Then I am redirected to my profile page
    And Exists a UserAsPerson with DNI = "45236834T"

  Scenario: The user enters invalid information
    Given I'm registered
    And I visit the modify as person page
    When Fields I've tried to modify contain invalid information
      | username | email                | country | province           | city         | zip_code | street | phone     | DNI       |
      | aragorn  | aragorn#arathorn-sil | gondor  | Campos de pelennor | minas tirith | 06660    | Anor   | 999666333 | 45236834T |

    And I submit the modify person form
    Then I get an error telling me the invalid information

  Scenario: User (company) updates profile information
    Given I'm registered
    And I visit the modify as company page
    When I change the form fields that interest me
      | username           | email                             | country       | province   | city         | zip_code | street              | phone     | CIF       |
      | oracle corporation | support_cloud_platform@oracle.com | Oracle Empire | California | Redwood city | 07421    | oracle headquarters | 323495156 | E43576214 |
    And I submit the modify company form
    Then I am redirected to my profile page
    And Exists a UserAsCompany with CIF = "E43576214"

  Scenario: The user (company) enters invalid information
    Given I'm registered
    And I visit the modify as company page
    When Fields I've tried to modify contain invalid information
      | username           | email                                | country       | province   | city         | zip_code    | street              | phone     | CIF       |
      | oracle corporation | support_cloud_platform#~$oracle->com | Oracle Empire | California | Redwood city | 07421------ | oracle headquarters | 323495156 | E43576214 |
    And I submit the modify company form
    Then I get an error telling me the invalid information
