Feature: Approval of void request

  Background: Create void request
    Given the user search for job order number in filter textbox
    When he click the filter result
    And submit void request
    Then successful submission response should be displayed on the page
    And status should display "Pending" in void request page

  Scenario: Approve void request of new card
    Given the user search for job order number in filter textbox in void request page
    When he click the filter result
    And check the request information(top-up amount, job order number and number of cards)
    Then result should display successful submission response
    And the filtered result for job order number entered in the filter textbox should have status "Approved"
    And status display "void_topup_incomplete" in the view void request page
    And status also display "Voided" in view all request webpage