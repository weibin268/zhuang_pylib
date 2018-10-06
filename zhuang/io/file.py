def read_text(path):
    file = open(path, "r")
    return file.readlines()


if __name__ == "__main__":
    content = read_text("file.py")
    print(content)
