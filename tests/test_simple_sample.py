import unittest
from simple_sample import activity_ConvertJATS
import json

json_output_parameter_example_string = open(
"tests/test_data/ConvertJATS_json_output_for_add_update_date_to_json.json","r").read()
json_output_return_example = json.loads(
    open("tests/test_data/ConvertJATS_add_update_date_to_json_return.json","r").read())

class MyTestCase(unittest.TestCase):

    def test_add_update_to_json(self):
        self.jats = activity_ConvertJATS()
        json_output_result = self.jats.add_update_date_to_json(json_output_parameter_example_string,
                                                                '2012-12-13T00:00:00Z',
                                                                None)
        self.assertDictEqual(json.loads(json_output_result),json_output_return_example)

if __name__ == '__main__':
    unittest.main()
