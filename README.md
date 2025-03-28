# Pytest Framework: Setup, Execution, and Git Integration

This repository contains my learning notes and commands related to **Pytest**, a powerful Python testing framework.

## Topics Covered

- Installing pytest
- Identifying test files and test functions
- Executing all test files using:
  ```sh
  pytest -v

Executing a specific file:

pytest <filename> -v

Executing tests by substring matching:

pytest -k <substring> -v

Executing tests based on markers:

pytest -m <marker_name> -v

Creating fixtures using:

@pytest.fixture

Using conftest.py to access fixtures from multiple files

Parameterizing tests using:

@pytest.mark.parametrize

Marking tests as expected failures using:

@pytest.mark.xfail

Skipping tests using:

@pytest.mark.skip

Stopping test execution after n failures:

pytest --maxfail=<num>

Running tests in parallel:

pytest -n <num>

Generating test results in XML format:

pytest -v --junitxml="result.xml"


Future Goals

Gain hands-on experience by writing real-world test cases.

Learn Pytest plugins for enhanced functionality.

Improve understanding of test automation frameworks.

Practice mocking and patching with Pytest.

Work on open-source contributions using Pytest.
