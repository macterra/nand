import sys

def next():
    # Read one character from stdin
    char = sys.stdin.read(1)

    if not char:
        print()
        exit(0);

    if char == '0':
        return 0

    if char == '1':
        return 1

    print()
    exit(0)

def nand():
    a = nand() if next() else next()
    b = nand() if next() else next()
    return 1 if not (a and b) else 0

def interpret():
    while True:
        n = next()

        if n == 0:
            print(next(), end="")
        elif n == 1:
            print(nand(), end="")

if __name__ == "__main__":
    interpret()
