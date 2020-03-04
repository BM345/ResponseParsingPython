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