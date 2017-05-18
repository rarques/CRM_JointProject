Feature: Modify user (person or company) profile information
  # description
  As a user (person or company).
  I want to change my profile information.
  So my information is up to date.

  Background: The user (person or company) is registered in the system previously and is in the profile

  Scenario: User (company) updates profile information
    Given I am registered as company
    And I am logged as company
      | username | password |
      | padre    | patata1  |
    And I visit the modify as company page
    When I change the form fields that interest me
      | username           | email                             | country       | province   | city         | zip_code | street              | phone     | cif       |
      | oracle corporation | support_cloud_platform@oracle.com | Oracle Empire | California | Redwood city | 07421    | oracle headquarters | 323495156 | E43576214 |
    And I submit the modify company form
    Then I am redirected to my profile page
    And Exists a UserAsCompany with CIF = "E43576214"