import os


def find_file(filename, search_path):
    file_locations = []
    for dirpath, dirnames, filenames in os.walk(search_path):
        if filename in filenames:
            file_location = os.path.join(dirpath, filename)
            file_locations.append(file_location)
    return file_locations

def add_license(license_file, file_locations):
    licnese_text = open(license_file, "r").read()
    for file_to_edit in file_locations:
        file_ref = open(file_to_edit, "r")
        file_text = file_ref.read()
        file_ref.close()
        file_text = licnese_text + "\n" + file_text
        file_write_ref = open(file_to_edit, "w")
        file_write_ref.write(file_text)
        file_write_ref.close()


if __name__ == "__main__":

    file_to_add_license_to = "README.md"
    license_file = "license.txt"
    path = "test"

    file_locations = find_file(file_to_add_license_to, path)
    add_license(license_file, file_locations)
