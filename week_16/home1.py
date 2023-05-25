import re

def extract_usernames():
    """
    This function extracts usernames from University of Tartu's home page URLs found in 'addresses.txt' file.
    Each URL is of the format 'http(s)://www.ut.ee/~username/', where 'username' is the username to be extracted.
    The function prints each username on a separate line.
    """
    with open('addresses.txt', 'r') as file:
        for line in file:
            match = re.search(r'http(s)?://www\.ut\.ee/~([^/]+)/', line)
            if match:
                print(match.group(2))


# Call the function
extract_usernames('addresses.txt')