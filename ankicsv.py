from pathlib import Path
import re
import click
import csv


def validate_string(body: str) -> None:
    pattern_line_non_escaped = "[^,]+[,]{1}[^,]+"
    pattern_line_escaped = r"[^,]+[,]{1}\s*[\"]{1}[^\"]+[\"]{1}\s*"
    pattern_line = f"({pattern_line_non_escaped}|{pattern_line_escaped})"
    pattern = re.compile(f"^({pattern_line}(\n)+)*{pattern_line}\n*$")
    return pattern.match(body)


def validate_lines(lines: list):
    keys = set()
    for line in lines:
        if not isinstance(line, list):
            raise ValueError()
        if len(line) != 2:
            raise ValueError(
                "A line had more than 2 values: \n"
                f"{str(line)}"
            )
        new_key = line[0].strip()
        if new_key in keys:
            raise ValueError(f"Key {new_key} occurs several times.")
        keys |= {new_key}


def validate_file(file: Path) -> None:
    with open(file, "r") as fh:
        print(f"Validating {file}.")
        reader = csv.reader(
            fh, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True
        )
        validate_lines(list(reader))


@click.group()
def cli():
    pass


@cli.command("validate")
@click.argument(
    "csv_path", type=click.Path(exists=True, file_okay=False, dir_okay=True)
)
def validate(csv_path):
    path = Path(csv_path)
    files = [f for f in path.iterdir() if f.is_file() and f.suffix == ".csv"]
    print(f"Validating the following files: {files}")
    for file in files:
        validate_file(file)
