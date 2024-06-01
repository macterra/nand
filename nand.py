import sys
from collections import deque

bits = deque(sys.stdin.read().strip())

def next_bit():
    global bits
    bit = bits.popleft()
    if bit == '0':
        return 0
    if bit == '1':
        return 1
    raise IndexError

def nand():
    return 1 if not (cond() and cond()) else 0

def cond():
    return nand() if next_bit() else next_bit()

def interpret():
    global bits
    try:
        while True:
            bit = str(cond())
            print(bit, end="")
            bits.append(bit)
    except IndexError:
        print()

if __name__ == "__main__":
    interpret()
