import keyword
import re
reserved_words = set(keyword.kwlist)
with open("random_int.py", "r", encoding="utf-8") as f:
    original_code = f.read()
def convert_identifier(match):
    identifier = match.group()
    return identifier if identifier in reserved_words else identifier.upper()
pattern = r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"
processed_code = re.sub(pattern, convert_identifier, original_code)
with open("converted_random_int.py", "w", encoding="utf-8") as f:
    f.write(processed_code)
