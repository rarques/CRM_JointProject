
Feature: Send recommendation to clients
  As the seller
  I want customized recommendations for my clients
  So they know the best products for them


  Scenario: Show recommendation
    Given I am interested in a category
    And I am registered
    | username | password | category |
    | padre    | java     | mobil    |
    And I log in
    And There are products related with my category
    | name | category |
    | bq   | mobil    |
    And So I get a recommendation
    And I go to the homepage