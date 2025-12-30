from functions.run_python_file import run_python_file

def test_run_python_file():
    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py"),
        ("calculator", "lorem.txt")
    ]

    for case in test_cases: 
        if len(case) == 2: 
            result = run_python_file(case[0], case[1])
            print(result)
        else:
            result = run_python_file(case[0], case[1], case[2])
            print(result)

if __name__ == "__main__":
    test_run_python_file()