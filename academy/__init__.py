"""Find the public URLs of Academy course datasets."""
from difflib import get_close_matches
from ._registry import FILES

_BASE_URL = "https://raw.githubusercontent.com/HassanAlgoz/academy-data/v1/"


def get_data_url(name: str | None = None) -> str:
    """Return the raw GitHub URL for a named dataset.

    Args:
        name: Dataset name shown on its Academy dataset card.

    Returns:
        An HTTPS URL suitable for pandas.read_csv or a browser.

    Raises:
        TypeError: The supplied name is not a string.
        ValueError: The name is missing, empty, or unknown.

    Examples:
        >>> get_data_url("tips").endswith("/data/tips/tips.csv")
        True
    """
    choices = ", ".join(sorted(FILES))
    if name is None or (isinstance(name, str) and not name.strip()):
        raise ValueError('Supply a dataset name, for example academy.get_data_url("tips"). Available names: ' + choices)
    if not isinstance(name, str):
        raise TypeError("Dataset name must be a string. Available names: " + choices)
    if name not in FILES:
        similar = get_close_matches(name, FILES, n=3, cutoff=0.5)
        suggestion = (" Did you mean " + ", ".join(repr(item) for item in similar) + "?") if similar else ""
        raise ValueError(f"Unknown dataset {name!r}.{suggestion} Available names: {choices}")
    return _BASE_URL + FILES[name]
