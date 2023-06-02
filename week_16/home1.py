import re

def extract_usernames(filename):
    """
    This function extracts usernames from University of Tartu's home page URLs found in the given file.
    Each URL is of the format 'http(s)://www.ut.ee/~username/', where 'username' is the username to be extracted.
    The function returns a list of usernames.
    
    Parameters:
    filename (str): Name of the text file to be processed.

    Returns:
    list: A list of extracted usernames.
    """
    usernames = []

    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r'http(s)?://www\.ut\.ee/~([^/]+)/', line)
            if match:
                usernames.append(match.group(2))

    return usernames


usernames = extract_usernames('addresses.txt')
for username in usernames:
    print(username)
