import os

directory = input("Enter directory path: ")

if not os.path.isdir(directory):
    print("Invalid directory.")
    exit()

files = os.listdir(directory)

categories = {}   # extension → list of files

for f in files:
    if os.path.isfile(os.path.join(directory, f)):
        parts = f.split(".")
        if len(parts) > 1:
            ext = parts[-1].lower()
        else:
            ext = "no_extension"

        categories.setdefault(ext, []).append(f)

# Display the result
for ext, file_list in categories.items():
    print(f"\nExtension: {ext}")
    for name in file_list:
        print("   ", name)
