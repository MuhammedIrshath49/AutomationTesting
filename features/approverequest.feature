Feature: Approval of top up requests

  Background: Access to EZ-Link's View Top Up Request Page
    Given the user browse EZ-Link's Portal
    When he enter username and password
    Then he should be able to login to View All Top Up Requests page


  Scenario: Approve request for new card
    Given the user click the filter results for the job order number of new card entered in filter textbox
    When he check the job order number, number of cards and top-up amount
    Then the successful submission response is displayed once request is submitted
    And status will show "Approved" when user search for the job order number of new card entered in the filter textbox
    And eventually status will show "Topup_Completed" upon reloading the page


  Scenario: Approve request for existing card
    Given the user click the filter results for the job order number of existing card entered in filter textbox
    When he check request info of existing card
    Then the successful response is displayed once request is submitted
    And status will show "Approved" when user search for the job order number of existing card entered in the filter textbox
    And eventually status will display "Topup_Completed"