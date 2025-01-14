import dataclasses
from textwrap import dedent
from typing import Union

from markdownTable import markdownTable
from typenames import typenames

from reprexlite.config import ReprexConfig
from reprexlite.rendering import renderer_registry


def define_env(env):
    "Hook function"

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
                    <td>{field.metadata['help']}</td>
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
                "Venue Keyword": venue_key,
                "Description": formatter.meta.venues[venue_key],
                "Formatter": f"[`{formatter.__name__}`](#{formatter.__name__.lower()})",
            }
            for venue_key, formatter in renderer_registry.items()
        ]
        table = markdownTable(data)
        return table.setParams(row_sep="markdown", quote=False).getMarkdown()

    @env.macro
    def create_venue_help_examples():
        out = []
        for formatter in dict.fromkeys(renderer_registry.values()):
            out.append(f"### `{formatter.__name__}`")
            out.append("")
            out.append(formatter.__doc__)
            out.append("")
            out.append("````")
            out.append(formatter.meta.example or "Example not shown.")
            out.append("````")
            out.append("")
            out.append(
                "<sup>"
                "↳ [API documentation]"
                f"(api-reference/formatting.md#reprexlite.formatting.{formatter.__qualname__})"
                "</sup>"
            )
        return "\n".join(out)
