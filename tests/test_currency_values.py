import unittest
from parameterized import parameterized
from pyunitreport import HTMLTestRunner

from rp.validation import *
import constraints
from general import *


class TestCurrencyValueValidation(unittest.TestCase):

    @parameterized.expand([
        ["12", constraints.dollars, True, "12"],
        ["12.0", constraints.dollars, False, "12.0"],
        ["12.00", constraints.dollars, True, "12.00"],
        ["12.000", constraints.dollars, False, "12.000"],
        ["12.1", constraints.dollars, False, "12.1"],
        ["12.12", constraints.dollars, True, "12.12"],
        ["12.121", constraints.dollars, False, "12.121"],
        ["12", constraints.pounds, True, "12"],
        ["12.0", constraints.pounds, False, "12.0"],
        ["12.00", constraints.pounds, True, "12.00"],
        ["12.000", constraints.pounds, False, "12.000"],
        ["12.1", constraints.pounds, False, "12.1"],
        ["12.12", constraints.pounds, True, "12.12"],
        ["12.121", constraints.pounds, False, "12.121"],
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
