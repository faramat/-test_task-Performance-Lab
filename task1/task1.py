import sys

def circ_foo(n,m):
    circ_array = list(range(1,n+1))
    path = []
    index = 0
    while circ_array[index] not in path:
        path.append(circ_array[index])
        index = (index + m - 1) % n
    return path

def main():
    if len(sys.argv) != 3:
        print("Использование: python task1.py <arg1> <arg2>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Аргументы должны быть числами")
        sys.exit(1)

    if n <= 0 or m <=0:
        print("Числа должны быть положительными")
        sys.exit(1)

    paths = circ_foo(n,m)
    print("".join(map(str,paths)))
    
if __name__ == "__main__":
    main()
