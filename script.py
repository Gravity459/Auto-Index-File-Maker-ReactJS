from os import path, listdir
from re import sub

# convert file name to camel case in case of image files
def convertToCamelCase(st):
    st = st[:-4]
    st = sub(r"(_|-)+", " ", st).title().replace(" ", "")
    return ''.join([st[0].lower(), st[1:]])


# create index.js file for assets folder
def createIndexFileForAssets():

    # uncomment the below line to take input from the user
    # user_input = input("Enter the directory: ")

    file_directory = "./src/assets"
    f = open(f"{file_directory}/index.js", "w")

    final_list = []

    # check if the directory exists
    if path.isdir(file_directory):
        files_list = listdir(file_directory)

        for file in files_list:
            if file == "index.js":
                continue
            camelCased = convertToCamelCase(file)
            final_list.append(camelCased)
            # print(f"import {camelCased} from '{file_directory}/{file}';\n")
            f.write(f"import {camelCased} from '{file_directory}/{file}';\n")

        export_string = "export { " + ", ".join(final_list) + " }"
        f.write(f"\n{export_string}")


# create index.js file for components folder
def createIndexFileForComponents():

    # uncomment the below line to take input from the user
    # user_input = input("Enter the directory: ")

    file_directory = "./src/components"
    f = open(f"{file_directory}/index.js", "w")

    final_list = []

    # check if the file exists
    if path.isdir(file_directory):
        files_list = listdir(file_directory)

        for file in files_list:
            if file == "index.js":
                continue

            final_list.append(file)
            # print(f"import {file} from './{file}/{file}';\n")
            f.write(f"import {file} from './{file}/{file}';\n")

        export_string = "export { " + ", ".join(final_list) + " }"
        f.write(f"\n{export_string}")


if __name__ == "__main__":

    createIndexFileForAssets()
    createIndexFileForComponents()
    print("Done!")