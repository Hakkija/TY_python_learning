def is_balanced(s):
    stack = []

    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != matching_brackets[char]:
                return False

    return not stack

def main():
    while True:
        s = input("Enter string: ")
        if is_balanced(s):
            print("Brackets are balanced")
        else:
            print("Brackets are not balanced")

main()
