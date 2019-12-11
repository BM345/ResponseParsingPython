import unittest
from parameterized import parameterized
from pyunitreport import HTMLTestRunner

from rp.validation import *
import constraints
from general import *


class TestDecimalValidation(unittest.TestCase):

    @parameterized.expand([
        ["1.23", "1", ".23", "positive", False, 0, 0, 3, 3, 2, False, False],
        [" 1.23 ", "1", ".23", "positive", False, 0, 0, 3, 3, 2, False, False],
        ["   1.23   ", "1", ".23", "positive", False, 0, 0, 3, 3, 2, False, False],
        ["+1.23", "1", ".23", "positive", True, 0, 0, 3, 3, 2, False, False],
        [" + 1.23 ", "1", ".23", "positive", True, 0, 0, 3, 3, 2, False, False],
        ["   +   1.23   ", "1", ".23", "positive", True, 0, 0, 3, 3, 2, False, False],
        ["-1.23", "1", ".23", "negative", True, 0, 0, 3, 3, 2, False, False],
        [" - 1.23 ", "1", ".23", "negative", True, 0, 0, 3, 3, 2, False, False],
        ["   -   1.23   ", "1", ".23", "negative", True, 0, 0, 3, 3, 2, False, False],
        ["0.123", "0", ".123", "positive", False, 1, 0, 3, 3, 3, False, True],
        ["000.123", "000", ".123", "positive", False, 3, 0, 3, 3, 3, False, True],
        [".123", "", ".123", "positive", False, 0, 0, 3, 3, 3, False, True],
        ["123.", "123", ".", "positive", False, 0, 0, 3, 3, 0, False, False],
        ["123.000", "123", ".000", "positive", False, 0, 3, 6, 6, 3, False, False],
        ["-0.123", "0", ".123", "negative", True, 1, 0, 3, 3, 3, False, True],
        ["-000.123", "000", ".123", "negative", True, 3, 0, 3, 3, 3, False, True],
        ["-.123", "", ".123", "negative", True, 0, 0, 3, 3, 3, False, True],
        ["-123.", "123", ".", "negative", True, 0, 0, 3, 3, 0, False, False],
        ["-123.000", "123", ".000", "negative", True, 0, 3, 6, 6, 3, False, False],
        ["0.00123", "0", ".00123", "positive", False, 1, 0, 3, 3, 5, False, True],
        ["0.0012300456", "0", ".0012300456", "positive", False, 1, 0, 8, 8, 10, False, True],
        ["0.00123000", "0", ".00123000", "positive", False, 1, 3, 6, 6, 8, False, True],
        ["0.", "0", ".", "positive", False, 1, 0, 1, 1, 0, True, True],
        [".0", "", ".0", "positive", False, 0, 1, 1, 1, 1, True, True],
        ["0.0", "0", ".0", "positive", False, 1, 1, 1, 1, 1, True, True],
        ["0.000", "0", ".000", "positive", False, 1, 3, 1, 1, 3, True, True],
        ["000.0", "000", ".0", "positive", False, 3, 1, 1, 1, 1, True, True],
        ["000.000", "000", ".000", "positive", False, 3, 3, 1, 1, 3, True, True],
        ["+0.0", "0", ".0", "positive", True, 1, 1, 1, 1, 1, True, True],
        ["-0.0", "0", ".0", "negative", True, 1, 1, 1, 1, 1, True, True],
    ])
    def test_parse(self, studentsResponse, integralPart, decimalPart, sign, signIsExplicit, nlz, ntz, nsf1, nsf2, ndp, isZero, integralPartIsZero):

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
        self.assertEqual(number.isZero, isZero)
        self.assertEqual(number.integralPartIsZero, integralPartIsZero)

    @parameterized.expand([
        ["1.23", {}, True, "1.23"],
        ["1.23", constraints.allowLeadingZeros, True, "1.23"],
        ["1.23", constraints.mustNotHavePlus, True, "1.23"],
        ["1.23", constraints.mustHavePlus, False, "1.23"],
        [" 1.23 ", {}, True, "1.23"],
        ["   1.23   ", constraints.allowLeadingZeros, True, "1.23"],
        [" 1.23 ", constraints.mustNotHavePlus, True, "1.23"],
        ["   1.23   ", constraints.mustHavePlus, False, "1.23"],
        ["001.23", {}, False, "001.23"],
        ["001.23", constraints.allowLeadingZeros, True, "001.23"],
        ["0.12", {}, True, "0.12"],
        ["0.12", constraints.allowLeadingZeros, True, "0.12"],
        [".12", {}, True, "0.12"],
        [".12", constraints.allowLeadingZeros, True, "0.12"],
        ["00.12", {}, False, "00.12"],
        ["00.12", constraints.allowLeadingZeros, True, "00.12"],
    ])
    def test_validate(self, studentsResponse, constraints, isAccepted, normalisedStudentsResponse):

        print "\"{0}\"".format( studentsResponse)

        validator = Validator()
        request = ValidationRequest()

        request.studentsResponse = studentsResponse
        request.expectedResponseType = "decimal"
        request.constraints = constraints

        response = validator.validate(request)

        self.assertEqual(response.isAccepted, isAccepted)
        self.assertEqual(response.normalisedStudentsResponse, normalisedStudentsResponse)

        print(response.messageText)


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output="example_dir"))
