# Configuration

reprexlite has the following configuration options.

> [!NOTE]
> Command-line option names for these configuration variables use hyphens instead of underscores.

{{ create_config_help_table() }}

## Configuration files

reprexlite supports reading default configuration values from configuration files. Both project-level files and user-level files are supported.

### `pyproject.toml`

reprexlite will search the nearest `pyproject.toml` file in the current working directory and any parent directory.
Configuration for reprexlite should be in the `[tool.reprexlite]` table following standard `pyproject.toml` specifications. For example:

```toml
[tool.reprexlite]
editor = "some_editor"
```

### `reprexlite.toml` or `.reprexlite.toml`

reprexlite also supports files named `reprexlite.toml` or `.reprexlite.toml` for project-level configuration. It will also search for these in the current working directory or any parent directory.

For reprexlite-specific files, all configuration options should be declared in the root namespace.

```toml
editor = "some_editor"
```

### User-level configuration

reprexlite supports searching standard platform-specific user configuration directories as determined by [platformdirs](https://github.com/tox-dev/platformdirs). Here are typical locations depending on platform:

| Platform | Path                                                       |
|----------|------------------------------------------------------------|
| Linux    | `~/.config/reprexlite/config.toml`                         |
| MacOS    | `~/Library/Application Support/reprexlite/config.toml`     |
| Windows  | `C:\Users\<username>\AppData\Local\reprexlite\config.toml` |

You can check where your user configuration would be with

```bash
python -m platformdirs
```

Look for the section `-- app dirs (without optional 'version')` for the value of `user_config_dir`. The value for `MyApp` is `reprexlite`. The configuration file should be named `config.toml` inside that directory.
