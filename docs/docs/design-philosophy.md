# Design Philosphy

Reprex is a portmanteau for **repr**oducible **ex**ample. It come to mean a certain to approach and formatting of code examples within the R data science community, driven by the adoption of the [reprex](https://reprex.tidyverse.org/index.html) tidyverse package. In particular, a good reprex should meet the following criteria:

> The reprex code:
>
> - Must run and, therefore, should be run by **the person posting**. No faking it.
> - Should be easy for others to digest, so **they don’t necessarily have to run it**. You are encouraged to include selected bits of output.
> - Should be easy for others to copy + paste + run, **if and only if they so choose**. Don’t let inclusion of output break executability.
>
> <p style="text-align: right">― <a href="https://reprex.tidyverse.org/articles/reprex-dos-and-donts.html#package-philosophy">"Package Philosophy,"</a> from the R reprex documentation</p>

Most of what makes a good reprex is what you choose to put into it (see ["Reprex Do's and Don'ts"](../dos-and-donts)). But another important part is a good tool that lowers the barrier to making one, so that you don't have that as an excuse. It should be easy to create a reprex in a format that others can simply copy, paste, and run. reprexlite aims to be such a tool for Python.

## Why reproducible examples?

There are generally two kinds of situations that call for a code example:

1. You have a problem, and you want to get help or report a bug
2. You're trying to teach, whether in a presentation or in documentation

In both of these situations, having a reprex that meets the ideals from earlier removes friction for your audience, making it more likely that you succeed in communicating with them.

If you have a problem, you are more likely to succeed in getting the help if you make it as easy as possible for them to help you. This is true whether or not they're obligated to help you—and remember, most open-source software maintainers are volunteers and have no such obligations.

Actual working examples are also a great way to teach someone how to do something with code. They'll be able to see what you're doing, and to tinker with it themselves if they choose to. Furthermore, users reading documentation often would prefer to get to code that works as fast as possible, and a reprex is a great way to do that.

## vs. Copying from shell (doctest-style)

A widely used standard for Python code examples is copying from an interactive Python shell. It is easily recognized from the `>>>` prompt before each code statement. Such a code example is sometimes called a "doctest" because the [`doctest` module](https://docs.python.org/3/library/doctest.html) from the Python standard library is able to parse it.

```python
>>> import math
>>> math.sqrt(4)
2.0
```

This style of code example takes no special tools to generate: simply open a `python` shell from command line, write your code, and copy what comes out. Many Python packages use it for their documentation, like [requests](https://requests.readthedocs.io/en/master/). There is also tooling for parsing it. The doctest module can run such examples in the docstrings of your scripts, and test that the output matches what is written. Other tools like [Sphinx](https://www.sphinx-doc.org/en/1.4.9/markup/code.html) are able to parse it when rendering your documentation into other formats.

The drawback of doctest-style examples is that it is not valid Python syntax, so you can't just copy, paste, and run such an example. The `>>>` prompt is not valid syntax. While IPython's interactive shell and Jupyter notebooks _do_ support executing code with the prompt, it won't work in a regular Python REPL or in Python scripts. Furthermore, since the outputs might be anything, they may not be valid Python syntax either, depending on their `repr`. A barebones class for example, will look like `<__main__.MyClass object at 0x7f932a001400>` and is not valid syntax. While no special tools were needed to _generate_ the example, special tools, or a lot of manual deleting of `>>>` and outputs, are needed to _run_ it.

In contrast, reprexes _are_ valid Python code. Anyone can copy, paste, and run a reprex with special tools or manual editing required.

```python
import math
math.sqrt(4)
#> 2.0
```

## reprexlite's Design

The primary design goal of reprexlite is that it should be *quick and convenient* to use. That objective drove the emphasis on following design characteristics.

- *Lightweight*. reprexlite needs to be in your virtual environment to be able to run your code. By having minimal and lightweight dependencies itself, reprexlite is quick to install and is unlikely to conflict with your other dependencies.
- *Quick access*. reprexlite comes with a CLI, so you can quickly create a reprex without needing to start a Python session or import anything.

The API, including the available configuration and naming of parameters, mostly matches both R reprex and reprexpy. The intent is that anyone familiar with these other tools can quickly feel comfortable with reprexlite.

As a secondary objective, the reprexlite library is designed so that its logic is accessible and extensible. It has a modular object-oriented design based on composition. Individual parts, like the code parsing or the output formatting, can be used independently, extended, or replaced. The library is thoroughly type-annotated.

## Limitations

Compared to R reprex and reprexpy, reprexlite does trade off some capabilities in favor of our design objective:

- *No clipboard integration.* The two main Python clipboard libraries, pyperclip and xerox, have non-Python dependencies on some OSes that make them sometimes difficult to install. However, command-line editor support built-in to the CLI is nearly as easy as reading from clipboard, and has the added benefit that you can see the code before it gets executed.
- *No plot image support.* Both R reprex and reprexpy support automatically uploading plots to imgur.com and injecting the link into your outputed reprex. This always seemed to me like a weird default as it could lead to inadvertent leaking of private data.
- *Code is not run in a subprocess, so it's not perfectly isolated.* That means, for example, modules that are stateful or have monkeypatching could potentially leak that state into the reprex.

By not supporting the first two functionalities, reprexlite has significantly fewer and simpler dependencies. Both of these features, while convenient, could lead to unintentional code execution or leaking data to the public web. From that perspective, I believe this is a worthwhile tradeoff.

The third limitation is one where feedback is welcome. Hopefully it will only turn up in unusual edge cases. Mitigation ideas using the current `eval`-`execute` implementation would be appreciated. A subprocess-based implementation would solve this, but would be more difficult to capture output from—any implementation ideas here are also welcome.
