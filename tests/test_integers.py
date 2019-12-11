import unittest
from parameterized import parameterized
from pyunitreport import HTMLTestRunner

from rp.validation import *
import constraints


def merge(d1, d2):
    a = d1.copy()
    a.update(d2)
    return a


class TestIntegerValidation(unittest.TestCase):

    @parameterized.expand([
        ["123", "123", "", "positive", False, 0, 0, 3, 3, 0],
        [" 123 ", "123", "", "positive", False, 0, 0, 3, 3, 0],
        ["   123   ", "123", "", "positive", False, 0, 0, 3, 3, 0],
        ["00123", "00123", "", "positive", False, 2, 0, 3, 3, 0],
        ["   00123   ", "00123", "", "positive", False, 2, 0, 3, 3, 0],
        ["+123", "123", "", "positive", True, 0, 0, 3, 3, 0],
        ["   +   123   ", "123", "", "positive", True, 0, 0, 3, 3, 0],
        ["-123", "123", "", "negative", True, 0, 0, 3, 3, 0],
        ["   -   123   ", "123", "", "negative", True, 0, 0, 3, 3, 0],
        ["-00123", "00123", "", "negative", True, 2, 0, 3, 3, 0],
        ["-0012300", "0012300", "", "negative", True, 2, 0, 3, 5, 0],
        ["-0012300456", "0012300456", "", "negative", True, 2, 0, 8, 8, 0],
        ["0", "0", "", "positive", False, 1, 0, 1, 1, 0],
        ["   0   ", "0", "", "positive", False, 1, 0, 1, 1, 0],
        ["000", "000", "", "positive", False, 3, 0, 1, 1, 0],
        ["   000   ", "000", "", "positive", False, 3, 0, 1, 1, 0],
        ["+0", "0", "", "positive", True, 1, 0, 1, 1, 0],
        ["   +   0   ", "0", "", "positive", True, 1, 0, 1, 1, 0],
        ["-0", "0", "", "negative", True, 1, 0, 1, 1, 0],
        ["   -   0   ", "0", "", "negative", True, 1, 0, 1, 1, 0]
    ])
    def test_parse(self, studentsResponse, integralPart, decimalPart, sign, signIsExplicit, nlz, ntz, nsf1, nsf2, ndp):

        parser = parsing.Parser()
        marker = parsing.Marker()

        integer = parser.getParseResult(studentsResponse)

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

    @parameterized.expand([
        ["123", {}, True, "123"],
        ["123", constraints.allowLeadingZeros, True, "123"],
        ["123", constraints.mustNotHavePlus, True, "123"],
        ["123", constraints.mustHavePlus, False, "123"],
        [" 123 ", {}, True, "123"],
        ["   123   ", constraints.allowLeadingZeros, True, "123"],
        [" 123 ", constraints.mustNotHavePlus, True, "123"],
        ["   123   ", constraints.mustHavePlus, False, "123"],
        ["00123", {}, False, "00123"],
        ["00123", constraints.allowLeadingZeros, True, "00123"],
        ["+123", {}, False, "+123"],
        ["+123", constraints.mustNotHavePlus, False, "+123"],
        ["+123", constraints.mustHavePlus, True, "+123"],
        [" + 123 ", {}, False, "+123"],
        ["   +   123   ", constraints.mustNotHavePlus, False, "+123"],
        ["   +   123   ", constraints.mustHavePlus, True, "+123"],
        ["-123", {}, True, "-123"],
        ["-123", constraints.mustNotHavePlus, True, "-123"],
        ["-123", constraints.mustHavePlus, True, "-123"],
        [" - 123 ", {}, True, "-123"],
        ["   -   123   ", constraints.mustNotHavePlus, True, "-123"],
        ["   -   123   ", constraints.mustHavePlus, True, "-123"],
        ["+00123", {}, False, "+00123"],
        ["+00123", constraints.allowLeadingZeros, False, "+00123"],
        ["+00123", constraints.mustHavePlus, False, "+00123"],
        ["+00123", merge(constraints.allowLeadingZeros, constraints.mustHavePlus), True, "+00123"],
        ["-00123", {}, False, "-00123"],
        ["-00123", constraints.allowLeadingZeros, True, "-00123"],
        ["-00123", constraints.mustHavePlus, False, "-00123"],
        ["-00123", merge(constraints.allowLeadingZeros, constraints.mustHavePlus), True, "-00123"],
        ["0", {}, True, "0"],
        [" 0 ", {}, True, "0"],
        ["0", constraints.allowLeadingZeros, True, "0"],
        ["0", constraints.mustNotHavePlus, True, "0"],
        ["0", constraints.mustHavePlus, False, "0"],
        ["+0", {}, False, "0"],
        ["   +   0   ", {}, False, "0"],
        ["+0", constraints.mustNotHavePlus, False, "0"],
        ["+0", constraints.mustHavePlus, True, "0"],
        ["123", constraints.mustHaveAtLeast3SF, True, "123"],
        ["12300", constraints.mustHaveAtLeast3SF, True, "12300"],
        ["12345", constraints.mustHaveAtLeast3SF, True, "12345"],
        ["120", constraints.mustHaveAtLeast3SF, True, "120"],
        ["100", constraints.mustHaveAtLeast3SF, True, "100"],
        ["123", constraints.mustHaveAtLeast5SF, False, "123"],
        ["12345", constraints.mustHaveAtLeast5SF, True, "12345"],
        ["12", constraints.mustHaveAtLeast3SF, False, "12"],
        ["012", merge(constraints.mustHaveAtLeast3SF, constraints.allowLeadingZeros), False, "012"],
        ["123", constraints.mustHaveNoMoreThan3SF, True, "123"],
        ["120", constraints.mustHaveNoMoreThan3SF, True, "120"],
        ["100", constraints.mustHaveNoMoreThan3SF, True, "100"],
        ["12345", constraints.mustHaveNoMoreThan6SF, True, "12345"],
        ["1000", constraints.mustHaveNoMoreThan3SF, True, "1000"],
        ["123000", constraints.mustHaveNoMoreThan3SF, True, "123000"],
        ["1234", constraints.mustHaveNoMoreThan3SF, False, "1234"],
        ["1234567", constraints.mustHaveNoMoreThan6SF, False, "1234567"],
        ["12300", constraints.mustHaveExactly3SF, True, "12300"],
        ["12000", constraints.mustHaveExactly3SF, True, "12000"],
        ["10000", constraints.mustHaveExactly3SF, True, "10000"],
        ["12340", constraints.mustHaveExactly3SF, False, "12340"],
        ["1230", constraints.mustHaveExactly5SF, False, "1230"],
        ["12300", constraints.mustHaveExactly5SF, True, "12300"],
        ["12345", constraints.mustHaveExactly5SF, True, "12345"],
        ["123456", constraints.mustHaveExactly5SF, False, "123456"],
    ])
    def test_validate(self, studentsResponse, constraints, isAccepted, normalisedStudentsResponse):

        validator = Validator()
        request = ValidationRequest()

        request.studentsResponse = studentsResponse
        request.expectedResponseType = "integer"
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
