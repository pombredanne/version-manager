import argparse

from src.file import loaded_files
from colorama import Fore, Back, Style


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--status', action='store_true', help='To see current status of versioning files')
    parser.add_argument('--set', help='To set specific version into version files. (--set 3.5.1)')
    parser.add_argument('--bump', choices=['major', 'minor', 'patch'], help='To bump version defined as SemVer. Choices are ["major", "minor", "patch"] (--bump major)')

    args = parser.parse_args()
    if args.status:
        status()
    elif args.set:
        set(args.set)
    elif args.bump:
        bump(args.bump)


def status():
    for file in loaded_files:
        print("%sFile %s version is %s\n" % (file.color, file.path, file.current_version))


def set(version):
    for file in loaded_files:
        file.update_version(version)


def bump(level):
    for file in loaded_files:
        file.bump_version(level)


if __name__ == '__main__':  # pragma: no cover
    main()
