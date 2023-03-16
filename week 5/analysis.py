filename = input("Enter filename: ")
analysis_type = input("Extract tags or text: ")

with open(filename, "r") as f:
    content = f.read()

if analysis_type == "tags":
    result = ""
    inside_tag = False
    for char in content:
        if char == "<":
            inside_tag = True
            result += char
        elif char == ">":
            inside_tag = False
            result += char + "\n"
        elif inside_tag:
            result += char
else:
    result = ""
    inside_tag = False
    current_text = ""
    for char in content:
        if char == "<":
            inside_tag = True
            if current_text.strip():
                result += current_text.strip() + "\n"
                current_text = ""
        elif char == ">":
            inside_tag = False
        elif not inside_tag:
            current_text += char
    if current_text.strip():
        result += current_text.strip() + "\n"

output_file = input("Enter output file name: ")
with open(output_file, "w") as f:
    f.write(result)

print("Saved!")
