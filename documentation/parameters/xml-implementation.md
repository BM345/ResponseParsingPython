# Proposed XML implementation of the response validation parameters

This document contains a proposal for how to implement the response validation parameters in the question XML.

```xml
<mcq>
    <key_values>
        <key_value type="integer">12</key_value>
    <key_values>
    <response_validation_parameters>
        <allow_leading_zeros>true</allow_leading_zeros>
        <sign>mustBeExplicit</sign>
        <must_have_exactly_nsf>3</must_have_exactly_nsf>
    </response_validation_parameters>
    <response_normalization_parameters>
        <remove_leading_zeros>true</remove_leading_zeros>
    </response_normalization_parameters>
</mcq>
```