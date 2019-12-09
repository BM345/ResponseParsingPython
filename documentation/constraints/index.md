# Constraints

This document describes what constraints can be applied to which response types.

<br /><br />

## Table of Contents

- [Integers](#integers)
- [Non-negative Integers](#non-negative-integers)

<br /><br />

## Response Types

| Name | String | Description |
|---|---|---|
| Integer | `"integer"` | All whole numbers from -∞ to +∞ |
| Non-negative Integers | `"nonNegativeIntegers"` |  All whole numbers from 0 to +∞, **including** 0 |
| Decimal | `"decimal"` | All rational numbers from -∞ to +∞ |
| Currency Value | `"currencyValue"` | All rational numbers from -∞ to +∞, optionally with a currency symbol |

<br /><br />

## Integers

### `"allowLeadingZeros"`

If set to `false`, if the student's response has any leading zeros then it will **not** pass validation.

The default is `false`.

#### Example

```json
{
    "allowLeadingZeros": true
}
```

<br /><br />

### `"mustHaveExplicitSign"`

If set to `true`, in order to pass validation the student's response must have an explicit "+" or "-" sign at the start.

If set to `false`, in order to pass validation the student's response must either have a "-" sign or no sign at the start. (If they put a "+" sign, the response will not pass validation.)

The default is `false`.

#### Example

```json
{
  "mustHaveExplicitSign": false
}
```

<br /><br />

### `"mustHaveAtLeastNSF"`

In order to pass validation, the student's response must have a **minimum** of *n* significant figures.

The default is `not set`.

#### Example

```json
{
    "mustHaveAtLeastNSF": 3
}
```

<br /><br />

### `"mustHaveNoMoreThanNSF"`

In order to pass validation, the student's response must have a **maximum** of *n* significant figures.

The default is `not set`.

#### Example

```json
{
    "mustHaveNoMoreThanNSF": 5
}
```

<br /><br />

### `"mustHaveExactlyNSF"`

In order to pass validation, the student's response must have **exactly** *n* significant figures.

The default is `not set`.

#### Example

```json
{
    "mustHaveExactlyNSF": 3
}
```

<br /><br />

## Non-negative Integers

This response type has the same constraints as the `integer` type, but of course it doesn't allow negative-integer answers. (This means that the `"mustHaveExplicitSign"` constraint now only applies to the plus sign.)

<br /><br />

## Decimals

The `"mustHaveExplicitSign"`, `"mustHaveAtLeastNSF"`, `"mustHaveNoMoreThanNSF"` and `"mustHaveExactlyNSF"` constraints from the `integer` type can also be applied to the `decimal` type, as well as the following.

<br /><br />

### `"mustHaveAtLeastNDP"`

In order to pass validation, the student's response must have a **minimum** of *n* decimal places.

The default is `not set`.

#### Example

```json
{
    "mustHaveAtLeastNDP": 2
}
```

<br /><br />

### `"mustHaveNoMoreThanNDP"`

In order to pass validation, the student's response must have a **maximum** of *n* decimal places.

The default is `not set`.

#### Example

```json
{
    "mustHaveNoMoreThanNDP": 4
}
```

<br /><br />

### `"mustHaveExactlyNDP"`

In order to pass validation, the student's response must have **exactly** *n* decimal places.

The default is `not set`.

#### Example

```json
{
    "mustHaveExactlyNDP": 3
}
```

<br /><br />

