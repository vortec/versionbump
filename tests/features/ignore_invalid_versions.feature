Feature: Ignore invalid versions

  Scenario: Ignore invalid file when increasing patch version
    Given a file that contains 2.1.0
    And we assume version 0.1.2
    And we use parameter --ignore
      When we run versionbump patch
      Then the file contains 2.1.0
      And the output was 0.1.3
      And the exit code was 0

  Scenario: Ignore invalid files when increasing patch version
    Given a file named aa.txt that contains 0.1.2
    And a file named bb.txt that contains 2.1.0
    And we assume version 0.1.2
    And we use parameter --ignore
      When we run versionbump patch
      Then the file aa.txt contains 0.1.3
      And the file bb.txt contains 2.1.0
      And the output was 0.1.3
      And the exit code was 0

