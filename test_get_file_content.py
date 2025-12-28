from functions.get_file_content import get_file_content

test_case_1 = [
    ("calculator", "lorem.txt"),
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py")
]

def test_get_file_content(cases): 
    for case in cases: 
        total_contents = get_file_content(case[0], case[1])
        if len(total_contents.split('...')) > 1: 
            trunc_msg = total_contents.split('...')[1]
            contents = total_contents.split('...')[0]
            print(len(contents))
            print(trunc_msg)
        else: 
            print(total_contents)


if __name__ == "__main__":
    test_get_file_content(test_case_1)
