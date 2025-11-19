import re

PASSWORD_PATTERN = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$"


def is_secure(password: str):
    return bool(re.match(PASSWORD_PATTERN, password))
