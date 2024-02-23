import os


def _read_file(file):
    """Helper method used to read files.

    Returns file as string if found, else an error message.
    """
    with open(file, "rb") as current_file:
        return current_file.readlines()


def _measure_content(content):
    file_size, line_count, word_count, char_count = 0, 0, 0, 0
    for line in content:
        file_size += len(line)
        line_count += line.count(10)
        word_count += len(line.split())
        char_count += len(line.decode())
    return file_size, line_count, word_count, char_count


def _print_all(*args):
    print(' '.join(str(x) for x in args[0]), args[1])


def _print_bytes(*args):
    print(args[0][0], args[1])


def _print_lines(*args):
    print(args[0][1], args[1])


def _print_words(*args):
    print(args[0][2], args[1])


def _print_chars(*args):
    print(args[0][3], args[1])


arg_output = {
    "": _print_all,
    "-c": _print_bytes,
    "-l": _print_lines,
    "-w": _print_words,
    "-m": _print_chars,
}


class CCWC:

    @staticmethod
    def process_file(piped, arg, entry):
        if piped:
            result = _measure_content(entry)
            arg_output[arg](result, '')
        else:
            content = _read_file(entry)
            result = _measure_content(content)
            arg_output[arg](result, entry)
