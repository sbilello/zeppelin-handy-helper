import unittest

from zeppelin_handy_helpers.utils import Formatter


class SlackFormatterTest(unittest.TestCase):
    def test_formatter(self):
        self.assertEqual(
            len(Formatter.format_slack_message([('n_id_1', 'pd_id_1', 'Finished')])['attachments'][0]['fields']),
            1)


if __name__ == '__main__':
    unittest.main()
