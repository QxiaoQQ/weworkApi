from testwework.utils.Utils import Utils


class TestUtils:
    def test_format(self):
        print(Utils.format({"a": 1, "b": {"c": "xxx"}}))

