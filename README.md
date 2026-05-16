# Automated Testing Framework for Python Applications


A structured automated testing framework built with **PyTest** and **Selenium**, demonstrating assertion-based testing, reusable validation pipelines, edge-case coverage, and CI/CD integration via GitHub Actions.

---

## Project Structure

```
automated-testing-framework/
├── src/
│   ├── calculator.py        # Calculator utility module
│   └── string_utils.py      # String processing utility module
├── tests/
│   ├── conftest.py          # Shared fixtures and pytest configuration
│   ├── test_calculator.py   # 15 test cases — arithmetic, edge cases
│   └── test_string_utils.py # 16 test cases — parametrized, boundary tests
├── reports/                 # Auto-generated HTML test reports
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI pipeline
├── pytest.ini               # PyTest configuration
└── requirements.txt
```

---

## What This Framework Demonstrates

| Concept | Implementation |
|---|---|
| Assertion-based testing | `assert` statements with `pytest.approx` for floats |
| Reusable validation pipelines | `@pytest.fixture` for shared test objects |
| Parametrized edge-case testing | `@pytest.mark.parametrize` across boundary inputs |
| Exception/error scenario testing | `pytest.raises` for expected failures (e.g. divide by zero) |
| CI/CD automation | GitHub Actions runs tests on every push/PR |
| HTML test reporting | `pytest-html` generates visual test reports |

---

## Test Coverage

**test_calculator.py** — 15 test cases
- Addition: positive, negative, zero, float inputs
- Subtraction: basic, negative results, identical values
- Multiplication: zero, negatives, floats
- Division: basic, float results, **divide-by-zero edge case**
- Power and parity: zero exponent, even/odd boundary

**test_string_utils.py** — 16 test cases
- Reverse: basic, single char, empty string, palindrome
- Palindrome: parametrized with 5 cases including multi-word phrase
- Vowel count: uppercase, no-vowels, empty string
- Capitalize words: mixed case, already capitalized
- Password strength: **6 edge cases** — boundary length, missing uppercase/digit/special char

---

## Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/automated-testing-framework.git
cd automated-testing-framework
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest
```

### Run with Verbose Output

```bash
pytest -v
```

### Generate HTML Report

```bash
pytest --html=reports/test_report.html --self-contained-html
```

---

## CI/CD Pipeline

Every push to `main` triggers the GitHub Actions workflow which:
1. Sets up Python 3.11
2. Installs all dependencies
3. Runs the full test suite with PyTest
4. Generates and uploads an HTML test report as a build artifact

---

## Skills Demonstrated

`PyTest` `Selenium` `Automated Testing` `Test Case Design` `Edge-Case Testing` `Assertion-Based Testing` `CI/CD` `GitHub Actions` `Software Validation` `Debugging`

---

## Author

**Vansh Pandey**  
CSE-AIML Undergraduate, MAIT Delhi  
Intern @ ARTPARK, IISc Bengaluru  
[LinkedIn](https://linkedin.com/in/vansh-pandey-030030234) · [GitHub](https://github.com/YOUR_USERNAME)
