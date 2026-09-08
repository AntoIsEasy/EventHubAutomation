# EventHubAutomation
Event Hub E2E tests running against the prod environment, at:
https://eventhub.rahulshettyacademy.com/login
available demo credentials for website exploration:
  Email: eventhubdemo@yopmail.com
  Password: Eventhub1!

- Prerequisites\stack: Python 3.14, Selenium 4.46, pytest
For more details install the dependencies with "pip install -r requirements_backup.txt" (if you can't use your IDE GUI)

- Build: you can launch the tests using the command 'pytest -v -s'
or locally you can install html report with pip install pytest-html
and launch pytest -v -s --html=reports/report.html
-s will print the output
-v shows which test has been launched

- Structure: (POM) the project is composed of the test_ file(s) and of the Page Objects file(s)
Every test calls the same JSON file (Data-Driven). The key in the JSON has a peculiar name, in order
to identify clearly to which test is related. You can see at the top of any test, which key is called, from the JSON

- CI/CD: at the moment, I've been using Jenkins, but I'm planning to move the project on GitHub Actions