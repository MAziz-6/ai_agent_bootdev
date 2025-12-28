from functions.get_files_info import get_files_info

def print_section(header, result_string):
    print(header)
    indented_result = "\n".join("  " + line for line in result_string.split("\n"))
    print(indented_result)


def main():
    print_section(
        "Result for current directory:",
        get_files_info("calculator", ".")
    )
    print_section(
        "Result for 'pkg' directory:",
        get_files_info("calculator", "pkg")
    )
    print_section(
        "Result for '/bin' directory:",
        get_files_info("calculator", "/bin")
    )
    print_section(
        "Result for '../' directory:",
        get_files_info("calculator", "../")
    )



if __name__ == "__main__":
    main()