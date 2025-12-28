from functions.get_files_info import get_files_info


test_cases = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../")
]
def test_get_files_info(test_cases):
    for case in test_cases: 
        file_list = get_files_info(case[0], case[1]).split("\n")
        print(f'Result for {case[1]} directory:')
        for item in file_list: 
            print(item)

if __name__ == "__main__":
    test_get_files_info(test_cases)