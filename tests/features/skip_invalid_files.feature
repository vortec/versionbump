Feature: Skip invalid files

  Scenario: Fail if file is empty
    Given an empty file
    And we assume version 0.1.2
      When we run bump patch
      Then the file is empty
      And the exit code was 1

  Scenario: Fail if file doesn't contain a version
    Given a file that contains foobar
    And we assume version 0.1.2
      When we run bump patch
      Then the file contains foobar
      And the exit code was 1

  Scenario: Fail if file doesn't contain a version
    Given a file that contains 2.1.0
    And we assume version 0.1.2
      When we run bump patch
      Then the file contains 2.1.0
      And the exit code was 1
