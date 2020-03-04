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

## Running the unit tests

You can run the unit tests in this library by calling

```bash

python -m unittest discover

```

## Testing the code through the browser interface

This library also contains a micro web-app for testing the response from the validation code when different validation and normalization parameters are applied.

Start the server for the web-app by calling

```bash
cd browser_based_testing
python start_app.py
```

## Documentation for developers

Technical documentation can be found in `/documentation`, and the release notes for each release can be found in `/documentation/release-notes`.

## Documentation for content writers

The documentation for content writers for how to use the different parameters can be found here: https://bm345.github.io/ResponseParsingPython/documentation/parameters/index.html