import unittest
from mock import patch
from session_usage import ExpandArticle


class MyTestCase(unittest.TestCase):

    @patch('session.Session')
    def test_do_activity_invalid_version(self, mock_session):
        expandarticle = ExpandArticle()
        mock_session.return_value = FakeSession(session_example)

        success = expandarticle.do_activity(data_invalid_version)
        self.assertEqual(False, success)


session_example = {
            'version': '1',
            'article_id': '00353',
            'run': '1ee54f9a-cb28-4c8e-8232-4b317cf4beda',
            'expanded_folder': '00353.1/1ee54f9a-cb28-4c8e-8232-4b317cf4beda',
            'update_date': '2012-12-13T00:00:00Z'
        }

data_invalid_version = {u'event_time': u'2016-06-07T10:45:18.141126Z',
                                       u'event_name': u'ObjectCreated:Put',
                                       u'file_name': u'elife-00353-vor-v-1-20121213000000.zip',
                                       u'file_etag': u'1e17ebb1fad6c467fce9cede16bb752f',
                                       u'bucket_name': u'jen-elife-production-final',
                                       u'file_size': 1097506}

class FakeSession:

    def __init__(self, fake_session):
        self.session_dict = fake_session

    def store_value(self, execution_id, key, value):
        self.session_dict[key] = value

    def get_value(self, execution_id, key):
        try:
            return self.session_dict[key]
        except:
            return None


if __name__ == '__main__':
    unittest.main()
