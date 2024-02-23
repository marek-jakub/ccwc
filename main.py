import sys
from sys import argv
import process

process = process.Command()


if __name__ == '__main__':

    try:
        # Check if input is not from terminal (TTY), i.e. being piped in or redirected
        if not sys.stdin.isatty():
            # Read input data into a buffer
            textObject = sys.stdin.buffer
            process.process_command(textObject, argv)
        else:
            process.process_command('noPipe', argv)
    except FileNotFoundError:
        print('File not found')
    except (ValueError, TypeError):
        print('Too many arguments')
    except KeyError:
        print('Command not recognized')
