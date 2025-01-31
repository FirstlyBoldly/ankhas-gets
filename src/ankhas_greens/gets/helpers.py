"""Utility functions for Ankha's Gets."""
# Built-ins
import unicodedata
import re

# Ankha's Gets
from errors import NonIntegerError


def warn(warning: str) -> None:
    """Prints the warning message the stream, if there is one."""
    if warning:
        print(warning)


def float_to_int(float_number: float, warning: str = '') -> int:
    """Return a float as an integer if said float can be converted into an integer without loss of data.
    Raises a NonIntegerError otherwise.
    """
    if float_number.is_integer():
        return int(float_number)
    else:
        raise NonIntegerError(warning)


def normalize_to_ascii(non_ascii_string: str) -> str:
    """Convert a Japanese full-width number to half-width."""
    return re.sub('[ー－―—‐]', '-', unicodedata.normalize('NFKC', non_ascii_string))
