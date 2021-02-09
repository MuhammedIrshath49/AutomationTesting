Feature: Rejection of top up requests

  Background: Access to EZ-Link's View Top Up Request Page
    Given the user search for EZ-Link's Portal
    When he enter login credentials
    Then he should be able to access View All Top Up Requests page


  Scenario: Reject request for new card
    Given the user click the filter results for the job order number of new card
    When he check top-up information
    And reject the request with valid reason
    Then result will show success message
    And status will show "Returned" when user search for the job order number of new card entered in the filter textbox



  Scenario: Reject request for existing card
    Given the user click the filter results for the job order number of existing card
    When he check top-up request information
    And reject the request with proper reason
    Then submission will be successful
    And status will show "Returned" when user search for the job order number of existing card entered in the filter textbox