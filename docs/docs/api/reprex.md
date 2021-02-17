# Module reprexlite.reprex

None

None

??? example "View Source"
        from abc import ABC, abstractmethod

        from datetime import datetime

        from enum import Enum

        from pathlib import Path

        from typing import Callable, Dict, Optional

        

        from reprexlite.code import CodeBlock

        from reprexlite.session_info import SessionInfo

        from reprexlite.version import __version__

        

        

        class Advertisement:

            """Class for generating the advertisement note for reprexlite."""

        

            pkg = "reprexlite"

            url = "https://github.com/jayqi/reprexlite"

        

            def __init__(self):

                now = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

                self.created = f"Created at {now} by"

                self.ver = f"v{__version__}"

        

            def markdown(self) -> str:

                return f"<sup>{self.created} [{self.pkg}]({self.url}) {self.ver}</sup>"

        

            def html(self) -> str:

                return f'<p><sup>{self.created} <a href="{self.url}">{self.pkg}</a> {self.ver}</sup></p>'

        

            def code_comment(self) -> str:

                return f"# {self.created} {self.pkg} {self.ver} <{self.url}>"

        

            def text(self) -> str:

                return f"{self.created} {self.pkg} {self.ver} <{self.url}>"

        

        

        class Reprex(ABC):

            """Abstract base class for a reprex instance. Concrete subclasses should implement the

            formatting logic appropriate to a specific venue for sharing."""

        

            default_advertise: bool

        

            def __init__(

                self, code_block: CodeBlock, advertise: Optional[bool] = None, session_info: bool = False

            ):

                self.code_block: CodeBlock = code_block

                self.advertise: bool = self.default_advertise if advertise is None else advertise

                self.session_info: bool = session_info

        

            @abstractmethod

            def __str__(self) -> str:  # pragma: no cover

                pass

        

        

        class GitHubReprex(Reprex):

            """Concrete implementation for rendering reprexes in GitHub Flavored Markdown."""

        

            default_advertise: bool = True

        

            def __str__(self) -> str:

                out = []

                out.append("```python")

                out.append(str(self.code_block))

                out.append("```")

                if self.advertise:

                    out.append("\n" + Advertisement().markdown())

                if self.session_info:

                    out.append("\n<details><summary>Session Info</summary>")

                    out.append("```text")

                    out.append(str(SessionInfo()))

                    out.append("```")

                    out.append("</details>")

                return "\n".join(out)

        

        

        class HtmlReprex(Reprex):

            """Concrete implementation for rendering reprexes in HTML. If optional dependency Pygments is

            available, the rendered HTML will have syntax highlighting for the Python code."""

        

            default_advertise: bool = True

        

            def __str__(self) -> str:

                out = []

                try:

                    from pygments import highlight

                    from pygments.lexers import PythonLexer

                    from pygments.formatters import HtmlFormatter

        

                    formatter = HtmlFormatter()

                    out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")

                    out.append(highlight(str(self.code_block), PythonLexer(), formatter))

                except ImportError:

                    out.append(f"<pre><code>{self.code_block}</code></pre>")

        

                if self.advertise:

                    out.append(Advertisement().html())

                if self.session_info:

                    out.append("<details><summary>Session Info</summary>")

                    out.append(f"<pre><code>{SessionInfo()}</code></pre>")

                    out.append("</details>")

                return "\n".join(out)

        

        

        class PyScriptReprex(Reprex):

            """Concrete implementation for rendering reprexes as a Python script."""

        

            default_advertise: bool = False

        

            def __str__(self) -> str:

                out = [str(self.code_block)]

                if self.advertise:

                    out.append("\n" + Advertisement().code_comment())

                if self.session_info:

                    out.append("")

                    sess_lines = str(SessionInfo()).split("\n")

                    out.extend("# " + line for line in sess_lines)

                return "\n".join(out)

        

        

        class RtfReprex(Reprex):

            """Concrete implementation for rendering reprexes in Rich Text Format."""

        

            default_advertise: bool = False

        

            def __str__(self) -> str:

                try:

                    from pygments import highlight

                    from pygments.lexers import PythonLexer

                    from pygments.formatters import RtfFormatter

                except ImportError:

                    raise ImportError("Pygments is required for RTF output.")

        

                out = str(self.code_block)

                if self.advertise:

                    out += "\n\n" + Advertisement().text()

                if self.session_info:

                    out += "\n\n" + str(SessionInfo())

                return highlight(out, PythonLexer(), RtfFormatter())

        

        

        class SlackReprex(Reprex):

            """Concrete implementation for rendering reprexes as Slack markup."""

        

            default_advertise: bool = False

        

            def __str__(self):

                out = []

                out.append("```")

                out.append(str(self.code_block))

                out.append("```")

                if self.advertise:

                    out.append("\n" + Advertisement().text())

                if self.session_info:

                    out.append("\n```")

                    out.append(str(SessionInfo()))

                    out.append("```")

                return "\n".join(out)

        

        

        venues_dispatcher: Dict[str, Callable] = {

            "gh": GitHubReprex,

            "so": GitHubReprex,

            "ds": GitHubReprex,

            "html": HtmlReprex,

            "py": PyScriptReprex,

            "rtf": RtfReprex,

            "slack": SlackReprex,

        }

        """Mapping from venue keywords to their Reprex implementation."""

        

        

        Venue = Enum("Venue", names={v.upper(): v for v in venues_dispatcher.keys()}, type=str)  # type: ignore

        Venue.__doc__ = """Enum for valid venue options."""

        

        

        def reprex(

            input: str,

            outfile: Optional[Path] = None,

            venue="gh",

            advertise: Optional[bool] = None,

            session_info: bool = False,

            style: bool = False,

            comment: str = "#>",

            print_=True,

            terminal=False,

        ) -> Reprex:

            """Render reproducible examples of Python code for sharing. This function will evaluate your

            code and returns an instance of a [`Reprex`](reprexlite.reprex.Reprex) subclass. Calling

            `str(...)` on the `Reprex` object will return your code with the evaluated results embedded

            as comments, plus additional markup appropriate to the sharing venue set by the `venue` keyword

            argument.

        

            For example, for the `gh` venue for GitHub Flavored Markdown, you'll get a reprex whose string

            representation looks like:

        

            ````

            ```python

            x = 2

            x + 2

            #> 4

            ```

        

            <sup>Created at 2021-02-15 16:58:47 PST by [reprexlite](https://github.com/jayqi/reprexlite) v0.1.0</sup>

            ````

        

            The supported `venue` formats are:

        

            - `gh` : GitHub Flavored Markdown

            - `so` : StackOverflow, alias for gh

            - `ds` : Discourse, alias for gh

            - `html` : HTML

            - `py` : Python script

            - `rtf` : Rich Text Format

            - `slack` : Slack

        

            Args:

                input (str): Block of Python code

                outfile (Optional[Path]): Optional file path to write reprex to. Defaults to None.

                venue (str): Determines the output format by the venue you want to share the code. Defaults

                    to "gh" for GitHub Flavored Markdown.

                advertise (Optional[bool]): Whether to include a note that links back to the reprexlite

                    package. Default `None` will use the default set by choice of `venue`.

                session_info (bool): Whether to include additional details about your Python version,

                    operating system, and installed packages. Defaults to False.

                style (bool): Whether to autoformat your code with black. Defaults to False.

                comment (str): Line prefix to use for displaying evaluated results. Defaults to "#>".

                print_ (bool): Whether to print your reprex to console. Defaults to True.

                terminal (bool): Whether to use syntax highlighting for 256-color terminal display.

                    Requires optional dependency Pygments. Defaults to False.

        

            Returns:

                Instance of a `Reprex` concrete subclass for `venue`.

            """

            if outfile or venue in ["html", "rtf"]:

                # Don't screw output file or lexing for HTML and RTF with terminal syntax highlighting

                terminal = False

            code_block = CodeBlock(input, style=style, comment=comment, terminal=terminal)

        

            reprex = venues_dispatcher[venue](

                code_block=code_block, advertise=advertise, session_info=session_info

            )

            if outfile is not None:

                with outfile.open("w") as fp:

                    fp.write(str(reprex) + "\n")

            if print_:

                print(reprex)

            return reprex

## Variables

```python3
venues_dispatcher
```

## Functions

    
### reprex

```python3
def reprex(
    input: str,
    outfile: Union[pathlib.Path, NoneType] = None,
    venue='gh',
    advertise: Union[bool, NoneType] = None,
    session_info: bool = False,
    style: bool = False,
    comment: str = '#>',
    print_=True,
    terminal=False
) -> reprexlite.reprex.Reprex
```

    
Render reproducible examples of Python code for sharing. This function will evaluate your

code and returns an instance of a [`Reprex`](reprexlite.reprex.Reprex) subclass. Calling
`str(...)` on the `Reprex` object will return your code with the evaluated results embedded
as comments, plus additional markup appropriate to the sharing venue set by the `venue` keyword
argument.

For example, for the `gh` venue for GitHub Flavored Markdown, you'll get a reprex whose string
representation looks like:

````
```python
x = 2
x + 2
#> 4
```

<sup>Created at 2021-02-15 16:58:47 PST by [reprexlite](https://github.com/jayqi/reprexlite) v0.1.0</sup>
````

The supported `venue` formats are:

- `gh` : GitHub Flavored Markdown
- `so` : StackOverflow, alias for gh
- `ds` : Discourse, alias for gh
- `html` : HTML
- `py` : Python script
- `rtf` : Rich Text Format
- `slack` : Slack

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| input | str | Block of Python code | None |
| outfile | Optional[Path] | Optional file path to write reprex to. Defaults to None. | None |
| venue | str | Determines the output format by the venue you want to share the code. Defaults
to "gh" for GitHub Flavored Markdown. | None |
| advertise | Optional[bool] | Whether to include a note that links back to the reprexlite
package. Default `None` will use the default set by choice of `venue`. | None |
| session_info | bool | Whether to include additional details about your Python version,
operating system, and installed packages. Defaults to False. | None |
| style | bool | Whether to autoformat your code with black. Defaults to False. | False |
| comment | str | Line prefix to use for displaying evaluated results. Defaults to "#>". | "#>" |
| print_ | bool | Whether to print your reprex to console. Defaults to True. | True |
| terminal | bool | Whether to use syntax highlighting for 256-color terminal display.
Requires optional dependency Pygments. Defaults to False. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Instance of a `Reprex` concrete subclass for `venue`. |

??? example "View Source"
        def reprex(

            input: str,

            outfile: Optional[Path] = None,

            venue="gh",

            advertise: Optional[bool] = None,

            session_info: bool = False,

            style: bool = False,

            comment: str = "#>",

            print_=True,

            terminal=False,

        ) -> Reprex:

            """Render reproducible examples of Python code for sharing. This function will evaluate your

            code and returns an instance of a [`Reprex`](reprexlite.reprex.Reprex) subclass. Calling

            `str(...)` on the `Reprex` object will return your code with the evaluated results embedded

            as comments, plus additional markup appropriate to the sharing venue set by the `venue` keyword

            argument.

        

            For example, for the `gh` venue for GitHub Flavored Markdown, you'll get a reprex whose string

            representation looks like:

        

            ````

            ```python

            x = 2

            x + 2

            #> 4

            ```

        

            <sup>Created at 2021-02-15 16:58:47 PST by [reprexlite](https://github.com/jayqi/reprexlite) v0.1.0</sup>

            ````

        

            The supported `venue` formats are:

        

            - `gh` : GitHub Flavored Markdown

            - `so` : StackOverflow, alias for gh

            - `ds` : Discourse, alias for gh

            - `html` : HTML

            - `py` : Python script

            - `rtf` : Rich Text Format

            - `slack` : Slack

        

            Args:

                input (str): Block of Python code

                outfile (Optional[Path]): Optional file path to write reprex to. Defaults to None.

                venue (str): Determines the output format by the venue you want to share the code. Defaults

                    to "gh" for GitHub Flavored Markdown.

                advertise (Optional[bool]): Whether to include a note that links back to the reprexlite

                    package. Default `None` will use the default set by choice of `venue`.

                session_info (bool): Whether to include additional details about your Python version,

                    operating system, and installed packages. Defaults to False.

                style (bool): Whether to autoformat your code with black. Defaults to False.

                comment (str): Line prefix to use for displaying evaluated results. Defaults to "#>".

                print_ (bool): Whether to print your reprex to console. Defaults to True.

                terminal (bool): Whether to use syntax highlighting for 256-color terminal display.

                    Requires optional dependency Pygments. Defaults to False.

        

            Returns:

                Instance of a `Reprex` concrete subclass for `venue`.

            """

            if outfile or venue in ["html", "rtf"]:

                # Don't screw output file or lexing for HTML and RTF with terminal syntax highlighting

                terminal = False

            code_block = CodeBlock(input, style=style, comment=comment, terminal=terminal)

        

            reprex = venues_dispatcher[venue](

                code_block=code_block, advertise=advertise, session_info=session_info

            )

            if outfile is not None:

                with outfile.open("w") as fp:

                    fp.write(str(reprex) + "\n")

            if print_:

                print(reprex)

            return reprex

## Classes

### Advertisement

```python3
class Advertisement(
    
)
```

??? example "View Source"
        class Advertisement:

            """Class for generating the advertisement note for reprexlite."""

        

            pkg = "reprexlite"

            url = "https://github.com/jayqi/reprexlite"

        

            def __init__(self):

                now = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

                self.created = f"Created at {now} by"

                self.ver = f"v{__version__}"

        

            def markdown(self) -> str:

                return f"<sup>{self.created} [{self.pkg}]({self.url}) {self.ver}</sup>"

        

            def html(self) -> str:

                return f'<p><sup>{self.created} <a href="{self.url}">{self.pkg}</a> {self.ver}</sup></p>'

        

            def code_comment(self) -> str:

                return f"# {self.created} {self.pkg} {self.ver} <{self.url}>"

        

            def text(self) -> str:

                return f"{self.created} {self.pkg} {self.ver} <{self.url}>"

------

#### Class variables

```python3
pkg
```

```python3
url
```

#### Methods

    
#### code_comment

```python3
def code_comment(
    self
) -> str
```

    

??? example "View Source"
            def code_comment(self) -> str:

                return f"# {self.created} {self.pkg} {self.ver} <{self.url}>"

    
#### html

```python3
def html(
    self
) -> str
```

    

??? example "View Source"
            def html(self) -> str:

                return f'<p><sup>{self.created} <a href="{self.url}">{self.pkg}</a> {self.ver}</sup></p>'

    
#### markdown

```python3
def markdown(
    self
) -> str
```

    

??? example "View Source"
            def markdown(self) -> str:

                return f"<sup>{self.created} [{self.pkg}]({self.url}) {self.ver}</sup>"

    
#### text

```python3
def text(
    self
) -> str
```

    

??? example "View Source"
            def text(self) -> str:

                return f"{self.created} {self.pkg} {self.ver} <{self.url}>"

### GitHubReprex

```python3
class GitHubReprex(
    code_block: reprexlite.code.CodeBlock,
    advertise: Union[bool, NoneType] = None,
    session_info: bool = False
)
```

??? example "View Source"
        class GitHubReprex(Reprex):

            """Concrete implementation for rendering reprexes in GitHub Flavored Markdown."""

        

            default_advertise: bool = True

        

            def __str__(self) -> str:

                out = []

                out.append("```python")

                out.append(str(self.code_block))

                out.append("```")

                if self.advertise:

                    out.append("\n" + Advertisement().markdown())

                if self.session_info:

                    out.append("\n<details><summary>Session Info</summary>")

                    out.append("```text")

                    out.append(str(SessionInfo()))

                    out.append("```")

                    out.append("</details>")

                return "\n".join(out)

------

#### Ancestors (in MRO)

* reprexlite.reprex.Reprex
* abc.ABC

#### Class variables

```python3
default_advertise
```

### HtmlReprex

```python3
class HtmlReprex(
    code_block: reprexlite.code.CodeBlock,
    advertise: Union[bool, NoneType] = None,
    session_info: bool = False
)
```

??? example "View Source"
        class HtmlReprex(Reprex):

            """Concrete implementation for rendering reprexes in HTML. If optional dependency Pygments is

            available, the rendered HTML will have syntax highlighting for the Python code."""

        

            default_advertise: bool = True

        

            def __str__(self) -> str:

                out = []

                try:

                    from pygments import highlight

                    from pygments.lexers import PythonLexer

                    from pygments.formatters import HtmlFormatter

        

                    formatter = HtmlFormatter()

                    out.append(f"<style>{formatter.get_style_defs('.highlight')}</style>")

                    out.append(highlight(str(self.code_block), PythonLexer(), formatter))

                except ImportError:

                    out.append(f"<pre><code>{self.code_block}</code></pre>")

        

                if self.advertise:

                    out.append(Advertisement().html())

                if self.session_info:

                    out.append("<details><summary>Session Info</summary>")

                    out.append(f"<pre><code>{SessionInfo()}</code></pre>")

                    out.append("</details>")

                return "\n".join(out)

------

#### Ancestors (in MRO)

* reprexlite.reprex.Reprex
* abc.ABC

#### Class variables

```python3
default_advertise
```

### PyScriptReprex

```python3
class PyScriptReprex(
    code_block: reprexlite.code.CodeBlock,
    advertise: Union[bool, NoneType] = None,
    session_info: bool = False
)
```

??? example "View Source"
        class PyScriptReprex(Reprex):

            """Concrete implementation for rendering reprexes as a Python script."""

        

            default_advertise: bool = False

        

            def __str__(self) -> str:

                out = [str(self.code_block)]

                if self.advertise:

                    out.append("\n" + Advertisement().code_comment())

                if self.session_info:

                    out.append("")

                    sess_lines = str(SessionInfo()).split("\n")

                    out.extend("# " + line for line in sess_lines)

                return "\n".join(out)

------

#### Ancestors (in MRO)

* reprexlite.reprex.Reprex
* abc.ABC

#### Class variables

```python3
default_advertise
```

### Reprex

```python3
class Reprex(
    code_block: reprexlite.code.CodeBlock,
    advertise: Union[bool, NoneType] = None,
    session_info: bool = False
)
```

??? example "View Source"
        class Reprex(ABC):

            """Abstract base class for a reprex instance. Concrete subclasses should implement the

            formatting logic appropriate to a specific venue for sharing."""

        

            default_advertise: bool

        

            def __init__(

                self, code_block: CodeBlock, advertise: Optional[bool] = None, session_info: bool = False

            ):

                self.code_block: CodeBlock = code_block

                self.advertise: bool = self.default_advertise if advertise is None else advertise

                self.session_info: bool = session_info

        

            @abstractmethod

            def __str__(self) -> str:  # pragma: no cover

                pass

------

#### Ancestors (in MRO)

* abc.ABC

#### Descendants

* reprexlite.reprex.GitHubReprex
* reprexlite.reprex.HtmlReprex
* reprexlite.reprex.PyScriptReprex
* reprexlite.reprex.RtfReprex
* reprexlite.reprex.SlackReprex

### RtfReprex

```python3
class RtfReprex(
    code_block: reprexlite.code.CodeBlock,
    advertise: Union[bool, NoneType] = None,
    session_info: bool = False
)
```

??? example "View Source"
        class RtfReprex(Reprex):

            """Concrete implementation for rendering reprexes in Rich Text Format."""

        

            default_advertise: bool = False

        

            def __str__(self) -> str:

                try:

                    from pygments import highlight

                    from pygments.lexers import PythonLexer

                    from pygments.formatters import RtfFormatter

                except ImportError:

                    raise ImportError("Pygments is required for RTF output.")

        

                out = str(self.code_block)

                if self.advertise:

                    out += "\n\n" + Advertisement().text()

                if self.session_info:

                    out += "\n\n" + str(SessionInfo())

                return highlight(out, PythonLexer(), RtfFormatter())

------

#### Ancestors (in MRO)

* reprexlite.reprex.Reprex
* abc.ABC

#### Class variables

```python3
default_advertise
```

### SlackReprex

```python3
class SlackReprex(
    code_block: reprexlite.code.CodeBlock,
    advertise: Union[bool, NoneType] = None,
    session_info: bool = False
)
```

??? example "View Source"
        class SlackReprex(Reprex):

            """Concrete implementation for rendering reprexes as Slack markup."""

        

            default_advertise: bool = False

        

            def __str__(self):

                out = []

                out.append("```")

                out.append(str(self.code_block))

                out.append("```")

                if self.advertise:

                    out.append("\n" + Advertisement().text())

                if self.session_info:

                    out.append("\n```")

                    out.append(str(SessionInfo()))

                    out.append("```")

                return "\n".join(out)

------

#### Ancestors (in MRO)

* reprexlite.reprex.Reprex
* abc.ABC

#### Class variables

```python3
default_advertise
```

### Venue

```python3
class Venue(
    /,
    *args,
    **kwargs
)
```

#### Ancestors (in MRO)

* builtins.str
* enum.Enum

#### Class variables

```python3
DS
```

```python3
GH
```

```python3
HTML
```

```python3
PY
```

```python3
RTF
```

```python3
SLACK
```

```python3
SO
```

```python3
name
```

```python3
value
```