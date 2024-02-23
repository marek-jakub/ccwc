import ccwc

ccwc = ccwc.CCWC()


def _unpack_args(piped, *args):
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
    ccwc.process_file(piped, arg, file)


commands = {
    "ccwc": _call_ccwc,
    # Process any other commands
    # "": ""
}


class Command:

    @staticmethod
    def process_command(piped_object, *args):
        if piped_object == 'noPipe':
            command, argument, file = _unpack_args(False, *args)
            commands[command](False, argument, file)
        else:
            command, argument, file = _unpack_args(True, *args)
            commands[command](True, argument, piped_object)
