# Proposed XML implementation of the response validation parameters

This document contains a proposal for how to implement the response validation parameters in the question XML.

## Overview

- Add two XML tags that are siblings of the `<key_values>` tag
  - `<response_validation_parameters>`
  - `<response_normalization_parameters>`
- The reason for making them sibling tags of the `<key_values>` tag, rather than attributes of it, is because when we start adding support for complex numbers and vectors, the structure of the parameters that can be applied to validation and normalization will be quite complex.
- The `<response_validation_parameters>` tag contains the parameters for the validation process
- The `<response_normalization_parameters>` tag contains the parameters for the normalization process.

## Example

Below is an example of how the XML might look for an integer response question.

```xml
<mcq>
    <key_values>
        <key_value type="integer">+12</key_value>
    <key_values>
    <response_validation_parameters>
        <allow_leading_zeros>true</allow_leading_zeros>
        <sign>mustBeExplicit</sign>
        <must_have_exactly_nsf>2</must_have_exactly_nsf>
    </response_validation_parameters>
    <response_normalization_parameters>
        <remove_leading_zeros>true</remove_leading_zeros>
    </response_normalization_parameters>
</mcq>
```

## `<response_validation_parameters>`

The following tags can be children of the `<response_validation_parameters>` tag.

| Tag Name | Allowed Values |
|---|---|
|`<allow_leading_zeros>`| `true` \| `false` |
|`<sign>`| `"mustBeExplicit"` \| `"mustBeImplicit"` \| `"canBeExplicitOrImplicit"` |
|`<must_have_at_least_nsf>`| any integer |
|`<must_have_no_more_than_nsf>`| any integer |
|`<must_have_exactly_nsf>`| any integer |
|`<must_have_at_least_ndp>`| any integer |
|`<must_have_no_more_than_ndp>`| any integer |
|`<must_have_exactly_ndp>`| any integer |

## `<response_normalization_parameters>`

The following tags can be children of the `<response_normalization_parameters>` tag.

| Tag Name | Allowed Values |
|---|---|
|`<remove_leading_zeros>`| `true` \| `false` |
|`<sign>`| `"makeExplicit"` \| `"makeImplicit"` \| `"notSet"` |