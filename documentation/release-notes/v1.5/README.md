# Release Notes for v1.5

- There are fixes for issues #1 and #2.
    - This has involved creating a dedicated function within the parser that handles the conversion from just a regular number node to a currency value node, a process that should be affected by the context of the parser.
    - Unit tests that cover these issues have also been added.
- There are now 362 unit tests; all passing.