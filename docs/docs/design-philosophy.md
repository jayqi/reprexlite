# Design Philosophy

Reprex is a portmanteau for **repr**oducible **ex**ample. This term and its ideal characteristics have been popularized within the R data science community, driven by the adoption of the [reprex](https://reprex.tidyverse.org/index.html) tidyverse package.

> The reprex code:
>
> - Must run and, therefore, should be run by **the person posting**. No faking it.
> - Should be easy for others to digest, so **they don’t necessarily have to run it**. You are encouraged to include selected bits of output.
> - Should be easy for others to copy + paste + run, **if and only if they so choose**. Don’t let inclusion of output break executability.
>
> <p style="text-align: right">― <a href="https://reprex.tidyverse.org/articles/reprex-dos-and-donts.html#package-philosophy">"Package Philosophy,"</a> from the R reprex documentation</p>

A good reprex depends on what you put into it (see ["Reprex Do's and Don'ts"](../dos-and-donts)). But it also helps to have a good tool that lowers the barrier to making one, so that you can't use formatting as an excuse not to. If you've put in the work of creating good content for an example, it should be easy to format it in a way that is readable and is easy to copy, paste, and run. The goal of reprexlite is to be such a tool for Python.

## Why reproducible examples?

<div style="float: right; margin-left: 2ch; "><img src="../images/help-me-help-you.png" /><p style="font-size: small; text-align: center; margin-top: 0;">From the R reprex <a href="https://reprex.tidyverse.org/index.html">readme</a>.</p></div>

### If you're looking for help with a problem or bug...

...you are more likely to succeed if you make it as easy as possible for others to help you. You are asking people to do work on your behalf. Remember: most open-source software maintainers and StackOverflow posters are volunteers and are not obligated to help you. Even someone who is obligated to help you would still be able to get to an answer more quickly if you make it easier for them to understand your problem.

Plus, the exercise of writing the reprex might even help you figure out how to solve the problem yourself. This is basically the principle of [rubber duck debugging](https://rubberduckdebugging.com/).

### If you're writing a tutorial or documentation...

...actual working examples are valuable to your users. A reprex—with complete directly runnable code and showing the expected outputs—will show your audience what you're demonstrating, and also give them the option to easily try for themselves. Doing is often the most effective way of learning how to do something in code. And, with documentation especially, people often just want to arrive at working code for their use case as quickly as possible. Something that they can just copy and run is exactly what they're looking for.

## Reprex vs. Copying from shell (doctest-style)

A widely used approach for Python code examples is copying from an interactive Python shell. It is easily recognized from the `>>>` prompt before each code statement. Such a code example is sometimes called a "doctest" because the [`doctest` module](https://docs.python.org/3/library/doctest.html) from the Python standard library is able to parse it.

```python
>>> import math
>>> math.sqrt(4)
2.0
```

This style of code example takes no special tools to generate: simply open a `python` shell from command line, write your code, and copy what you see. Many Python packages use it for their documentation, e.g., [requests](https://requests.readthedocs.io/en/master/). There is also tooling for parsing it. The doctest module can run such examples in the docstrings of your scripts, and test that the output matches what is written. Other tools like [Sphinx](https://www.sphinx-doc.org/en/1.4.9/markup/code.html) are able to parse it when rendering your documentation into other formats.

The drawback of doctest-style examples is that they are _not_ valid Python syntax, so you can't just copy, paste, and run such  examples. The `>>>` prompt is not valid. While IPython's interactive shell and Jupyter notebooks _do_ support executing code with the prompt, it won't work in a regular Python REPL or in Python scripts. Furthermore, since the outputs might be anything, they may not be valid Python syntax either, depending on their `repr`. A barebones class, for example, will look like `<__main__.MyClass object at 0x7f932a001400>` and is not valid.

So, while no special tools were needed to _generate_ a doctest-style example, either special tools or manual editing are needed to _run_ it. This puts the burden on the person you're sharing with, which is counterproductive. As discussed in the previous section, we want reproducible examples to make it _easier_ for others to run your code.

In contrast, reprexes _are_ valid Python code. Anyone can copy, paste, and run a reprex without any special tools or manual editing required.

```python
import math
math.sqrt(4)
#> 2.0
```

## reprexlite's Design

The primary design goal of reprexlite is that it should be **quick and convenient** to use. That objective drove the emphasis on following the design characteristics:

- **Lightweight**. reprexlite needs to be in your virtual environment to be able to run your code. By having minimal and lightweight dependencies itself, reprexlite is quick to install and is unlikely to conflict with your other dependencies.
- **Quick access**. reprexlite comes with a CLI, so you can quickly create a reprex without needing to start a Python shell or to import anything.

The API, including the available configuration and naming of parameters, mostly matches both [R reprex](https://reprex.tidyverse.org/) and [reprexpy](https://github.com/crew102/reprexpy). The intent is that anyone familiar with these other tools can quickly feel comfortable with reprexlite.

As a secondary objective, the reprexlite library is designed so that its underlying functionality is accessible and extensible. It has a modular object-oriented design based on composition. Individual parts, like the code parsing or the output formatting, can be used independently, extended, or replaced. Additionally, the library is thoroughly type-annotated and documented.

## Limitations

Compared to [R reprex](https://reprex.tidyverse.org/) and [reprexpy](https://github.com/crew102/reprexpy), reprexlite does trade off some capabilities in favor of our design objective. Known limitations include:

- **No clipboard integration.** The two main Python clipboard libraries, [pyperclip](https://github.com/asweigart/pyperclip) and [xerox](https://github.com/adityarathod/xerox), have non-Python dependencies on some OSes that make them sometimes difficult to install. However, command-line editor support built-in to the CLI is nearly as easy as reading from clipboard, and has the added benefit that you can see the code before it gets executed.
- **No plot image support.** Both R reprex and reprexpy support automatically uploading plots to imgur.com and injecting the link into your outputed reprex. This always seemed to me like a weird default as it could lead to inadvertent leaking of private data.
- **Code is not run in a subprocess, so it's not perfectly isolated.** reprexlite runs the code using `eval` and `exec` with a fresh namespace, but otherwise still executes code within the main Python process. That means, for example, modules that are stateful or have been monkeypatched could potentially leak that state into the reprex.

By not supporting the first two functionalities, reprexlite has significantly fewer and simpler dependencies. Both of these features, while convenient, could lead to unintentional code execution or leaking data to the public web. From that perspective, I believe this is a worthwhile tradeoff.

The third limitation is one where feedback is welcome. Hopefully it will only matter in unusual edge cases. If you have ideas for mitigation for the current `eval`-`exec` implementation, please [open an issue on GitHub](https://github.com/jayqi/reprexlite/issues). A subprocess-based implementation would solve this, but would be more difficult to capture output from—any implementation ideas for this approach are also welcome.
