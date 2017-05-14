Feature: Register a product incidence
  As a user
  I want to register an incidence about a problem of a product that I have bought
  So the problem can be solved

  Background: The user wants to register an incidence.
    Given I'm registered
    And I am logged as person

  Scenario: Register incidence
    Given I have bought a product
    When I click the Incidence button
    And write and submit the incidence
    Then I see that the incidence is registered