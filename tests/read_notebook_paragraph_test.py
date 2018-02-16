import unittest

from mock import patch

from zeppelin_handy_helpers.handlers import NPhandler

### Test experiment for mocking
class NPreadtest(unittest.TestCase):
    @patch('zeppelin_handy_helpers.handlers.NPhandler.get_notebook')
    def test_get_notebook(self, mock_response):
        mock_response.return_value = 'Ciao'
        self.assertEqual('Ciao', NPhandler.get_notebook('test', 'test'))

if __name__ == '__main__':
    unittest.main()