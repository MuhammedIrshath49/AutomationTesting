Feature: Cancellation of void request

  Background: Create void request
    Given the user enter job order number in filter textbox
    When he click on the filter result
    And submit the void request
    Then respose should be successful
    And status should display as "Pending" in void request page


  Scenario: Cancel void request of new card
    Given the user enter job order number in filter textbox in void request page
    When he click the filtered result
    And check the topup request information(top-up amount, job order number and number of cards)
    And reject request with acceptable reason
    Then result should display rejected submission response
    And the filtered result  should have status "Cancelled"

