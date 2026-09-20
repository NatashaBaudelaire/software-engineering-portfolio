# Software Testing

Exercises on software testing techniques: manual test execution, test case
design and automated unit testing with JUnit 5.

## Directory Structure

### `manual-testing`

A candidate-status program (`CandidateStatus.java`) used as the subject for
manual test execution (test cases, bug reports and exploratory testing by
hand).

### `test-case-design`

A vehicular device simulation (`vehiculardevice/`):

- `VehicularDevice.java` - class under test (speed/gear logic)
- `Comments.java` - documentation of design decisions
- `VehicularDeviceTest.java` - test cases with boundary value analysis and
  equivalence partitioning
- `VehicularDeviceTestSuite.java` - JUnit test suite

### `unit-testing`

A calculator (`calculator/`) with automated unit tests written in JUnit 5:

- `Calculator.java` - arithmetic operations under test
- `CalculatorTest.java` - JUnit 5 unit test class

## How to Run (JUnit 5)

```bash
# Compile the class under test and the tests
javac -cp junit-jupiter-api.jar:. VehicularDevice.java VehicularDeviceTest.java

# Run the tests (example with the JUnit Platform Console Standalone)
java -jar junit-platform-console-standalone.jar \
  --class-path . --select-class VehicularDeviceTest
```

## Learning Objectives

- Manual test execution and documentation
- Test case design: boundary value analysis, equivalence partitioning
- Automated unit tests with JUnit 5
- `assertEquals`/`assertFalse` style assertions and test isolation