# reprexlite Changelog

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
