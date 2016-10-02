import unittest
from mock import patch
import json
import sample_dashboard

class MyTestCase(unittest.TestCase):
    def setUp(self):
        sample_dashboard.app.config['TESTING'] = True
        self.client = sample_dashboard.app.test_client()
        pass

    @patch('requests.post')
    def test_schedule_article_publication(self, mock_requests_post):
        mock_requests_post.return_value = FakeResponse(200, {'result': 'success'})
        input = '{"articles":{"article-identifier":"03430","scheduled":"1463151540"}}'
        resp = self.client.post('/api/schedule_article_publication', data=input)
        self.assertDictEqual(json.loads(resp.data), {'result': 'success'})

    @patch('requests.post')
    def test_schedule_article_publication_error(self, mock_requests_post):
        mock_requests_post.return_value = FakeResponse(200, None)
        input = '{"articles":{"article-identifier":"03430","scheduled":"1463151540"}}'
        resp = self.client.post('/api/schedule_article_publication', data=input)
        self.assertDictEqual(json.loads(resp.data), {u'message': u'Error in scheduling service', u'detail': u'Status code from scheduler was 500'})


class FakeResponse:
    def __init__(self, status_code, response_json):
        self.status_code = status_code
        self.response_json = response_json

    def json(self):
        return self.response_json


if __name__ == '__main__':
    unittest.main()




