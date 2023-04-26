def dictionary_from_file(filename):
    country_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            code, name = line.strip().split()
            country_dict[code] = name
    return country_dict


def codes_to_names(filename, country_codes):
    country_names = []
    with open(filename, 'r') as file:
        for line in file:
            code = line.strip()
            if code in country_codes:
                country_names.append(country_codes[code])
            else:
                country_names.append('Unknown')
    return country_names


def main():
    country_file = input("Enter country file name: ")
    crossings_file = input("Enter border crossings file name: ")

    country_codes = dictionary_from_file(country_file)
    country_names = codes_to_names(crossings_file, country_codes)

    for name in country_names:
        print(name)


main()
