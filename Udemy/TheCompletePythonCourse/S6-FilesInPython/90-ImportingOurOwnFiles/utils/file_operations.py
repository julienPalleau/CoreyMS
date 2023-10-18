def save_to_file(content, filename):
    with open(filename, 'w') as f:
        f.write(content)


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()  # 'Rolf\nCharlie\nAnna\nJen'.split('\n') ['Rolf', 'Charlie', 'Anna', 'Jen']
