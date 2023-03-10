filename = input("Enter filename: ")
analysis_type = input("Extract tags or text: ")
if analysis_type == "tags":
    output_filename = "analysis-tags.txt"
elif analysis_type == "text":
    output_filename = "analysis-text.txt"
else:
    print("Invalid analysis type!")
    exit()

with open(filename, "r") as file, open(output_filename, "w") as output_file:
    for line in file:
        if analysis_type == "tags":
            for word in line.split():
                if word.startswith("<"):
                    output_file.write(word + "\n")
        elif analysis_type == "text":
            for word in line.split():
                if not word.startswith("<"):
                    output_file.write(word + "\n")
print("Saved!")
