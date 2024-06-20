import sys, os, math

def circle_dots_foo(path_circle,path_dots):
    with open(path_circle,'r') as f:
        nums = f.readlines()
        x1,y1 = map(float,(nums[0]).split())
        R = float(nums[1])

    with open(path_dots,'r') as f:

        lines = f.readlines()
        count_lines = len(lines)
        if count_lines < 1:
            print("Добавьте координаты точки в файле")
            sys.exit(1)
        elif count_lines > 100:
            print("Максимальное количество точек 100")
            sys.exit(1)
        else:
            for line in lines:
                x2,y2 = map(float,line.split())
                D = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                if D == R:
                    print(0)
                elif D < R:
                    print(1)
                else:
                    print(2)

def main():
    if len(sys.argv) != 3:
        print("Использование: python3 task2.py <path1> <path2>")
        sys.exit(1)

    path_circle = sys.argv[1]
    path_dots = sys.argv[2]

    if not os.path.exists(path_circle):
        print(f"Файл '{path_circle}' не существует.")
        sys.exit(1)

    if not os.path.exists(path_dots):
        print(f"Файл '{path_dots}' не существует.")
        sys.exit(1)

    circle_dots_foo(path_circle,path_dots)
if __name__ == "__main__":
    main()