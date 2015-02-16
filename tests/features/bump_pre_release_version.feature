Feature: Handle pre release tags

  Scenario: Introduce pre-release from stdin
    Given we assume version 0.1.2
      When we run versionbump pre
      Then the output was 0.1.3-dev.0
      And the exit code was 0

  Scenario: Introduce pre-release with custom label from stdin
    Given we assume version 0.1.2
    And we asusume label alpha
      When we run versionbump pre
      Then the output was 0.1.3-alpha.0
      And the exit code was 0

  Scenario: Increase pre-release version from stdin
    Given we assume version 0.1.3-alpha.0
      When we run versionbump pre
      Then the output was 0.1.3-alpha.1
      And the exit code was 0

  Scenario: Remove pre-release from stdin
    Given we assume version 0.1.3-alpha.0
      When we run versionbump minor
      Then the output was 0.2.0
      And the exit code was 0

  Scenario: Increase pre-release version in a file
    Given a file that contains 0.1.3-alpha.2
    And we assume version 0.1.3-alpha.2
      When we run versionbump pre
      Then the file contains 0.1.3-alpha.3
      And the output was 0.1.3-alpha.3
      And the exit code was 0

  Scenario: Remove pre-release in a file
     Given we assume version 0.1.3-alpha.0
       When we run versionbump minor
       Then the output was 0.2.0
       And the exit code was 0
