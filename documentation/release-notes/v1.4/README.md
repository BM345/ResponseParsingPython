# Release Notes for v1.4

- The messages file has been translated into four additional languages: French, Spanish, Portuguese, and Arabic. Messages can now be delivered in a total of five languages.
- The "currency" parameter now works for the Egyptian Pound (EGP) and the Saudi Riyal (SAR). The same limitations are applied to these currencies as to USD and GBP - any answer that isn't written to zero or two decimal places will not pass validation.
  - Unit tests have been added for these new currencies.
- Three new parameters have been added, which are:
  - "allowTrailingZeros"
  - "removeTrailingZerosFromNormalizedForm"
  - "removeTrailingDecimalPointFromNormalizedForm"
  - The way that these parameters work has been added to the documentation.
  - Unit tests have been added for these new parameters.
- A 'web' version of the parameters documentation has been added for content developers and writers.
- A fix for currency values of the form '___.00' has been added. Any currency value of this form will always be normalized to '___' - i.e., '12.00' will always become '12'. This is an in-built feature - for currency values, the parameters "allowTrailingZeros", "removeTrailingZerosFromNormalizedForm", and "removeTrailingDecimalPointFromNormalizedForm" are always ignored.
- There are currently 347 unit tests; all passing.