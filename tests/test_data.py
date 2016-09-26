
class FakeResponse:
    def __init__(self, status_code, response_json):
        self.status_code = status_code
        self.response_json = response_json

    def json(self):
        return self.response_json


request_scheduled_article_publication = FakeResponse(200, {'result': 'success'})
request_scheduled_status_500 = FakeResponse(500, None)

json_output_parameter_example_string = open("tests/test_data/ConvertJATS_json_output_for_add_update_date_to_json.json", "r").read()