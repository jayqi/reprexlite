Module reprexlite.reprex
========================

Variables
---------

    
`venues_dispatcher: Dict[str, Callable]`
:   Mapping from venue keywords to their Reprex implementation.

Functions
---------

    
`reprex(input: str, outfile: Union[pathlib.Path, NoneType] = None, venue='gh', advertise: Union[bool, NoneType] = None, session_info: bool = False, style: bool = False, comment: str = '#>', print_=True, terminal=False) ‑> reprexlite.reprex.Reprex`
:   Render reproducible examples of Python code for sharing. This function will evaluate your
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

Classes
-------

`Advertisement()`
:   Class for generating the advertisement note for reprexlite.

    ### Class variables

    `pkg`
    :

    `url`
    :

    ### Methods

    `code_comment(self) ‑> str`
    :

    `html(self) ‑> str`
    :

    `markdown(self) ‑> str`
    :

    `text(self) ‑> str`
    :

`GitHubReprex(code_block: reprexlite.code.CodeBlock, advertise: Union[bool, NoneType] = None, session_info: bool = False)`
:   Concrete implementation for rendering reprexes in GitHub Flavored Markdown.

    ### Ancestors (in MRO)

    * reprexlite.reprex.Reprex
    * abc.ABC

    ### Class variables

    `default_advertise: bool`
    :

`HtmlReprex(code_block: reprexlite.code.CodeBlock, advertise: Union[bool, NoneType] = None, session_info: bool = False)`
:   Concrete implementation for rendering reprexes in HTML. If optional dependency Pygments is
    available, the rendered HTML will have syntax highlighting for the Python code.

    ### Ancestors (in MRO)

    * reprexlite.reprex.Reprex
    * abc.ABC

    ### Class variables

    `default_advertise: bool`
    :

`PyScriptReprex(code_block: reprexlite.code.CodeBlock, advertise: Union[bool, NoneType] = None, session_info: bool = False)`
:   Concrete implementation for rendering reprexes as a Python script.

    ### Ancestors (in MRO)

    * reprexlite.reprex.Reprex
    * abc.ABC

    ### Class variables

    `default_advertise: bool`
    :

`Reprex(code_block: reprexlite.code.CodeBlock, advertise: Union[bool, NoneType] = None, session_info: bool = False)`
:   Abstract base class for a reprex instance. Concrete subclasses should implement the
    formatting logic appropriate to a specific venue for sharing.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Descendants

    * reprexlite.reprex.GitHubReprex
    * reprexlite.reprex.HtmlReprex
    * reprexlite.reprex.PyScriptReprex
    * reprexlite.reprex.RtfReprex
    * reprexlite.reprex.SlackReprex

    ### Class variables

    `default_advertise: bool`
    :

`RtfReprex(code_block: reprexlite.code.CodeBlock, advertise: Union[bool, NoneType] = None, session_info: bool = False)`
:   Concrete implementation for rendering reprexes in Rich Text Format.

    ### Ancestors (in MRO)

    * reprexlite.reprex.Reprex
    * abc.ABC

    ### Class variables

    `default_advertise: bool`
    :

`SlackReprex(code_block: reprexlite.code.CodeBlock, advertise: Union[bool, NoneType] = None, session_info: bool = False)`
:   Concrete implementation for rendering reprexes as Slack markup.

    ### Ancestors (in MRO)

    * reprexlite.reprex.Reprex
    * abc.ABC

    ### Class variables

    `default_advertise: bool`
    :

`Venue(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   Enum for valid venue options.

    ### Ancestors (in MRO)

    * builtins.str
    * enum.Enum

    ### Class variables

    `DS`
    :

    `GH`
    :

    `HTML`
    :

    `PY`
    :

    `RTF`
    :

    `SLACK`
    :

    `SO`
    :