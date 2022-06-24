Feature: Finding the sum of two integers for a given target

  Scenario: A list of 5 numbers where only two indices sum up to the target
    Given I have a list of numbers "2,8,11,13,21"
    When I find two indices whose sum is "24"
    Then the answer should be "2, 3"


