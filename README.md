# clean-unwanted

A simple CLI tool to **recursively delete unwanted system or metadata files** (e.g., `.DS_Store`, `Thumbs.db`, `._*`) from any directory. Built with [Typer](https://typer.tiangolo.com) for a clean command-line experience.

---

## 🚀 Installation

### With [pipx](https://github.com/pypa/pipx) (recommended)

```bash
pipx install dist/clean_unwanted-0.1.0-py3-none-any.whl
````

### From source with Poetry

```bash
poetry install
poetry run clean-unwanted /path/to/dir
```

---

## 🧼 Default Behavior

Running the tool with just a directory will **recursively remove** these files:

* `.DS_Store`
* `Thumbs.db`
* `.Spotlight-V100`
* `desktop.ini`
* `._*` (resource forks from macOS)

```bash
clean-unwanted /path/to/dir
```

---

## 🧩 Custom Patterns

You can override the default list using one or more `--pattern` (or `-p`) flags. These support glob-style wildcards (`*`, `?`, etc.).

### Examples:

* Remove `.bak` and `.tmp` files:

  ```bash
  clean-unwanted . -p "*.bak" -p "*.tmp"
  ```

* Match a specific file name:

  ```bash
  clean-unwanted . -p ".DS_Store"
  ```

* Match all hidden files:

  ```bash
  clean-unwanted . -p ".*"
  ```

> Note: Specifying `--pattern` replaces the default list.

---

## 🔧 Options

```bash
Usage: clean-unwanted [OPTIONS] DIRECTORY

Arguments:
  DIRECTORY  Target directory to clean.  [default: .]

Options:
  -p, --pattern TEXT  File pattern(s) to remove (can use wildcards). [default: .DS_Store,Thumbs.db, .Spotlight-V100, desktop.ini, ._*]
  -v, --verbose       Print each matched file.
  --dry-run           Preview what will be deleted without removing anything.
  --help              Show this message and exit.
```

---

## 📂 Example

```bash
clean-unwanted ~/Projects --dry-run --verbose
```

---

## 🛠 License

MIT License.

