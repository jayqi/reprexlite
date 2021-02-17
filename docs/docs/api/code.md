Module reprexlite.code
======================

Variables
---------

    
`NO_RETURN`
:   Explicit placeholder object for statements, which have no return value (as opposed to
    expressions).

Classes
-------

`CodeBlock(input: str, style: bool = False, comment: str = '#>', terminal=False)`
:   Class that takes a block of Python code input and evaluates it. Call `str(...)` on an
    instance to get back a string containing the original source with evaluated outputs embedded
    as comments below each statement.
    
    Attributes:
        input (str): Block of Python code
        style (bool): Whether to use black to autoformat code in returned string representation.
        comment (str): Line prefix to use when rendering the evaluated results.
        terminal (bool): Whether to apply syntax highlighting to the string representation.
            Requires optional dependency Pygments.
        tree (libcst.Module): Parsed LibCST concrete syntax tree of input code.
        statements (List[Statement]): List of individual statements parsed from input code.
        results (List[Result]): List of evaluated results corresponding to each item of statements.

`Result(result: Any, comment: str = '#>')`
:   Class that holds the result of evaluated code. Use `str(...)` on an instance to produce a
    pretty-formatted comment block representation of the result.
    
    Attributes:
        result (Any): Some Python object, intended to be the return value of evaluated Python code.
        comment (str): Line prefix to use when rendering the result for a reprex.

`Statement(stmt: Union[libcst._nodes.statement.SimpleStatementLine, libcst._nodes.statement.BaseCompoundStatement], style: bool = False)`
:   Class that holds a LibCST parsed statement. The evaluate method will evaluate the statement
    and return a [`Result`][reprexlite.code.Result] object. To recover the original source code
    for an instancement, call `str(...)` on it. You can optionally autoformat the returned source
    code, controlled by the `style` attribute.
    
    Attributes:
        stmt (Union[libcst.SimpleStatementLine, libcst.BaseCompoundStatement]): LibCST parsed
            statement.
        style (bool): Whether to autoformat the source code with black.

    ### Methods

    `evaluate(self, scope: dict) ‑> reprexlite.code.Result`
    :