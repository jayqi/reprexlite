# Reprex Do's and Don'ts

This article discusses how to write an effective reprex. If you're asking for help or sharing code with someone, you will be much more likely to succeed if you have a good reprex. If you still need to be convinced why you should write a reprex or use reprexlite, check out the first half of ["Design Philosophy"](../design-philosophy/).

Many of the key ideas in this article are borrowed from R reprex's ["Reprex do's and don'ts"](https://reprex.tidyverse.org/articles/reprex-dos-and-donts.html) and StackOverflow's ["How to create a Minimal, Reproducible Example"](https://stackoverflow.com/help/minimal-reproducible-example).

## Your reprexes should be...

### Minimal

- **Do** use the smallest, simplest data possible.
  - If working with the PyData stack, the [`sklearn.datasets` module](https://scikit-learn.org/stable/datasets.html#datasets) has convenient toy datasets like `iris`.
- **Don't** include code unrelated to the specific thing you want to demonstrate.
  - **Do** ruthlessly remove unnecessary code. If you're not sure, try removing things bit by bit until it doesn't produce what you want anymore.
  - Consider starting your reprex from scratch. This helps force you to add in only what is needed.


### Readable

- **Do** follow [code style best practices](https://www.python.org/dev/peps/pep-0008/).
  - Consider using the `style` option which will use [black](https://github.com/psf/black) to autoformat your code.
- **Don't** sacrifice clarity for brevity.
  - **Don't** play [code golf](https://en.wikipedia.org/wiki/Code_golf). For loops and if-else blocks can often be more readable.
  - **Do** use clear, descriptive, and idiomatic naming conventions.


### Reproducible

- **Do** include everything required to produce your example, including imports and custom class/function definitions. If you're using reprexlite, your code won't work without this anyways.
- **Do** detail what versions of relevant package, Python, and OS you are using.
  - Consider using the `session_info` option, which will include information about your Python, OS, and installed packages at the end of your reprex.
- **Do** double-check that your example reproduces the thing you want to show. One can often inadvertently solve a problem they were trying to debug when writing an example.
- **Don't** hardcode paths that wouldn't exist on someone else's computer, especially absolute paths.

### Respectful of other people's computers

- **Do** clean up after yourself if you create files. Take advantage of Python's [`tempfile` module](https://docs.python.org/3/library/tempfile.html) for creating temporary files and directories.
- **Don't** delete files that you didn't create.

## This seems like a lot of work!

> Yes, creating a great reprex requires work. You are asking other people to do work too. It’s a partnership.
>
> 80% of the time you will solve your own problem in the course of writing an excellent reprex. YMMV.
>
> The remaining 20% of the time, you will create a reprex that is more likely to elicit the desired behavior in others.
>
> <p style="text-align: right">― <a href="https://reprex.tidyverse.org/articles/reprex-dos-and-donts.html#this-seems-like-a-lot-of-work">"Reprex do's and don'ts,"</a> from the R reprex documentation</p>
