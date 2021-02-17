# reprexlite Changelog

## v0.2.0 (2021-02-17)

- Removing old results from inputs: ([#8](https://github.com/jayqi/reprexlite/pull/8))
  - Changed reprexes to—by default—remove lines matching the `comment` prefix (`#>` by default). This means that if your input code is a previously rendered reprex, the old results will be removed first and you effectively regenerate it.
  - Added a new option `old_results` that—if set to True—will preserve such lines.
- Fixed a bug that caused intentional blank lines to be removed. ([#7](https://github.com/jayqi/reprexlite/pull/7))

## v0.1.0 (2021-02-15)

Initial release! 🎉
