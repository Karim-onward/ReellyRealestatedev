# Created by karimonward at 06/05/2025
Feature: Test for change password
   input new password and confirm the button

  Scenario:  user can change password
    Given open the main page
    When login to the page
    When click on the setting_btn at the right side
    Then click on the change password button
    Then enter new password
    Then verify change password button is displayed

