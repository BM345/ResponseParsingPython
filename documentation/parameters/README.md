# Validation and Normalization Parameters

This document describes which validation and normalization parameters can be set for which response types.

<br /><br />

## Response Types

| Name | String | Description |
|---|---|---|
| Integer | `"integer"` | All whole numbers from -∞ to +∞ |
| Non-negative Integer | `"nonNegativeInteger"` |  All whole numbers from 0 to +∞, **including** 0 |
| Decimal | `"decimal"` | All rational numbers from -∞ to +∞ |
| Currency Value | `"currencyValue"` | All rational numbers from -∞ to +∞ |

<br /><br />

## Parameters that can be set for integers

### `"allowLeadingZeros"`

#### Allowed Values

| Value | | Description | Examples that WOULD pass | Examples that WOULD NOT pass |
|---|---|---|---|---|
| `false` | *default* | In order to pass validation, the student's response **must not** have any leading zeros. | `12` | `0012` |
| `true` | | The student's response will pass validation regardless of whether or not it has any leading zeros. | `12`, `0012` |

#### Example (JSON)

```json
{
    "allowLeadingZeros": true
}
```

<br /><br />

### `"removeLeadingZerosFromNormalizedForm"`

#### Allowed Values

| Value | | Description |
|---|---|---|
| `false` | *default* | When the student's response is normalized, leading zeros **will not** be removed. |
| `true` | | When the student's response is normalized, leading zeros **will** be removed. |

#### Example (JSON)

```json
{
    "removeLeadingZerosFromNormalizedForm": true
}
```

<br /><br />

### `"sign"`

#### Allowed Values

| Value | | Description | Examples that WOULD pass | Examples that WOULD NOT pass |
|---|---|---|---|---|
|`"mustBeExplicit"`| | In order to pass validation, the student's response must have an explicit "+" or "-" sign at the start. | `+12`, `-12` | `12` | 
|`"mustBeImplicit"`| | In order to pass validation, the student's response must either have a "-" sign at the start, or no sign (an implicit plus). | `12`, `-12` | `+12` |
|`"canBeExplicitOrImplicit"`| *default* | The student's response will pass validation regardless of whether it has a "+" sign, a "-" sign, or no sign at the start. | `+12`, `12`, `-12` | |

#### Example (JSON)

```json
{
  "sign": "mustBeExplicit"
}
```

<br /><br />

### `"normalizeSign"`

#### Allowed Values

| Value | | Description |
|---|---|---|
|`"makeExplicit"`| | When the student's response is normalized, if it is a positive number, it will be given an explicit plus sign. |
|`"makeImplicit"`| | When the student's response is normalized, if it is a positive number, and it has an explicit plus sign, the plus sign will be removed. |
|`"notSet"`| *default* | No change will be made to plus signs when the student's response is normalized. |

#### Example (JSON)

```json
{
  "normalizeSign": "makeImplicit"
}
```

<br /><br />

<div style="background-color: hsl(30, 50%, 80%); color: hsl(30, 70%, 50%); padding: 1em 2em; border-radius: 2px; border: 1px solid hsl(30, 50%, 60%);">
<h3>Tip</h3>
<p>For most questions, you will want to set "sign" to "canBeExplicitOrImplicit" and "normalizeSign" to "makeImplicit". This will allow students to either type a plus sign or not for positive numbers, but their response can still be checked against the key (assuming the key does not have a plus sign).</p>
<p>In other words, if the key is '12', a student can type '12' or '+12', and their response will both pass validation and then be normalized to '12'.</p>
</div>

<br /><br />

### `"mustHaveAtLeastNSF"`

#### Allowed Values

| Value | Description |
|---|---|
| any integer *n* greater than 0 | In order to pass validation, the student's response must have a **minimum** of *n* significant figures. |

The default is `not set`.

#### Example (JSON)

```json
{
    "mustHaveAtLeastNSF": 3
}
```

<br /><br />

### `"mustHaveNoMoreThanNSF"`

#### Allowed Values

| Value | Description |
|---|---|
| any integer *n* greater than 0 | In order to pass validation, the student's response must have a **maximum** of *n* significant figures. |

The default is `not set`.

#### Example (JSON)

```json
{
    "mustHaveNoMoreThanNSF": 5
}
```

<br /><br />

### `"mustHaveExactlyNSF"`

#### Allowed Values

| Value | Description |
|---|---|
| any integer *n* greater than 0 | In order to pass validation, the student's response must have **exactly** *n* significant figures. |

The default is `not set`.

#### Example (JSON)

```json
{
    "mustHaveExactlyNSF": 3
}
```

<br /><br />

## Parameters that can be set for non-negative integers

This response type can have the same parameters as the `integer` type, but of course it doesn't allow negative-integer answers.

<br /><br />

## Parameters that can be set for decimals

The `"allowLeadingZeros"`, `"removeLeadingZerosFromNormalizedForm"`, `"sign"`, `"normalizeSign"`, `"mustHaveAtLeastNSF"`, `"mustHaveNoMoreThanNSF"` and `"mustHaveExactlyNSF"` parameters from the `integer` type can also be set for the `decimal` type, as well as the following.

<br /><br />

### `"allowTrailingZeros"`

A trailing zero is any zero that appears **at the end of a number** and **after the decimal point**.

![](trailing-zeros.png)
![](trailing-zeros-2.png)

#### Allowed Values

| Value | | Description | Examples that WOULD pass | Examples that WOULD NOT pass |
|---|---|---|---|---|
| `false` | | In order to pass validation, the student's response **must not** have any trailing zeros. | `12.3` | `12.30`, `12.300` |
| `true` | *default* | The student's response will pass validation regardless of whether or not it has any trailing zeros. | `12.3`, `12.30`, `12.300` |

#### Example (JSON)

```json
{
    "allowTrailingZeros": false
}
```

<br /><br />

### `"removeTrailingZerosFromNormalizedForm"`

#### Allowed Values

| Value | | Description |
|---|---|---|
| `false` | *default* | When the student's response is normalized, trailing zeros **will not** be removed. |
| `true` | | When the student's response is normalized, trailing zeros **will** be removed. |

#### Example (JSON)

```json
{
    "removeTrailingZerosFromNormalizedForm": true
}
```

<br /><br />

### `"removeTrailingDecimalPointFromNormalizedForm"`

#### Allowed Values

| Value | | Description |
|---|---|---|
| `false` | | When the student's response is normalized, if it has a trailing decimal point it **will not** be removed. |
| `true` | *default* | When the student's response is normalized, if it has a trailing decimal point it **will** be removed. |

#### Example (JSON)

```json
{
    "removeTrailingDecimalPointFromNormalizedForm": false
}
```

<br /><br />

### `"addSingleLeadingZeroToNormalizedForm"`

A student may enter '.12' as an answer to a decimal question. This is a valid decimal, and so should be allowed, but the answer has probably been stored in the XML as '0.12', so a '0' must be added to the normalized form.

#### Allowed Values

| Value | | Description |
|---|---|---|
| `false` | | When the student's response is normalized, if it has no digits before the decimal point, then a '0' **will not** be added. |
| `true` | *default* | When the student's response is normalized, if it has no digits before the decimal point, then a '0' **will** be added. |

#### Example (JSON)

```json
{
    "addSingleLeadingZeroToNormalizedForm": false
}
```

<br /><br />

### `"mustHaveAtLeastNDP"`

#### Allowed Values

| Value | Description |
|---|---|
| any integer *n* greater than 0 | In order to pass validation, the student's response must have a **minimum** of *n* decimal places. |

The default is `not set`.

#### Example (JSON)

```json
{
    "mustHaveAtLeastNDP": 2
}
```

<br /><br />

### `"mustHaveNoMoreThanNDP"`

#### Allowed Values

| Value | Description |
|---|---|
| any integer *n* greater than 0 | In order to pass validation, the student's response must have a **maximum** of *n* decimal places. |

The default is `not set`.

#### Example (JSON)

```json
{
    "mustHaveNoMoreThanNDP": 4
}
```

<br /><br />

### `"mustHaveExactlyNDP"`

#### Allowed Values

| Value | Description |
|---|---|
| any integer *n* greater than 0 | In order to pass validation, the student's response must have **exactly** *n* decimal places. |

The default is `not set`.

#### Example (JSON)

```json
{
    "mustHaveExactlyNDP": 3
}
```

<br /><br />

## Parameters that can be set for currency values

The `"allowLeadingZeros"`, `"removeLeadingZerosFromNormalizedForm"`, `"sign"`, and `"normalizeSign"` parameters from the `integer` type can also be set for the `currencyValue` type.

The `"allowTrailingZeros"` and `"removeTrailingZerosFromNormalizedForm"` parameters **cannot** be set for the `currencyValue` type. This is because for currency values they should always have values of `true` and `false` respectively (and these are their default values). '$12.50' is always a valid way of writing a currency value in dollars, and how we would expect the value to be stored in the question XML.

### `"currency"`

#### Allowed Values

| Value | Description | Examples that WOULD pass | Examples that WOULD NOT pass |
|---|---|---|---|
| `"USD"` | US Dollars | `12`, `12.50` | `12.5`, `12.500` |
| `"GBP"` | UK Pounds | `12`, `12.50` | `12.5`, `12.500` |
| `"EGP"` | Egyptian Pounds | `12`, `12.50` | `12.5`, `12.500` | |

If `"currency"` is set to any of these values, the student's response will be rejected if it is **not** written to 2 decimal places or 0 decimal places.

#### Example (JSON)

```json
{
    "currency": "USD"
}
```

<br /><br />




