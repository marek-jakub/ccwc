import ccwc

ccwc = ccwc.Ccwc()


def _unpack_args(piped, *args):
    """
    Unpacks command line arguments.
    :param: piped (bool): Indicates whether the command is piped.
    :param: *args: Variable-length argument list.
    :return: tuple: A tuple containing command, argument, and file.
        """
    if len(args[0]) == 2:
        _, command, argument, file = args[0] + ["", None]
    elif len(args[0]) == 3 and not piped:
        _, command, file, argument = args[0] + [""]
    elif len(args[0]) == 3 and piped:
        _, command, argument, file = args[0] + [""]
    else:
        _, command, argument, file = args[0]
    return command, argument, file


def _call_ccwc(piped, arg, file):
    """
    Calls method to process file or an object.
    :param: piped (bool): Indicates whether the command is piped.
    :param: arg (str): Command argument.
    :param: file (str): File name.
    :return: None
    """
    ccwc.process_file(piped, arg, file)


# The dictionary maps command(s) to corresponding functions.
commands = {
    "ccwc": _call_ccwc,
    # Process any other commands
    # "": ""
}


class Command:
    """
    The class represents a command and argument handler.
    """

    @staticmethod
    def process_command(piped_object, *args):
        """
        Unpack arguments and call a command based on input.
        :param: piped_object (str): Indicates whether the command is piped.
        :param: *args: Variable-length argument list.
        :return: None
        """
        if piped_object == 'noPipe':
            command, argument, file = _unpack_args(False, *args)
            commands[command](False, argument, file)
        else:
            command, argument, file = _unpack_args(True, *args)
            commands[command](True, argument, piped_object)
