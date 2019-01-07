Feature: ORANGE HRM Website

 	Scenario: Verify Login for ORANGE HRM

		Given I have launch https://opensource-demo.orangehrmlive.com

		When I entered user as Admin in OrangeHRM

        And  I entered password as admin123 in OrangeHRM

        And I click login in OrangeHRM

        Then I should get loginid as Welcome Admin in OrangeHRM