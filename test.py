from pathlib import Path


def removess(filename):
    text = ""
    with open(f"{filename}", "r") as file:
        for line in file.readlines():
            if not (line.__contains__("setStyleSheet")):
                text += line

    with open(f"{filename}", "w") as file:
        file.write(text)


if __name__ == "__main__":
    path = Path("converts")
    for f in path.iterdir():
        if f.is_file() and f.suffix == ".py":
            removess(f"converts/{f.name}")
