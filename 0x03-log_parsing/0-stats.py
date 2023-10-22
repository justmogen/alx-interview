#!/usr/bin/python3
"""
This module contains a method that reads stdin line by line and
compute the total size of files
"""
import sys


def display_metrics(total_size, status_code):
    """
    prints the required metrics described
    """

    print('File size: {}'.format(total_size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


if __name__ == '__main__':
    total_size = 0
    status_code = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
    }

    try:
        i = 0
        for line in sys.stdin:
            argms = line.split()
            if len(argms) > 6:
                status = argms[-2]
                file_size = argms[-1]
                total_size += int(file_size)
                if status in status_code:
                    i += 1
                    status_code[status] += 1
                    if i % 10 == 0:
                        display_metrics(total_size, status_code)

    except KeyboardInterrupt:
        display_metrics(total_size, status_code)
        raise
    else:
        display_metrics(total_size, status_code)
