import sys

def next_bit():
    bit = sys.stdin.read(1)
    if bit == '0':
        return 0
    if bit == '1':
        return 1
    raise EOFError

def nand():
    a = nand() if next_bit() else next_bit()
    b = nand() if next_bit() else next_bit()
    return 1 if not (a and b) else 0

def interpret():
    try:
        while True:
            n = next_bit()
            if n == 0:
                print(next_bit(), end="")
            elif n == 1:
                print(nand(), end="")
    except EOFError:
        print()

if __name__ == "__main__":
    interpret()
