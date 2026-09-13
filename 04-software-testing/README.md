# Software Testing

This directory contains software testing exercises covering various testing methodologies and practices. These exercises were completed as part of my learning journey in software quality assurance and testing.

## Directory Structure

### 📁 manual-testing
Manual testing techniques and procedures.

**Content:**
- Test case creation and execution
- Test scenario planning
- Bug reporting and documentation
- User acceptance testing procedures
- Exploratory testing techniques

### 📁 test-case-design
Test case design principles and methodologies.

**Content:**
- Test case design techniques
- Boundary value analysis
- Equivalence partitioning
- Decision table testing
- State transition testing
- Use case testing

### 📁 unit-testing
Automated unit testing implementation.

**Content:**
- Unit testing frameworks (JUnit, pytest, etc.)
- Test-driven development (TDD) practices
- Mock and stub implementation
- Test coverage analysis
- Automated test execution

## Learning Objectives

These exercises cover fundamental software testing concepts:

- **Testing Fundamentals**: Understanding testing principles and objectives
- **Test Planning**: Creating comprehensive test plans
- **Test Design**: Designing effective test cases
- **Manual Testing**: Performing manual test execution
- **Automated Testing**: Implementing automated test suites
- **Test Documentation**: Creating test reports and documentation
- **Quality Assurance**: Understanding QA processes and methodologies

## Testing Methodologies Covered

### Manual Testing
- **Black Box Testing**: Testing without knowledge of internal code
- **White Box Testing**: Testing with knowledge of internal structure
- **Gray Box Testing**: Combination of black and white box approaches
- **Exploratory Testing**: Simultaneous learning and testing

### Test Design Techniques
- **Boundary Value Analysis**: Testing at boundaries of input ranges
- **Equivalence Partitioning**: Dividing inputs into equivalence classes
- **Decision Table Testing**: Testing complex business logic
- **State Transition Testing**: Testing system state changes

### Unit Testing
- **Test Isolation**: Testing individual components
- **Mocking**: Simulating dependencies
- **Test Coverage**: Measuring code coverage
- **Test Maintenance**: Keeping tests updated

## How to Use

### Manual Testing Exercises

1. Review the test scenario documentation
2. Understand the requirements and acceptance criteria
3. Create test cases based on the design techniques
4. Execute tests manually and document results
5. Report any bugs or issues found

### Test Case Design Exercises

```bash
# Navigate to test-case-design directory
cd test-case-design

# Review the requirements document
# Apply appropriate design techniques:
# - Boundary value analysis
# - Equivalence partitioning
# - Decision tables
# - State transition diagrams

# Create test cases following the templates provided
```

### Unit Testing Exercises

#### Java (JUnit)
```bash
# Navigate to unit-testing directory
cd unit-testing

# For Java projects with JUnit:
# Compile tests
javac -cp junit.jar:. TestClass.java

# Run tests
java -cp junit.jar:. org.junit.runner.JUnitCore TestClass
```

#### Python (pytest)
```bash
# Navigate to unit-testing directory
cd unit-testing

# Install pytest
pip install pytest

# Run tests
pytest test_file.py

# Run with coverage
pytest --cov=module test_file.py
```

## Testing Tools and Frameworks

### Manual Testing Tools
- **Test Management**: JIRA, TestRail, Zephyr
- **Bug Tracking**: Bugzilla, Mantis, GitHub Issues
- **Screen Recording**: OBS Studio, Loom for bug demonstrations

### Automated Testing Tools
- **Java**: JUnit, TestNG, Mockito
- **Python**: pytest, unittest, nose2
- **JavaScript**: Jest, Mocha, Jasmine
- **Coverage Tools**: JaCoCo, coverage.py

## Best Practices

- **Test Early**: Start testing as early as possible in development
- **Test Frequently**: Run tests regularly during development
- **Test Independently**: Each test should be independent
- **Test thoroughly**: Aim for high test coverage
- **Document Clearly**: Maintain clear test documentation
- **Automate Repetitive Tasks**: Automate repetitive test cases
- **Review and Refactor**: Regularly review and refactor tests

## Common Issues

### Test Failures
- Verify test environment setup
- Check for flaky tests (non-deterministic failures)
- Review test data and dependencies
- Ensure tests are isolated and independent

### Maintenance Challenges
- Keep tests updated with code changes
- Remove obsolete tests
- Refactor test code for maintainability
- Monitor test execution time

### Coverage Issues
- Aim for meaningful coverage, not just high percentages
- Focus on critical business logic
- Test edge cases and error conditions
- Review coverage reports regularly

## Testing Metrics

- **Test Coverage**: Percentage of code covered by tests
- **Pass Rate**: Percentage of tests passing
- **Defect Density**: Number of defects per unit of code
- **Test Execution Time**: Time taken to run test suite
- **Defect Leakage**: Defects found in production vs. testing

## Next Steps

After completing these exercises, consider:
- Learning integration testing
- Exploring end-to-end testing
- Studying performance testing
- Understanding security testing
- Learning about continuous integration testing
- Exploring API testing tools (Postman, REST Assured)

## Resources

- [ISTQB Foundation Level Certification](https://www.istqb.org/)
- [JUnit Documentation](https://junit.org/junit5/)
- [pytest Documentation](https://docs.pytest.org/)
- [Software Testing Help](https://www.softwaretestinghelp.com/)
