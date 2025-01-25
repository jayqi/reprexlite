# Configuration

reprexlite has the following configuration options.

> [!NOTE]
> Command-line option names for these configuration variables use hyphens instead of underscores.

{{ create_config_help_table() }}

## Configuration files

reprexlite supports reading default configuration values from configuration files. It will search for files named `pyproject.toml`, `reprexlite.toml`, or `.reprexlite.toml`, and will search for both project-scope configuration and user-scope configuration files.

### Configuration file formats

#### `pyproject.toml`

reprexlite will read from the `[tool]` table of a `pyproject.toml` file.  For example:

```toml
[tool.reprexlite]
editor = "some_editor"
```

#### `reprexlite.toml` or `.reprexlite.toml`

For reprexlite-specific files, all configuration options should be declared in the root namespace.

```toml
editor = "some_editor"
```

### Configuration file search locations

#### Project configuration

reprexlite will search for configuration files in the current working directory and all parent directories of the current working directory.

#### User configuration

reprexlite supports searching standard platform-specific user configuration directories as determined by [platformdirs](https://github.com/tox-dev/platformdirs). The file should be within the `reprexlite` subdirectory.

For example, if your user configuration directory is `~/.config/` then you can have a configuration file like `~/.config/reprexlite/reprexlite.toml`.

On Linux and MacOS, the `XDG_CONFIG_DIR` environment variable is supported for explicitly setting the user configuration directory.
