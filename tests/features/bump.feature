Feature: Bump version strings

  Scenario: Increase patch version
    Given the version 0.1.2
      When we bump patch
      Then version is 0.1.3

  Scenario: Increase minor version
    Given the version 0.1.2
      When we bump minor
      Then version is 0.2.0

  Scenario: Increase major version
    Given the version 0.1.2
      When we bump major
      Then version is 1.0.0
