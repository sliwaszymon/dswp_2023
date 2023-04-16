from typing import Any

def extract_numbers(vals: list[Any]) -> list[int | float]:
    return list(filter(lambda x: (isinstance(x, int) or isinstance(x, float)) and not isinstance(x, bool), vals))

print(extract_numbers(['a', True, '3', 3, 2.11]))