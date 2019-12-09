import unittest
from parameterized import parameterized

import sys

sys.path.append("../rp")

from validation import *


class TestIntegerValidation(unittest.TestCase):

    @parameterized.expand([
        ["123", "integer", "123"],
        ["+123", "integer", "+123"]
    ])
    def test_1(self, a, b, c):

        validator = Validator()

        request = ValidationRequest()

        request.studentsResponse = a
        request.expectedResponseType = b

        response = validator.validate(request)

        self.assertTrue(response.isAccepted)
        self.normalisedStudentsResponse = c

if __name__ == "__main__":
    unittest.main()
