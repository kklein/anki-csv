`anki-csv` is a tool to validate whether csv files comply with [Anki](https://apps.ankiweb.net/)'s basic flashcard format.

## Usage as pre-commit hook

Either create a `.pre-commit-config.yaml` file in the top level
of your repository or add an entry to `repos`:

```yml
repos:
  - repo: https://github.com/kklein/anki-csv
    rev: 0.0.1
    hooks:
      - id: anki-csv
```

Once this file has been created or adapted, you can install the hooks, via

```console
pre-commit install
```

This will ensure that whenever you try to `git commit`, the hooks will be run first.
If you want to commit despite a hook failing, you can always run:

```console
git commit -m "Fix bug" --no-verify
```

Aside from the `git commit` hook mechanism, you can always run the hooks proactively at any
point in time by e.g. running:

```console
pre-commit run --all-files
```

Find more details in the [pre-commit docs](https://pre-commit.com/).

## Usage as script

TODO


## Development

Recommended initial setup looks as follows:
```console
$ git clone git@github.com:kklein/anki-csv.git
$ cd anki-csv
$ mamba env create -f environment.yaml
$ mamba activate anki-csv
$ pre-commit install
```

Then, when changes to the source code have been made, install the package via

```console
$ pip install .
```

and run the tests via

```console
$ pytest tests/
```


