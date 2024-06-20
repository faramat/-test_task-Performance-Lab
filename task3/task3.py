import sys,os

def check_file_exists(file_path):
    if not os.path.exists(file_path):
        print(f"Файл '{file_path}' не существует.")
        return False
    return True

def create_report(path_values,path_tests,path_report):
    pass

def main():
    if len(sys.argv) != 4:
        print("Использование: python3 task3.py <path1> <path2> <path3>")
        sys.exit(1)

    path_values = sys.argv[1]
    path_tests = sys.argv[2]
    path_report = sys.argv[3]

    files = [path_values, path_tests, path_report]

    for file_path in files:
        if not check_file_exists(file_path):
            sys.exit(1)

    create_report(path_values,path_tests,path_report)


if __name__ == "__main__":
    main()