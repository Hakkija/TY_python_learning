def read_names(filename):
    names = {}
    with open(filename, 'r') as file:
        for line in file:
            id_code, name = line.strip().split(' ', 1)
            names[id_code] = name
    return names

def children_with_parents(names_file, children_file):
    names = read_names(names_file)
    children_parents = {}

    with open(children_file, 'r') as file:
        for line in file:
            parent_id, child_id = line.strip().split(' ')
            parent_name = names[parent_id]
            child_name = names[child_id]

            if child_name not in children_parents:
                children_parents[child_name] = set()

            children_parents[child_name].add(parent_name)

    return children_parents

names_filename = "names.txt"
children_filename = "children.txt"

children_parents = children_with_parents(names_filename, children_filename)

for child, parents in children_parents.items():
    parents_string = ', '.join(parents)
    print(f"{child}: {parents_string}")
