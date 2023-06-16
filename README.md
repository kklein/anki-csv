This is a functionality to validate whether csv files comply with Anki's
basic flashcard format.

## Usage as pre-commit hook

TODO

## Usage as script

TODO


## Development

Recommended initial setup looks as follows:
```bash
$ git clone git@github.com:kklein/anki-csv.git
$ cd anki-csv
$ mamba env create -f environment.yaml
$ mamba activate anki-csv
$ pre-commit install
```

Then, when changes to the source code have been made, install the package via

```bash
$ pip install .
```

and run the tests via

```bash
$ pytest tests/
```


