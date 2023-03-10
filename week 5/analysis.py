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
        elif char == ">":
            result += char + "\n"
            inside_tag = False
        elif inside_tag:
            result += char
else:
    result = ""
    inside_tag = False
    for char in content:
        if char == "<":
            inside_tag = True
        elif char == ">":
            inside_tag = False
        elif not inside_tag:
            result += char
    result = result.split("\n")
    result = "\n".join(line.strip() for line in result if line.strip())

output_file = f"analysis-{analysis_type}.txt"
with open(output_file, "w") as f:
    f.write(result)

print("Saved!")
