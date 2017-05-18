Feature: Register a product incidence
  As a user
  I want to register an incidence about a problem of a product that I have bought
  So the problem can be solved

  Background: The user wants to register an incidence.
    Given There are product categories in the data base
    And There are prodcuts in the data base

  Scenario: Register incidence
    Given I am registered as person
    And I login
      | username  | password      |
      | used_name | patatapatata1 |
    And I have bought a product
    When I visit my purchases page
    And I click the Incidence button
    And write and submit the incidence
      | name         | explanation             |
      | Broken thing | My thing is very broken |
    Then I see that the incidence is registered