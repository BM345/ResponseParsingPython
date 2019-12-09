import unittest
from parameterized import parameterized

import sys

sys.path.append("../rp")

from validation import *


class TestIntegerValidation(unittest.TestCase):

    @parameterized.expand([
        ["123", True, "123", "", "positive", False, 0, 0, 3, 3, 0, "123"],
        ["+123", True, "123", "", "positive", True, 0, 0, 3, 3, 0, "+123"],
        ["-123", True, "123", "", "negative", True, 0, 0, 3, 3, 0, "-123"],
        ["-00123", True, "00123", "", "negative", True, 2, 0, 3, 3, 0, "-00123"],
        ["-0012300", True, "0012300", "", "negative",
            True, 2, 0, 3, 5, 0, "-0012300"],
        ["-0012300456", True, "0012300456", "", "negative",
            True, 2, 0, 8, 8, 0, "-0012300456"],
        ["0", True, "0", "", "zero", False, 1, 0, 1, 1, 0, "0"],
        ["000", True, "000", "", "zero", False, 3, 0, 1, 1, 0, "000"],
        ["+0", True, "0", "", "zero", True, 1, 0, 1, 1, 0, "0"],
        ["-0", True, "0", "", "zero", True, 1, 0, 1, 1, 0, "0"]
    ])
    def test_accept(self, studentsResponse, isAccepted, integralPart, decimalPart, sign, signIsExplicit, nlz, ntz, nsf1, nsf2, ndp, asciiMath):

        validator = Validator() 
        request = ValidationRequest()

        request.studentsResponse = studentsResponse
        request.expectedResponseType = "integer"

        response = validator.validate(request)

        self.assertTrue(response.isAccepted)

        integer = response.expressionTree

        self.assertEqual(integer.type, "number")
        self.assertEqual(integer.subtype, "integer")
        self.assertEqual(integer.integralPart, integralPart)
        self.assertEqual(integer.decimalPart, decimalPart)
        self.assertEqual(integer.sign, sign)
        self.assertEqual(integer.signIsExplicit, signIsExplicit)
        self.assertEqual(integer.numberOfLeadingZeros, nlz)
        self.assertEqual(integer.numberOfTrailingZeros, ntz)
        self.assertEqual(integer.minimumNumberOfSignificantFigures, nsf1)
        self.assertEqual(integer.maximumNumberOfSignificantFigures, nsf2)
        self.assertEqual(integer.numberOfDecimalPlaces, ndp)
        self.assertEqual(integer.asciiMath, asciiMath)


if __name__ == "__main__":
    unittest.main()
