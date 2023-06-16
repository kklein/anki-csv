from pathlib import Path

import pytest

from ankicsv import validate_file


@pytest.mark.parametrize(
    "file, expected_success",
    [
        ("missing_value.csv", False),
        ("duplicate_key.csv", False),
        ("superfluous_comma.csv", False),
        ("multiline.csv", True),
        ("escaped_comma.csv", True),
    ],
)
def test_validate(file, expected_success):
    path = Path(__file__).parent / file
    print(path)
    if expected_success:
        validate_file(path)
    else:
        with pytest.raises(ValueError):
            validate_file(path)
