import sys
import os
from pprint import pprint


def main(extension, search):
    cwd = os.getcwd()
    results = []
    exclude=['PyKivy']
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


def search_file(filename, search):
    with open(filename, 'r') as file:
        for contents in file:
            if search in contents:
                return {'file': filename, 'result': contents.strip()}

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sys.exit(main(sys.argv[1], sys.argv[2]))
    else:
        print('Missing arguments. Need extension and search string.')
        print("Example: pygrep .py 'This is a search string'")
    sys.exit()
