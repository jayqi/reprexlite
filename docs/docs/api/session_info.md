Module reprexlite.session_info
==============================

Functions
---------

    
`tabulate(rows: List[Tuple[str, str]]) ‑> List[str]`
:   

Classes
-------

`Package(distribution: importlib.metadata.Distribution)`
:   Interface for adapting [`importlib.metadata.Distribution`](https://docs.python.org/3/library/importlib.metadata.html#distributions)
    instances for introspection by [`SessionInfo`][reprexlite.session_info.SessionInfo].

    ### Instance variables

    `name: str`
    :

    `version: str`
    :

`SessionInfo()`
:   Class for pretty-formatting Python session info. Includes details about your Python version,
    your operating system, and the Python packages installed in your current environment.