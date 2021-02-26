# reprexlite Changelog

## v0.3.0 (2021-02-25)

- Updated pygments styling to use the "friendly" color scheme, which looks better for dark backgrounds. ([#15](https://github.com/jayqi/reprexlite/pull/17))
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
