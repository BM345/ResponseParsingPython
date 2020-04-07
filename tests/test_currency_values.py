import unittest
from parameterized import parameterized
from pyunitreport import HTMLTestRunner

import sys

sys.path.append("../rp")

from validation import *
import constraints
from general import *


class TestCurrencyValueValidation(unittest.TestCase):

    @parameterized.expand([
        ["12", constraints.dollars, True, "12"],
        ["12.", constraints.dollars, True, "12"],
        ["12.", merge(constraints.dollars, constraints.dontRemoveTrailingDecimalPoint), True, "12"],
        ["12.0", constraints.dollars, False, "12"],
        ["12.00", constraints.dollars, True, "12"],
        ["12.000", constraints.dollars, False, "12"],
        ["12.000", merge(constraints.dollars, constraints.removeTrailingZerosFromNormalizedForm), False, "12"],
        ["-12", constraints.dollars, True, "-12"],
        ["-12.", constraints.dollars, True, "-12"],
        ["-12.", merge(constraints.dollars, constraints.dontRemoveTrailingDecimalPoint), True, "-12"],
        ["-12.0", constraints.dollars, False, "-12"],
        ["-12.00", constraints.dollars, True, "-12"],
        ["-12.000", constraints.dollars, False, "-12"],
        ["-12.000", merge(constraints.dollars, constraints.removeTrailingZerosFromNormalizedForm), False, "-12"],
        ["12.1", constraints.dollars, False, "12.1"],
        ["12.12", constraints.dollars, True, "12.12"],
        ["12.121", constraints.dollars, False, "12.121"],
        ["12", constraints.pounds, True, "12"],
        ["12.", constraints.pounds, True, "12"],
        ["12.", merge(constraints.pounds, constraints.dontRemoveTrailingDecimalPoint), True, "12"],
        ["12.0", constraints.pounds, False, "12"],
        ["12.00", constraints.pounds, True, "12"],
        ["12.000", constraints.pounds, False, "12"],
        ["12.000", merge(constraints.pounds, constraints.removeTrailingZerosFromNormalizedForm), False, "12"],
        ["12.1", constraints.pounds, False, "12.1"],
        ["12.12", constraints.pounds, True, "12.12"],
        ["12.121", constraints.pounds, False, "12.121"],
        ["12", constraints.egp, True, "12"],
        ["12.", constraints.egp, True, "12"],
        ["12.", merge(constraints.egp, constraints.dontRemoveTrailingDecimalPoint), True, "12"],
        ["12.0", constraints.egp, False, "12"],
        ["12.00", constraints.egp, True, "12"],
        ["12.000", constraints.egp, False, "12"],
        ["12.000", merge(constraints.egp, constraints.removeTrailingZerosFromNormalizedForm), False, "12"],
        ["12.1", constraints.egp, False, "12.1"],
        ["12.12", constraints.egp, True, "12.12"],
        ["12.121", constraints.egp, False, "12.121"],
        ["12", constraints.sar, True, "12"],
        ["12.", constraints.sar, True, "12"],
        ["12.", merge(constraints.sar, constraints.dontRemoveTrailingDecimalPoint), True, "12"],
        ["12.0", constraints.sar, False, "12"],
        ["12.00", constraints.sar, True, "12"],
        ["12.000", constraints.sar, False, "12"],
        ["12.000", merge(constraints.sar, constraints.removeTrailingZerosFromNormalizedForm), False, "12"],
        ["12.1", constraints.sar, False, "12.1"],
        ["12.12", constraints.sar, True, "12.12"],
        ["12.121", constraints.sar, False, "12.121"],
        ["012", constraints.dollars, False, "012"],
        ["012", merge(constraints.dollars, constraints.allowLeadingZeros), True, "012"],
        ["012", merge(constraints.dollars, constraints.allowLeadingZeros, constraints.removeLeadingZerosFromNormalizedForm), True, "12"],
        ["0012", merge(constraints.dollars, constraints.allowLeadingZeros, constraints.removeLeadingZerosFromNormalizedForm), True, "12"],
        ["00012", merge(constraints.dollars, constraints.allowLeadingZeros, constraints.removeLeadingZerosFromNormalizedForm), True, "12"],
        ["012.00", merge(constraints.dollars, constraints.allowLeadingZeros, constraints.removeLeadingZerosFromNormalizedForm), True, "12"],
        ["0012.00", merge(constraints.dollars, constraints.allowLeadingZeros, constraints.removeLeadingZerosFromNormalizedForm), True, "12"],
        ["00012.00", merge(constraints.dollars, constraints.allowLeadingZeros, constraints.removeLeadingZerosFromNormalizedForm), True, "12"],
    ])
    def test_validate(self, studentsResponse, constraints, isAccepted, normalisedStudentsResponse):

        validator = Validator()
        request = ValidationRequest()

        request.studentsResponse = studentsResponse
        request.expectedResponseType = "currencyValue"
        request.constraints = constraints

        response = validator.validate(request)

        self.assertEqual(response.isAccepted, isAccepted)
        self.assertEqual(response.normalisedStudentsResponse, normalisedStudentsResponse)


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output="example_dir"))
