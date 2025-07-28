# Created by karimonward at 16/07/2025
Feature:  Test for filtering price
   filter the products by price range 1200000 to 2000000

  Scenario: user can filter price range
    Given the user is on the main page
    When the user logs into the page
    When click on the off_plan_button
    When click on the filter_button
    Then enter minimum price 120000
    Then enter maximum price 20000000
    Then click on the show_results_btn
    #Then verify the price text

