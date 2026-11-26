# EventHubAutomation

-Badge set up: it shows the result of the last test run (non-technical users)
[![Tests](https://github.com/AntoIsEasy/EventHubAutomation/actions/workflows/tests.yml/badge.svg)](https://github.com/AntoIsEasy/EventHubAutomation/actions/workflows/tests.yml)
- Report: HTML report can be found and downloaded in the job logs. Screenshot added when a test fails.

Event Hub E2E tests running against the prod environment, at:
https://eventhub.rahulshettyacademy.com/login
available demo credentials for website exploration:
  Email: eventhubdemo@yopmail.com
  Password: Eventhub1!

- Prerequisites\stack: Python 3.14, Selenium 4.46, pytest, requests
For more details install the dependencies with "pip install -r requirements_backup.txt" (if you can't use your IDE GUI)

- Build: you can launch the tests using the command 'pytest -v -s'
or locally you can install html report with pip install pytest-html
and launch pytest -v -s --html=reports/report.html
-s will print the output log
-v shows which tests have been launched and shows the status (passed/failed)

- Structure: (POM) the project is composed of the test_ file(s) and of the Page Objects file(s)
Every test calls the same JSON file (Data-Driven). The key in the JSON has a peculiar name, in order to identify clearly to which test is related. You can see at the top of any test, which key is called, from the JSON

- CI/CD: I've been using Jenkins, but I'm planning to move the project on GitHub Actions. UPDATE: added GitHub Actions.

- Some tests may need fresh input data to make it work properly (must be added manually)