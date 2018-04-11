import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--input', dest='input', action='store_const', help='takes name of input file')

args = parser.parse_args()

print args.input