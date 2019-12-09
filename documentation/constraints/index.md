# Constraints

This document describes what constraints can be applied to which response types.

## `"integer"`

### `"mustHaveAtLeastNSF"`

In order to pass validation, the student's response must have a **minimum** of *n* significant figures.

#### Example

```json
{
    "mustHaveAtLeastNSF": 3
}
```

### `"mustHaveNoMoreThanNSF"`

In order to pass validation, the student's response must have a **maximum** of *n* significant figures.

#### Example

```json
{
    "mustHaveNoMoreThanNSF": 5
}
```

### `"mustHaveExactlyNSF"`

In order to pass validation, the student's response must have **exactly** *n* significant figures.

If set, this constraint overrides both `"mustHaveAtLeastNSF"` and `"mustHaveNoMoreThanNSF"`.

#### Example

```json
{
    "mustHaveExactlyNSF": 3
}
```

