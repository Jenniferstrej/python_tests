# import unittest
# from mock import patch
# from exceptions import ShortRetryException


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#     @patch('dashboard.models.articles._commit_and_close_connection')
#     @patch('dashboard.models.articles._get_connection')
#     def test_process_property_message_short_retry_exception(self, mock_get_connection, mock_commit_and_close_conn):
#         mock_get_connection.return_value = fake_get_connection(FakeConnection(), FakeCursor())
#         mock_commit_and_close_conn.side_effect = None
#         attempt = self._process_property_message(message_from_process_message)
#         self.assertRaises(ShortRetryException, attempt)
#
#     def _process_property_message(self, message):
#         return lambda: process_dashboard_queue.process_property_message(message)
#
#
# if __name__ == '__main__':
#     unittest.main()
