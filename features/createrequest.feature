Feature: Creation of top up requests


  Background: Access to EZ-Link's Utility Top Up Menu
    Given the user access EZ-Link's Portal
    When he enter login information
    Then he should be able to login to Utility Top Up navigation menu


  Scenario: Create top up request for new card
    Given the user click on create top up (new card) request navigation menu
    When he enter job order number and top up amount in the request page
    And check the total top-up amount
    Then the successful submission response is displayed once request is submitted for new card
    And status should display "Pending" once he key in the new card job order number in the View Top Up Request page


  Scenario: Create top up request for existing card
    Given the user click on create top up (existing card) request navigation menu
    When he enter job order number in the request page
    And check the total topup amount
    Then the successful submission response is displayed once request is submitted for existing card
    And status should display "Pending" once he key in the existing card job order number in the View Top Up Request page>


