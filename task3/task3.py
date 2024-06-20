import sys,os,json

def check_file_exists(file_path):
    if not os.path.exists(file_path):
        if "report.json" in file_path:
            return True
        print(f"Файл '{file_path}' не существует.")
        return False
    return True

def load_json(file_path):
    with open(file_path,'r') as f:
        return json.load(f)
    
def find_value(test_id, values):
    for value in values:
        if value['id'] == test_id:
            return value['value']
    return None

def fill_values(tests, values):
    for test in tests:
        test_id = test['id']
        value = find_value(test_id,values)
        if value is not None:
            test['value'] = value
        if 'values' in test:
            fill_values(test['values'], values)

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
def create_report(path_values,path_tests,path_report):
    tests_data = load_json(path_tests)
    values_data = (load_json(path_values))["values"]
    fill_values(tests_data['tests'],values_data)
    save_json(path_report, tests_data)

def main():
    if len(sys.argv) != 4:
        print("Использование: python3 task3.py <path values.json> <path tests.json> <path report.json>")
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