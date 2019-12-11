import unittest
from parameterized import parameterized
from pyunitreport import HTMLTestRunner

from rp.validation import *
import constraints
from general import *


class TestDecimalValidation(unittest.TestCase):

    @parameterized.expand([
        ["1.23", "1", ".23", "positive", False, 0, 0, 3, 3, 2],
        [" 1.23 ", "1", ".23", "positive", False, 0, 0, 3, 3, 2],
        ["   1.23   ", "1", ".23", "positive", False, 0, 0, 3, 3, 2],
        ["+1.23", "1", ".23", "positive", True, 0, 0, 3, 3, 2],
        [" + 1.23 ", "1", ".23", "positive", True, 0, 0, 3, 3, 2],
        ["   +   1.23   ", "1", ".23", "positive", True, 0, 0, 3, 3, 2],
        ["-1.23", "1", ".23", "negative", True, 0, 0, 3, 3, 2],
        [" - 1.23 ", "1", ".23", "negative", True, 0, 0, 3, 3, 2],
        ["   -   1.23   ", "1", ".23", "negative", True, 0, 0, 3, 3, 2],
        ["0.123", "0", ".123", "positive", False, 1, 0, 3, 3, 3],
        ["000.123", "000", ".123", "positive", False, 3, 0, 3, 3, 3],
        [".123", "", ".123", "positive", False, 0, 0, 3, 3, 3],
        ["123.", "123", ".", "positive", False, 0, 0, 3, 3, 0],
        ["123.000", "123", ".000", "positive", False, 0, 3, 6, 6, 3],
           ["-0.123", "0", ".123", "negative", True, 1, 0, 3, 3, 3],
        ["-000.123", "000", ".123", "negative", True, 3, 0, 3, 3, 3],
        ["-.123", "", ".123", "negative", True, 0, 0, 3, 3, 3],
        ["-123.", "123", ".", "negative", True, 0, 0, 3, 3, 0],
        ["-123.000", "123", ".000", "negative", True, 0, 3, 6, 6, 3],
        ["0.00123", "0", ".00123", "positive", False, 1, 0, 3, 3, 5],
        ["0.0012300456", "0", ".0012300456", "positive", False, 1, 0, 8, 8, 10],
        ["0.00123000", "0", ".00123000", "positive", False, 1, 3, 6, 6, 8],
        ["0.", "0", ".", "positive", False, 1, 0, 1, 1, 0],
        [".0", "", ".0", "positive", False, 0, 1, 1, 1, 1],
        ["0.0", "0", ".0", "positive", False, 1, 1, 1, 1, 1],
        ["0.000", "0", ".000", "positive", False, 1, 3, 1, 1, 3],
        ["000.0", "000", ".0", "positive", False, 3, 1, 1, 1, 1],
        ["000.000", "000", ".000", "positive", False, 3, 3, 1, 1, 3],
        ["+0.0", "0", ".0", "positive", True, 1, 1, 1, 1, 1],
        ["-0.0", "0", ".0", "negative", True, 1, 1, 1, 1, 1],
    ])
    def test_parse(self, studentsResponse, integralPart, decimalPart, sign, signIsExplicit, nlz, ntz, nsf1, nsf2, ndp):

        parser = parsing.Parser()
        marker = parsing.Marker()

        number = parser.getParseResult(studentsResponse)

        self.assertEqual(number.type, "number")
        self.assertEqual(number.subtype, "decimalNumber")
        self.assertEqual(number.integralPart, integralPart)
        self.assertEqual(number.decimalPart, decimalPart)
        self.assertEqual(number.sign, sign)
        self.assertEqual(number.signIsExplicit, signIsExplicit)
        self.assertEqual(number.numberOfLeadingZeros, nlz)
        self.assertEqual(number.numberOfTrailingZeros, ntz)
        self.assertEqual(number.minimumNumberOfSignificantFigures, nsf1)
        self.assertEqual(number.maximumNumberOfSignificantFigures, nsf2)
        self.assertEqual(number.numberOfDecimalPlaces, ndp)

    @parameterized.expand([
       
    ])
    def test_validate(self, studentsResponse, constraints, isAccepted, normalisedStudentsResponse):

        validator = Validator()
        request = ValidationRequest()

        request.studentsResponse = studentsResponse
        request.expectedResponseType = "decimal"
        request.constraints = constraints

        response = validator.validate(request)

        self.assertEqual(response.isAccepted, isAccepted)
        self.assertEqual(response.normalisedStudentsResponse, normalisedStudentsResponse)

        print(response.messageText)

        integer = response.expression

        self.assertEqual(integer.type, "number")
        self.assertEqual(integer.subtype, "integer")


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output="example_dir"))