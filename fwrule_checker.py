#!/usr/bin/python

import os.path
import argparse


class Rule:
	def __init__(self, target, protocol_range, options, source_range, destination_range, ctstate):
		self.target = target
		self.protocol = protocol_range
		self.options = options
		self.source_range = source_range
		self.destination_range = destination_range
		self.ctstate = ctstate

def parse_rule(rule):
	rule_contents = rule.read().split()
	print rule_contents


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle

#TODO: change Argument Parser Description
def main():
	parser = argparse.ArgumentParser(description='Final Project for NSF')
	parser.add_argument('rule_file', help='Firewall Rule in a *.txt file')
	parser.add_argument('chain_file', help='Firewall chain in a *.txt file')
	args = parser.parse_args()

	rule = is_valid_file(parser, args.rule_file)
	parse_rule(rule)



if __name__ == "__main__":
	main()
