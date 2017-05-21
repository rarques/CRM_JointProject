Feature: Send reminders to afk clients
  As a worker (technogad)
  I want to send an email to afk clients
  So they remember our web page.

  Background: The worker wants to send emails
    Given There are clients afk

  Scenario: Send emails
    Given I am logged in
    And I visit the send reminders page
    When There is an afk client
      | username | password | last_login | email |
      | pepito   | palote   | 2017-05-02 | pepito@palotes.com |
    And I click the send button
    Then I see the reminder sent page
