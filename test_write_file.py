from functions.write_file import write_file



def test_write_file(): 
    test_case = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed")
    ]

    for case in test_case: 
        result = write_file(case[0], case[1], case[2])
        print(result)


if __name__ == "__main__":
    test_write_file()
