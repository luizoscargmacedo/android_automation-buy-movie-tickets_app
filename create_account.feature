Feature: Validate NEW USER REGISTER
    As a user would like to create an account and validate all information


    
    Scenario: Create account and validate profile information (TELBZL-1184)
          Given already screen apresentation app
          When tap in button NEW USER REGISTER
          And fill all information
          | email          | password              | confirm_password  |
          | $email_random  | Knight_Rider_85@*     | Knight_Rider_85@* |
          And tap in button NEXT
          And fill the personal information fields
          | name          | nickname          | id         | x_mobile_number          | switch_greater_than_eighteen |
          | $name_random  | $nickname_random  | $id_random | $x_mobile_number_random  |  True                        |
          And verify if all information are correct
          Then button REGISTER must be enabled and tap it
