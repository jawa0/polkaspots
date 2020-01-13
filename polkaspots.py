import argparse
import cairocffi
import sys


def main():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('-s', '--side', required=True)
	arg_parser.add_argument('-r', '--radius', required=True)
	arg_parser.add_argument('-c', '--count', required=True)
	args = arg_parser.parse_args(sys.argv[1:])

	SIDE_PX = int(args.side)
	RADIUS_PX = int(args.radius)
	NUM_DOTS = int(args.count)


if __name__=='__main__':
	main()
