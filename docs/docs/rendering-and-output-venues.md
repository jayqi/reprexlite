# Rendering and Output Venues

A rendered reprex will be code plus the computed outputs plus additional formatting markup appropriate for some particular output venue. For example, the `gh` venue (GitHub) will be in GitHub-flavored markdown and may look like this:

````
```python
2+2
#> 4
```
````

The venue can be set using the `--venue / -v` command-line flag or the `venue` configuration file option. The following section documents the available output venue options.

## Venue options

{{ create_venue_help_table() }}

## Formatter functions

{{ create_venue_help_examples() }}

## Under the hood and Python API

There are two steps to rendering a reprex:

1. The `Reprex.render()` method renders a reprex instance as just the code and outputs.
2. A formatter function from `reprexlite.formatting` (see [above](#formatter-functions)) formats the rendered reprex code and outputs for the specified venue.

The whole process is encapsulated in the `Reprex.render_and_format()` method.
