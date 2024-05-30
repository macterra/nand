import sys

def next():
    bit = sys.stdin.read(1)

    if bit == '0':
        return 0

    if bit == '1':
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
