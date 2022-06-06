Website: https://selenium1py.pythonanywhere.com

For running of tests:
1. Clone the repository;
2. Activate test env;
3. Install all requirements from requirements.txt run: pip install -r requirements.txt
4. Run: 'pytest', if you want to run all tests

To run tests and send results to Slack:
1. in post_test_reports_to_slack.py: Add the Incoming WebHook URL
2. Run: pytest -v -I Y > pytest_report.log

To run tests and send results to TestRail:
1. in testreil_config.cfg: Add your url, email, password
2. Run: pytest --testrail --tr-config=testreil_config.cfg