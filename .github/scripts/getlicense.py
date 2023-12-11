#!/usr/bin/env python3
import os
import re
import sys


def main(arguments):
    if len(arguments) != 3:
        print('Wrong number of arguments, was {} should be 3'.format(len(arguments)))
        return 1

    if not os.path.exists(arguments[0]) and os.path.isfile(arguments[0]):
        print('First argument "{}" is not a file'.format(arguments[0]))
        return 1

    startpattern = None
    try:
        startpattern = re.compile(arguments[1])
    except Exception:
        print('Second argument "{}" is not a valid pattern'.format(arguments[1]))
        return 1

    endpattern = None
    try:
        endpattern = re.compile(arguments[2])
    except Exception:
        print('Third argument "{}" is not a valid pattern'.format(arguments[2]))
        return 1

    with open(arguments[0]) as inputfile:
        startfound = False
        for line in inputfile:
            if not startfound:
                if startpattern.search(line) is not None:
                    startfound = True
                    continue
            elif endpattern.search(line) is not None:
                break
            else:
                print(line[:-1])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
