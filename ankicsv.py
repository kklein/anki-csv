import csv
from pathlib import Path

import click


def validate_lines(lines: list):
    keys = set()
    for line in lines:
        if not isinstance(line, list):
            raise ValueError("Parsing of csv file failed.")
        length = len(line)
        if length == 0:
            continue
        elif length == 1:
            element = line[0]
            # We tolerate comments indicated by a hash.
            if not hasattr(element, "__str__") or not str(element).startswith("#"):
                raise ValueError(
                    "A line had only 1 values; it was expected to contain two values. \n"
                    f"{str(line)}"
                )
        elif length == 2:
            new_key = line[0].strip()
            if new_key in keys:
                raise ValueError(f"Key {new_key} occurs several times.")
            keys |= {new_key}
        else:
            raise ValueError(
                f"A line had {length} values; it was expected to contain only two values.\n "
                f"{str(line)}"
            )


def validate_file(file: Path) -> None:
    with open(file) as fh:
        print(f"Validating {file}.")
        reader = csv.reader(
            fh,
            quotechar='"',
            delimiter=",",
            quoting=csv.QUOTE_ALL,
            skipinitialspace=True,
        )
        validate_lines(list(reader))


@click.group()
def cli():
    pass


@cli.command("validate")
@click.argument(
    "csv_paths", type=click.Path(exists=True, file_okay=True, dir_okay=False), nargs=-1
)
def validate(csv_paths):
    for csv_path in csv_paths:
        path = Path(csv_path)
        validate_file(path)
