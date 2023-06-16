import re


def validate(body: str) -> None:
    pattern_line_non_escaped = "[^,]+[,]{1}[^,]+"
    pattern_line_escaped = r"[^,]+[,]{1}\s*[\"]{1}[^\"]+[\"]{1}\s*"
    pattern_line = f"({pattern_line_non_escaped}|{pattern_line_escaped})"
    pattern = re.compile(f"^({pattern_line}(\n)+)*{pattern_line}\n*$")
    if pattern.match(body) is None:
        raise ValueError()
