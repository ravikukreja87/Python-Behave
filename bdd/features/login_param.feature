Feature: I as a normal user want to login to CRM Portal

Scenario Outline: Login as all users
  Given I am at Login Page of CRM Portal
  When I enter correct username and password and press Login for <username> and <password>
  Then I should be logged in to CRM and welcome message should be displayed

  Examples: By user type
  | username                             | password     |
  | techcanvassacademy@techcanvass.co.in | abhishek1234 |
  | techcanvassuser@techcanvass.co.in    | user1234     |