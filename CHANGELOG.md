# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v1.0.0 (Unreleased)

This release involves major changes to reprexlite. There is a significant refactoring of the library internals and also many changes to the API. This enabled new feature and more customizability.

_This release also removes support for Python 3.6, 3.7, and 3.8._

### CLI and IPython User Interfaces

#### Added

- Added a new `--editor`/`-e` option to specify what editor to use. If not used, this has same behavior as before. This option is also the new way to launch the IPython interactive shell editor (by passing `ipython`).
- Added new options to control parsing and output style.
  - `--prompt` and `--continuation` options let you set the primary and secondary prompt prefixes in rendered output. These default to empty srings `""` for "reprex-style" output.
  - A new `--parsing-method` option controls input-parsing behavior.
    - The default value `auto` can automatically handle "reprex-style" input as well as "doctest-style`/Python REPL input.
    - A value `declared` will use the values of `--prompt`, `--continuation`, and `--comment` for parsing input in addition to styling output. To handle input and output with different styes, you can override input-side values with the `--input-prompt`, `--input-continuation`, and `--input-comment` options.
- Added support for configuration files, including support for `[tool.reprexlite]` in `pyproject.toml` files and for user-level configuration. See ["Configuration"](https://jayqi.github.io/reprexlite/stable/configuration/#configuration-files) for more details.

#### Changed

- Changed the way to access the IPython interactive shell editor. This is now launched by using the new `--editor`/`-e` option by passing `ipython`. The IPython shell editor also now respects other command line configuration options. It is now considered a stable feature and is no longer experimental.
- Renamed the `--old-results` option to `--keep-old-results`.

#### Fixed

- Fixed bug that silenced output when using the IPython cell magic or the IPython shell editor and encountering an error where reprexlite couldn't render your code (such as a syntax error). This should now display an informative error message.

### Library

#### Added

- Added new `reprexlite.parsing` module which contains functions for parsing input. These functions yield tuples representing lines of the input with an enum indicating whether the line is code or a result.
- Added new `reprexlite.reprexes` module which contains code for evaluating a reprex.
  - The new `Reprex` dataclass serves as the main container for reprex data. It holds parallel lists of `Statement`, `ParsedResult`, and `RawResult` data.
    - The `Reprex.from_input_lines` factory method creates a `Reprex` from the output of the `reprexlite.parsing` parsing functions.
    - The `Reprex.from_input` factory method wraps parsing and takes a string input.
  - The `Statement` dataclass holds code data and parsed concrete syntax tree. This serves a similar purpose to the old `Statement` class.
  - The `ParsedResult` dataclass holds old evaluation results parsed from the input, if any.
  - The `RawResult` dataclass holds the returned values from evaluating code. This serves a similar purpose to the old `Result` class.
- Added new `reprexlite.config` module and `ReprexConfig` dataclass for holding configuration values.
- Added new `reprexlite.exceptions` module with exception classes that subclass a base exception class `ReprexliteException`.

#### Changed

- Changed formatting abstractions in `reprexlite.formatting` module.
  - Rather than `*Reprex` classes that encapsulate reprex data, we now have formatter callables and take a rendered reprex output string as input and appropriately prepares the reprex output for a venue, such as adding venue-specific markup.
  - The `venues_dispatcher` dictionary in `reprexlite.formatting` is now a `formatter_registry` dictionary-like.
  - Formatters are added to the registry using a `formatter_registry.register` decorator instead of being hard-coded.

#### Removed

- Removed `reprexlite.code` module. The functionality in this module was reimplemented in the new `reprexlite.reprexes` and `reprexlite.parsing` modules.
- Removed `reprexlite.reprex` module. The `reprex` function has been moved to `reprexlite.reprexes`.

### General

#### Added

- Added a "Rendering and Output Venues" page to the documentation that documents the different formatting options with examples.
- Added a "Configuration" page to the documentation that provides a reference for configuration options and documents how to use configuration files.
- Added an "Alternatives" page to the documentation that documents alternative tools.

#### Changed

- Changed reprexlite to use a pyproject.toml-based build process and metadata declaration.
- Renamed `HISTORY.md` to `CHANGELOG.md`.

## v0.5.0 (2020-02-20)

- Added experimental IPython interactive editor which can be launched via command line with `reprex --ipython`. This modified IPython editor will run every cell automatically as a reprex.

## v0.4.3 (2021-11-05)

- Added explicit setting of code evaluation namespace's `__name__` to `'__reprex__'`. Previously this was unset and would get inferred, and weird things like `'builtins'` would turn up. ([PR #44](https://github.com/jayqi/reprexlite/pull/44))

## v0.4.2 (2021-02-28)

- Added support for parsing code copied from an interactive Python shell (REPL) with `>>>` prompts. ([#29](https://github.com/jayqi/reprexlite/pull/29))
- Fixed issue where `tests` module was unintentionally included in distribution. ([#30](https://github.com/jayqi/reprexlite/pull/30))
- Fixed missing requirement `importlib_metadata` for Python 3.6 and 3.7. ([#31](https://github.com/jayqi/reprexlite/pull/31))

## v0.4.1 (2021-02-27)

- Added missing LICENSE file.

## v0.4.0 (2021-02-27)

- Added optional IPython extension that enables `%%reprex` cell magic. See [documentation](https://jayqi.github.io/reprexlite/stable/ipython-jupyter-magic/) for usage. ([#21](https://github.com/jayqi/reprexlite/pull/21))

## v0.3.1 (2021-02-26)

- Documentation improvements. ([#14](https://github.com/jayqi/reprexlite/pull/14), [#19](https://github.com/jayqi/reprexlite/pull/19))

## v0.3.0 (2021-02-25)

- Changed pygments styling to use the "friendly" color scheme, which looks better for dark backgrounds. ([#15](https://github.com/jayqi/reprexlite/pull/15))
- Changed submodule organization for code related to reprex formatting. This is now in the `formatting` submodule. ([#17](https://github.com/jayqi/reprexlite/pull/17))

## v0.2.0 (2021-02-20)

- Removing old results from inputs: ([#8](https://github.com/jayqi/reprexlite/pull/8))
  - Changed reprexes to—by default—remove lines matching the `comment` prefix (`#>` by default). This means that if your input code is a previously rendered reprex, the old results will be removed first and you effectively regenerate it.
  - Added a new option `old_results` that—if set to True—will preserve such lines.
- Fixed a bug that caused intentional blank lines to be removed. ([#7](https://github.com/jayqi/reprexlite/pull/7))
- Added stdout capturing. Any content printed to stdout will be shown as a result in the reprex. ([#10](https://github.com/jayqi/reprexlite/pull/10))
- Added exception handling and stacktrace capture. If the input code has an exception, the stacktrace will be shown as a result in the reprex. ([#12](https://github.com/jayqi/reprexlite/pull/12))

## v0.1.0 (2021-02-15)

Initial release! 🎉
