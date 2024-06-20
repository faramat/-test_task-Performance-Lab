import sys, os, math

def check_file_exists(file_path):
    if not os.path.exists(file_path):
        print(f"Файл '{file_path}' не существует.")
        return False
    return True

def read_numbers(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]
    
def find_min(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

def main():
    if len(sys.argv) != 2:
        print("Использование: python3 task4.py <path1>")
        sys.exit(1)

    path_file = sys.argv[1]

    if not check_file_exists(path_file):
        sys.exit(1)
            
    nums = read_numbers(path_file)
    print(find_min(nums))
if __name__ == "__main__":
    main()