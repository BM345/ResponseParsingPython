# Constraints

This document describes what constraints can be applied to which response types.

## `"integer"`

### `"mustHaveAtLeastNSF"`

In order to pass validation, the student's response must have a minimum of *n* significant figures.

#### Example

```json
{
    "mustHaveAtLeastNSF": 3
}
```

