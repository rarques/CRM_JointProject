Feature: Post an opinion about a product
  As a user
  I want to post an opinion about a product that I have bought
  So that the company has more feedback to improve services

  Background: The user wants to post an opinion
    Given There are product categories in the data base
    And There are prodcuts in the data base

  Scenario: Post opinion
    Given I am registered as person
    And I login
      | username  | password      |
      | used_name | patatapatata1 |
    And I have bought a product
    When I visit my purchases page
    And I click the Opinion button
    And write and submit the opinion
      | name         | comment               | rating |
      | Good service | Good customer service | 4      |
    Then I see that the opinion is posted