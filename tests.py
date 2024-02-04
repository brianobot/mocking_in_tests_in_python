import unittest
from unittest import TestCase, mock

from main import SomeClass


class TestSomeClass(TestCase):
    def test_public_method(self):
        obj = SomeClass()
        # this replaces the _hidden_method of the someclass instance with
        # a mock object, while in this context, references to the replaced
        # method/attribute would reference the mock method
        obj._hidden_method = mock.MagicMock()
        # the return value indicated the value to be returned
        # when the attribute is called like a function/method
        obj._hidden_method.return_value = 10
        result = obj.public_method(5)
        self.assertEqual(15, result, "return value from public method is incorrect")


if __name__ == "__main__":
    unittest.main()
