from functions.get_file_content import get_file_content
from config import MAX_CHARS

def print_section(header, result_string):
    print(header)

    if result_string.startswith("Error:"):
        print(result_string)
        return

    if len(result_string) > MAX_CHARS:
        print(f"Content Length: {len(result_string)} characters (truncated)")
        print(f"Truncation Message: {result_string[MAX_CHARS:]}")
    else:
        print(result_string)

def main():
    print_section(
        "Result for 'lorem.txt' file:",
        get_file_content("calculator", "lorem.txt")
    )
    print_section(
        "Result for 'main.py' file:",
        get_file_content("calculator", "main.py")
    )
    print_section(
        "Result for 'pkg/calculator.py' file:",
        get_file_content("calculator", "pkg/calculator.py")
    )
    print_section(
        "Result for '/bin/cat' file:",
        get_file_content("calculator", "/bin/cat")
    )
    print_section(
        "Result for 'pkg/does_not_exist.py' file:",
        get_file_content("calculator", "pkg/does_not_exist.py")
    )

if __name__ == "__main__":
    main()