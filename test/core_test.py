""" core_test.py """

import unittest

from vslack import VSlack

class VSlackSetupTests(unittest.TestCase):

    def test_incoming_webhook_uri_is_required(self):
        with self.assertRaises(TypeError):
            VSlack()

    def test_icon_emoji_is_set_properly_if_passed_in(self):
        vs = VSlack('some_uri', icon_emoji=':smile:')
        self.assertEqual(':smile:', vs.icon_emoji)

    def test_username_is_set_properly_if_passed_in(self):
        vs = VSlack('some_uri', username='Bot')
        self.assertEqual('Bot', vs.username)


if __name__ == '__main__':
    unittest.main()
