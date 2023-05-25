import re

def is_strong(password):
    """
    This function checks whether a given password is strong.
    A strong password is defined as being at least eight characters long,
    containing at least one uppercase letter, one lowercase letter, and one digit.

    Parameters:
    password (str): The password to check.

    Returns:
    bool: True if the password is strong, False otherwise.
    """
    if len(password) < 8:
        return False
    elif not re.search(r'[a-z]', password):
        return False
    elif not re.search(r'[A-Z]', password):
        return False
    elif not re.search(r'[0-9]', password):
        return False
    else:
        return True
