Feature: Bump version in a file

  Scenario: Increase patch version in a file
    Given a file that contains 0.1.2
    And we assume version 0.1.2
      When we run versionbump patch
      Then the file contains 0.1.3
      And the output was 0.1.3
      And the exit code was 0

  Scenario: Increase minor version in a file
    Given a file that contains 0.1.2
    And we assume version 0.1.2
      When we run versionbump minor
      Then the file contains 0.2.0
      And the output was 0.2.0
      And the exit code was 0

  Scenario: Increase major version in a file
    Given a file that contains 0.1.2
    And we assume version 0.1.2
      When we run versionbump major
      Then the file contains 1.0.0
      And the output was 1.0.0
      And the exit code was 0
