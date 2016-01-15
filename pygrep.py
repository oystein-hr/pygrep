#!/usr/bin/env python
import sys
import os
from subprocess import call


def main(extension, search):
    print(search)
    cwd = os.getcwd()
    results = []
    exclude = ['PyKivy']
    for root, dirs, files in os.walk(cwd, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        files[:] = [f for f in files if f.endswith(extension)]

        for file in files:
            full_path = os.path.join(root, file)
            file_search = search_file(full_path, search)
            if file_search is not None:
                results.append(file_search)

    for index, item in enumerate(results):
        print('[{}]{} : {}'.format(index, item['file'], item['result']))

    while True:
        choice = input('Choose file to be opened (number, "n" to cancel): ')
        if choice.isdigit():
            choice = int(choice)
        elif choice == 'n':
            sys.exit()
        else:
            continue
        if choice <= len(results) - 1:
            break

    print('Opening [{}]: {}'.format(choice, results[choice]['file']))
    call(["/usr/local/bin/charm", results[choice]['file']])


def search_file(filename, search):
    with open(filename, 'r') as file:
        for contents in file:
            if search in contents:
                return {'file': filename, 'result': contents.strip()}

if __name__ == '__main__':
    if len(sys.argv) > 2:
        sys.exit(main(sys.argv[1], sys.argv[2]))
    else:
        print('Usage:')
        print("  pygrep .py 'This is a search string'")
    sys.exit()
