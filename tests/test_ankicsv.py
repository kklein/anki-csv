import pytest

from ankicsv import validate


@pytest.mark.parametrize("input, expected_success", [
    ("asdf, asdf", True),
    ("""asdf, "asdf" """, True),
    ("asdf, asdf, asdf", False),
    (""" asdf, "asdf, asdf" """, True),
    ("""asdf, asdf
    asdf, asdf""", True),
    ("""asdf, asdf
    asdf,""", False),
    ("""asdf, asdf
    asdf, "asdf
    asdf
    asdf
    "
    asdf, asdf""", True),
])
def test_validate_single_line(input, expected_success):
    if expected_success:
        validate(input)
    else:
        with pytest.raises(ValueError):
            validate(input)


