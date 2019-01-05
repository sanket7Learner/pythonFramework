Feature: ORANGE HRM Website

 	Scenario: Verify Login for ORANGE HRM

		Given I have launch https://opensource-demo.orangehrmlive.com

		When I enter username Admin and password admin123

        And I click login

        Then I should get user as Welcome Admin

    Scenario: Verify Fail Login for ORANGE HRM

		Given I have launch https://www.instagram.com/accounts/login/?hl=en

		When I enter username admin and password admin133

        And I click login

        Then I should get user as Welcome Admin