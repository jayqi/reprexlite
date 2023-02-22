# Venues Formatting

reprexlite comes with support for formatting reprexes for the following venues.

{{ create_venue_help_table() }}

## Examples

{{ create_venue_help_examples() }}

## Custom Formatter

There are two steps to creating a custom formatter:

1. Subclass the `Formatter` abstract base class and implement a `format` method.
2. Register your custom formatter with the `@register_formatter(...)` decorator.

```python
from reprexlite.formatting import Formatter, register_formatter

@register_formatter(venue="myformat", label="My Custom Format")
class MyCustomerFormatter(Formatter):

    @classmethod
    def format(
        cls, reprex_str: str, advertise: bool | None = None, session_info: bool = False
    ) -> str:
        ...
```

This will make your formatter available under the venue key you provide to the registration decorator.

Currently, reprexlite does not have any extension or plugin system to load your code with your custom formatter. This means that you will only be able to easily access it with certain usage options where you can import or run your code, such as using reprexlite as a library or with the IPython cell magic.
