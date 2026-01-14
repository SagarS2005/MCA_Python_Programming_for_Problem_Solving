def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        print(content)

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    finally:
        print("File read attempt completed.")

read_file("file.txt")