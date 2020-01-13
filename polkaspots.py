import argparse
import cairocffi as cr
from math import pi
import random
import sys


def main():
	# python polkaspots.py --side 128 --radius 10 --dots 5 --images 100
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('-s', '--side', required=True)
	arg_parser.add_argument('-r', '--radius', required=True)
	arg_parser.add_argument('-d', '--dots', required=True)
	arg_parser.add_argument('-i', '--images', required=True)
	args = arg_parser.parse_args(sys.argv[1:])

	SIDE_PX = int(args.side)
	RADIUS_PX = int(args.radius)
	NUM_DOTS = int(args.dots)
	NUM_IMAGES = int(args.images)

	filename_prefix = 'dots_%03d_' % (NUM_DOTS,)
	for i in range(NUM_IMAGES):
		surf = cr.ImageSurface(cr.FORMAT_RGB24, SIDE_PX, SIDE_PX)
		ctx = cr.Context(surf)

		ctx.set_source_rgb(1,1,1)
		ctx.rectangle(0, 0, SIDE_PX, SIDE_PX)
		ctx.fill()
		
		ctx.set_source_rgb(0,0,0)
		for d in range(NUM_DOTS):
			cx = random.uniform(RADIUS_PX, SIDE_PX - RADIUS_PX - 1)
			cy = random.uniform(RADIUS_PX, SIDE_PX - RADIUS_PX - 1)

			ctx.new_sub_path()
			ctx.arc(cx, cy, RADIUS_PX, 0, 2 * pi)
			ctx.fill()


		surf.write_to_png(filename_prefix + '%05d.png' % (i,))


if __name__=='__main__':
	main()
