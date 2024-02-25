import os


def _read_file(file):
    """
    The function reads the content of a file and returns it as a list of strings.
    :param file: The path to the file to be read.
    :return: A list of strings representing the lines of the file.
    :rtype: list[str]
    """
    with open(file, "rb") as current_file:
        return current_file.readlines()


def _measure_content(content):
    """
    The function measures various properties of the input content.
    :param content: A list of strings representing the content.
    :return: A tuple containing the following properties:
        - file_size: Total size of the content in bytes.
        - line_count: Number of lines in the content.
        - word_count: Total number of words in the content.
        - char_count: Total number of characters in the content.
    :rtype: tuple
    """
    file_size, line_count, word_count, char_count = 0, 0, 0, 0
    for line in content:
        file_size += len(line)
        line_count += line.count(10)
        word_count += len(line.split())
        char_count += len(line.decode())
    return file_size, line_count, word_count, char_count


def _print_all(*args):
    """
    The function prints the elements in the input list followed by a separator.
    :param args: A list of elements to be printed.
    :return: None
    """
    print(' '.join(str(x) for x in args[0]), args[1])


def _print_bytes(*args):
    """
    The function prints the first element of the first list element in args,
    followed by the second element.
    :param args: A list of elements to be printed.
    :return: None
    """
    print(args[0][0], args[1])


def _print_lines(*args):
    """
    The function prints the second element of the first list element in args,
    followed by the second element.
    :param args: A list of elements to be printed.
    :return: None
    """
    print(args[0][1], args[1])


def _print_words(*args):
    """
    The function prints the third element of the first list element in args,
    followed by the second element.
    :param args: A list of elements to be printed.
    :return: None
    """
    print(args[0][2], args[1])


def _print_chars(*args):
    """
    The function prints the fourth element of the first list element in args,
    followed by the second element.
    :param args: A list of elements to be printed.
    :return: None
    """
    print(args[0][3], args[1])


# The dictionary maps command-line arguments to corresponding functions.
arg_output = {
    "": _print_all,
    "-c": _print_bytes,
    "-l": _print_lines,
    "-w": _print_words,
    "-m": _print_chars,
}


class Ccwc:
    """
    The class provides functionality for processing files based on command-line arguments.
    """

    @staticmethod
    def process_file(piped, arg, entry):
        """
        Process the file content based on command-line arguments.
        :param piped: A boolean indicating whether the input is piped.
        :param arg: The command-line argument.
        :param entry: The file path or content.
        :return: None
        """
        if piped:
            result = _measure_content(entry)
            arg_output[arg](result, '')
        else:
            content = _read_file(entry)
            result = _measure_content(content)
            arg_output[arg](result, entry)
