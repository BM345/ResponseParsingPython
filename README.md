# Response Parsing (Python)

At the moment, the validation code is in the folder `/rp`.

## Basic Usage

```python

from validation import *

validator = Validator()
request = ValidationRequest()

request.studentsResponse = "17"
request.expectedResponseType = "integer"
request.constraints = {
    "allowLeadingZeros": False,
    "mustHaveExplicitSign": False
}

response = validator.validate()

print(response.isAccepted) # True

```