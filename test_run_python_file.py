from functions.run_python_file import run_python_file

def print_section(header, result_string):
    print(header)
    print(result_string)

def main():
    print_section(
        "Result for running 'main.py':",
        run_python_file("calculator", "main.py")
    )
    print_section(
        "Result for running 'main.py' with arguments ['3 + 5']:",
        run_python_file("calculator", "main.py", ["3 + 5"])
    )
    print_section(
        "Result for running 'tests.py:",
        run_python_file("calculator", "tests.py")
    )
    print_section(
        "Result for running '../main.py':",
        run_python_file("calculator", "../main.py")
    )
    print_section(
        "Result for running 'nonexistent.py':",
        run_python_file("calculator", "nonexistent.py")
    )
    print_section(
        "Result for running 'lorem.txt':",
        run_python_file("calculator", "lorem.txt")
    )

if __name__ == "__main__":
    main()