import json, os, requests


def post_reports_to_slack():
    url = "https://hooks.slack.com/services/your_key"

    # To generate report file add "> pytest_report.log" at end of py.test command for e.g. py.test -v > pytest_report.log
    test_report_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'pytest_report.log'))  # Add report file name and address here

    # Open report file and read data
    with open(test_report_file, "r") as in_file:
        testdata = ""
        for line in in_file:
            testdata = testdata + '\n' + line

    # Set Slack Pass Fail bar indicator color according to test results
    if 'FAILED' in testdata:
        bar_color = "#ff0000"
    else:
        bar_color = "#36a64f"

    # Arrange your data in pre-defined format. Test your data format here: https://api.slack.com/docs/messages/builder?
    data = {"attachments": [
        {"color": bar_color,
         "title": "Test Report",
         "text": testdata}
    ]}
    json_params_encoded = json.dumps(data)
    slack_response = requests.post(url=url, data=json_params_encoded, headers={"Content-type": "application/json"})
    if slack_response.text == 'ok':
        print
        '\n Successfully posted pytest report on Slack channel'
    else:
        print
        '\n Something went wrong. Unable to post pytest report on Slack channel. Slack Response:', slack_response