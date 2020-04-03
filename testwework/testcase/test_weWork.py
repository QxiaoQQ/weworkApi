from testwework.api.WeWork import WeWork
from unittest import TestCase


class TestWework:
    def test_get_token(self):
        wework = WeWork()
        Token = wework.get_token()
        print(wework.get_token())
        assert Token != None

        wework.get_token()
        assert Token != None

        wework.get_token()
        assert Token != None
