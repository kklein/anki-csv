import csv
from pathlib import Path

import click


def validate_lines(lines: list):
    keys = set()
    for line in lines:
        if not isinstance(line, list):
            raise ValueError()
        if len(line) != 2:
            raise ValueError(f"A line had more than 2 values: \n {str(line)}")
        new_key = line[0].strip()
        if new_key in keys:
            raise ValueError(f"Key {new_key} occurs several times.")
        keys |= {new_key}


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
