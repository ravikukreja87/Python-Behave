Feature: I as a normal user want to login to CRM Portal

Scenario: Login
  Given I am at Login Page of CRM Portal
  When I enter correct username and password and press Login for normal user
  Then I should be logged in to CRM and welcome message should be displayed

  Scenario: Login with admin user
    Given I am at Login Page of CRM Portal
    When I enter correct username and password and press Login for admin user
    Then I should be logged in to CRM and welcome message should be displayed
