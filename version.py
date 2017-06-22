import os
import subprocess
import sys

version_file = "version.txt"
full_version = "0.0.0"
major = 0
minor = 0
patch = 0

hash = str(subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip())


def main():
    global java_file, gradle_file, xml_file, full_version, major, minor, patch, hash

    if os.path.isfile(version_file):
        with open(version_file, 'r') as f:
            full_version = f.readline().strip()

        version_array = full_version.split('.')

        major = int(version_array[0])
        minor = int(version_array[1])
        patch = int(version_array[2])
    else:
        with open(version_file, 'w+') as f:
            f.write(full_version)

    new_version = full_version

    if len(sys.argv) == 2:
        user_input = int(sys.argv[1])
    else:
        print("Current version is:", full_version)
        print ("Enter 1 to change major version to:", str(major + 1) + ".0.0." + hash)
        print ("Enter 2 to change minor version to:", str(major) + "." + str(minor + 1) + ".0." + hash)
        print ("Enter 3 to change patch version to:", str(major) + "." + str(minor) + "." + str(patch + 1) + "." + hash)

        print("Enter your selection:")
        user_input = int(sys.stdin.readline())

    if 1 > user_input or user_input > 3:
        print("Your selection", user_input, "is invalid!")
        sys.exit(1)

    if user_input == 1:
        new_version = str(major + 1) + ".0.0." + hash
    elif user_input == 2:
        new_version = str(major) + "." + str(minor + 1) + ".0." + hash
    elif user_input == 3:
        new_version = str(major) + "." + str(minor) + "." + str(patch + 1) + "." + hash

    print("Updating version", full_version, "to", new_version)

    update_file_version(version_file, full_version, new_version)


def update_file_version(relative_file, old, new):
    full_file = os.path.join(os.path.dirname(__file__), relative_file)

    modified = []
    with open(full_file) as f:
        original = f.readlines()

    for x in original:
        modified.append(x.replace(old, new))

    write_file(full_file, modified)


def write_file(full_file, file_data):
    # Write the file out again
    with open(full_file, 'w') as file:
        file.writelines(file_data)


main()
