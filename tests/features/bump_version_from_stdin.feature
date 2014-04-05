Feature: Bump version from stdin

  Scenario: Increase patch version from stdin
    Given we assume version 0.1.2
      When we run versionbump patch
      Then the output was 0.1.3
      And the exit code was 0

  Scenario: Increase minor version from stdin
    Given we assume version 0.1.2
      When we run versionbump minor
      Then the output was 0.2.0
      And the exit code was 0

  Scenario: Increase major version from stdin
    Given we assume version 0.1.2
      When we run versionbump major
      Then the output was 1.0.0
      And the exit code was 0

  Scenario: Run in quiet mode
    Given we assume version 0.1.2
    And we use parameter --quiet
      When we run versionbump patch
        Then there was no output
        And the exit code was 0
