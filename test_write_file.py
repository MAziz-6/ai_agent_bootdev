from functions.write_file import write_file

def print_section(header, result_string):
    print(header)
    print(result_string)

def main():
    print_section(
        "Result for writing to lorem.txt:",
        write_file("calculator", "lorem.txt", "wait, this isn't lorem ipusm")
    )
    print_section(
        "Result for writing to pkg/morelorem.txt:",
        write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    )
    print_section(
        "Result for writing to /tmp/temp.txt:",
        write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    )

if __name__ == "__main__":
    main()