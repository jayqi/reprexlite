from collections import defaultdict
import dataclasses
from textwrap import dedent
from typing import Union

from griffe import Docstring, DocstringSectionAdmonition, DocstringSectionText
from markdownTable import markdownTable
from typenames import typenames

from reprexlite.config import ReprexConfig
from reprexlite.formatting import formatter_registry


def define_env(env):
    "Hook function"

    docstring = Docstring(ReprexConfig.__doc__, lineno=1)
    parsed = docstring.parse("google")
    descriptions = {param.name: param.description.replace("\n", " ") for param in parsed[1].value}

    @env.macro
    def create_config_help_table():
        out = dedent(
            """\
            <table>
                <thead>
                    <tr>
                        <th class="no-wrap"><b>Name</b></th>
                        <th class="no-wrap"><b>Type</b></th>
                        <th class="no-wrap"><b>Description</b></th>
                    </tr>
                    {}
                </thead>
            </table>
            """
        )
        out = out.format(
            "\n".join(
                f"""
                <tr>
                    <td class="no-wrap"><b><code>{field.name}</code></b></td>
                    <td class="no-wrap"><code>{typenames(field.type)}</code></td>
                    <td>{descriptions[field.name]}</td>
                </tr>
                """
                for field in dataclasses.fields(ReprexConfig)
            )
        )
        out = out.replace(
            '"Venues Formatting"', '<a href="../formatting/">"Venues Formatting"</a>'
        )
        return out
        # data = [
        #     {
        #         "Name": f"**`{field.name}`**",
        #         "Type": f"`{typenames(field.type)}`",
        #         "Description": field.metadata["help"],
        #     }
        #     for field in dataclasses.fields(ReprexConfig)
        # ]
        # table = markdownTable(data)
        # return table.setParams(row_sep="markdown", quote=False).getMarkdown()

    @env.macro
    def create_venue_help_table():
        data = [
            {
                "Venue Keyword": f"`{venue_key.value}`",
                "Description": formatter_entry.label,
                "Formatter Function": f"[`{formatter_entry.fn.__name__}`](#{formatter_entry.fn.__name__})",
            }
            for venue_key, formatter_entry in formatter_registry.items()
        ]
        table = markdownTable(data)
        return table.setParams(row_sep="markdown", quote=False).getMarkdown()

    @env.macro
    def create_venue_help_examples():
        data = defaultdict(list)
        for key, entry in formatter_registry.items():
            data[entry.fn].append(key)

        out = []
        for fn, keys in data.items():
            pass
            fn = entry.fn

            keys_list = ", ".join(f"`{key.value}`" for key in keys)
            out.append(f"### `{fn.__name__}`")

            # Parse docstring
            docstring = Docstring(fn.__doc__, lineno=1)
            parsed = docstring.parse("google")

            for section in parsed:
                if isinstance(section, DocstringSectionText):
                    out.append("")
                    out.append(section.value)
                elif isinstance(section, DocstringSectionAdmonition):
                    out.append("")
                    out.append(f"**Used for venues**: {keys_list}")
                    out.append("")
                    out.append(f"**{section.title}**")
                    out.append("")
                    out.append("````")
                    admonition = section.value
                    out.append(admonition.description)
                    out.append("````")
            out.append("")
            out.append(
                "<sup>"
                "↳ [API documentation]"
                f"(api-reference/formatting.md#reprexlite.rendering.{fn.__qualname__})"
                "</sup>"
            )
        return "\n".join(out)
