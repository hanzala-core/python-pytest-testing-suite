# Python Pytest Testing Suite

A hands-on Python project demonstrating automated testing
and software reliability using Pytest.

## Features

- Unit testing
- Parameterized testing
- Boundary value analysis
- Reusable fixtures
- Exception handling
- Database mocking
- SMS notification mocking
- Expected failure testing

## Project Structure

    bank.py
    calculator.py
    pytest.ini
    requirements.txt
    tests/
        conftest.py
        test_bank.py
        test_calculator.py
        test_db_mock.py

## Installation

    python -m venv venv

    .\venv\Scripts\python.exe -m pip install -r requirements.txt

## Run Tests

    .\venv\Scripts\python.exe -m pytest -v

## Test Results

| Status | Count |
|--------|-------|
| Total | 27 |
| Passed | 26 |
| Expected Failure | 1 |
| Unexpected Failure | 0 |

The expected failure demonstrates a known issue
with negative withdrawal validation.

## Technologies

Python, Pytest, Git and GitHub.
