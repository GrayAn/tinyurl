import string

SHORT_URL_SYMBOLS = string.ascii_lowercase + string.digits


def generate_short_url(full_url: str, length: int) -> str:
    """
    Lowercase latin letters and digits are used for short URLs.
    Each symbol is extracted from the hash of the full URL.
    """
    full_url_hash = hash(full_url)
    result = []
    while len(result) < length:
        position = full_url_hash % len(SHORT_URL_SYMBOLS)
        result.append(SHORT_URL_SYMBOLS[position])
        full_url_hash = (full_url_hash - position) // len(SHORT_URL_SYMBOLS)
    return ''.join(result)
