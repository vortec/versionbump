Feature: Bump version in multiple files

  Scenario: Increase patch version in multiple files
    Given a file named aa.txt that contains 0.1.2
    And a file named bb.txt that contains 0.1.2
    And we assume version 0.1.2
      When we run versionbump patch
      Then the file aa.txt contains 0.1.3
      And the file bb.txt contains 0.1.3
      And the output was 0.1.3
      And the exit code was 0
