# EventHub Test Automation

[![Tests](https://github.com/AntoIsEasy/EventHubAutomation/actions/workflows/tests.yml/badge.svg)](https://github.com/AntoIsEasy/EventHubAutomation/actions/workflows/tests.yml)

Test automation for [EventHub](https://eventhub.rahulshettyacademy.com/login), a practice event-booking web application by Rahul Shetty Academy. The suite combines Selenium UI tests with REST API calls for test setup and verification.

## Tech stack

- Python 3.14
- Selenium 4.46
- pytest and pytest-html
- requests
- GitHub Actions

## Highlights

- **Page Object Model**: locators and page actions are kept separate from test logic.
- **API + UI testing**: the API creates fresh users and retrieves the expected values checked in the UI.
- **Data-driven tests**: test data is stored in JSON and injected with `pytest.mark.parametrize`.
- **Repeatable registration**: unique email addresses are generated with `uuid`.
- **Failure diagnostics**: a pytest hook attaches a screenshot to the HTML report when a test fails.
- **Continuous integration(CI)**: the suite runs in headless Chrome on every push to `main`.

## Test cases

| ID  | Scenario | What is verified |
|-----|----------|------------------|
| TC1 | Invalid login | An error message appears for a wrong email or password |
| TC2 | New user registration | The user is logged in and redirected to the home page |
| TC3 | Already registered user | The "Email already registered" message appears |
| TC4 | Booking form validation | Errors appear for invalid name, email and phone number |
| TC5 | Maximum tickets | The ticket counter matches the value expected from the API |
| TC6 | Clear bookings | All bookings are removed and the empty state is shown |

## Project structure

```
├── .github/workflows/   # CI pipeline
├── ApiUtils/            # API helper class
├── Data/                # JSON test data
├── E2Etest/             # Test cases and pytest fixtures
├── PageObjects/         # Page Object classes
├── Utils/               # Shared base class for page objects
├── pytest.ini
└── requirements.txt
```

## Getting started

Requirements: Python 3.14 and Google Chrome.

## Running the tests

Bash

pytest -v --html=reports/report.html --self-contained-html       # with HTML report


## CI and reports

The GitHub Actions workflow runs on every push to `main` and can also be started manually. Each run publishes the HTML report as a downloadable artifact named `html-report`, available on the run summary page.

## Known limitations

- Tests run against a shared public environment, so results depend on its availability and data.
- TC5 reads the seat availability of a fixed event ID.

## Roadmap for further improvement

- Create test preconditions through the API
- Remove the fixed event ID in TC5
- Move the base URL to a configuration file
- Replace implicit waits with explicit waits
- Run tests in parallel
