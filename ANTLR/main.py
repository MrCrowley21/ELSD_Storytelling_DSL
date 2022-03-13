from DSL_grammarParser import DSL_grammarParser
import sys


def main(argv):
    parser = DSL_grammarParser
    parser.parse(argv)


if __name__ == '__main__':
    main(sys.argv)
