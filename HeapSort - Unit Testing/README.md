# Unit testing of HeapSort code using PyTest

## Pytest

**Source:**
pytest is a third-party Python testing
framework that requires manual installation.

**Test Discovery:**
Based on naming
conventions, pytest can automatically find and
run test functions and classes. This reduces the
requirement for explicit setting and speeds up
the testing procedure.

**Parameterized Testing:**
To execute the same
test function with various input values or
settings, pytest enables parameterized testing.
Without having to duplicate test code, this
functionality is helpful for evaluating many
scenarios, including edge cases.

**Syntax:** 
Pytest makes it simple and needs little
boilerplate code to create test functions.
Assertions can be used in test routines to verify
anticipated behavior, and they can be built
using standard Python functions.

**Assertions:** A variety of built-in assertion
procedures provided by pytest make it simple to confirm anticipated results in our tests. Clear
failure warnings from assertion introspection
enable rapid problem diagnosis.

**Fixtures:** Pytest's fixtures let us create and
control the testing context. They offer a
method for creating and sharing resources,
such as database connections or test data,
amongst several tests.

**Plugins and Extensibility:** A wide variety of
plugins are available for pytest, which can
improve its capabilities. These plugins may be
used to personalize test discovery, provide
thorough reports, interface with other tools,
and more.

**Parallel Test Execution:** Large test suites can
benefit greatly from pytest's parallel test
execution capability, which makes use of
many CPU cores to speed up test execution.

**Output and Reporting:** During test
execution, pytest produces thorough and
instructive output, highlighting specific test
results and any errors. For enhanced visibility,
several reporting alternatives may be created,
including JUnit XML and HTML reports.

**Integration with Continuous Integration
(CI):** To make sure that new code changes
don't cause regressions, pytest is frequently
used in CI/CD processes. It works nicely with
well-known CI platforms like CircleCI, Travis
CI, Jenkins, and more.
