"""Generate images of randomly-placed disks of a given radius."""

import argparse
from math import pi
import random
import sys
import cairocffi as cr


def main():
    """Main routine that runs when executed as a script. Example command-line
        usage: python polkaspots.py --side 128 --radius 10 --dots 5 --images 100
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-s', '--side', required=True)
    arg_parser.add_argument('-r', '--radius', required=True)
    arg_parser.add_argument('-i', '--images', required=True)
    args = arg_parser.parse_args(sys.argv[1:])

    side_px = int(args.side)
    radius_px = float(args.radius)
    nb_dots = int(args.dots)
    nb_images = int(args.images)

    filename_prefix = 'dots_%03d_' % (nb_dots, )
    for i in range(nb_images):
        surf = cr.ImageSurface(cr.FORMAT_RGB24, side_px, side_px)
        ctx = cr.Context(surf)

        ctx.set_source_rgb(1, 1, 1)
        ctx.rectangle(0, 0, side_px, side_px)
        ctx.fill()

        ctx.set_source_rgb(0, 0, 0)
        for _ in range(nb_dots):
            centre_x = random.uniform(radius_px, side_px - radius_px - 1)
            centre_y = random.uniform(radius_px, side_px - radius_px - 1)

            ctx.new_sub_path()
            ctx.arc(centre_x, centre_y, radius_px, 0, 2 * pi)
            ctx.fill()


        surf.write_to_png(filename_prefix + '%05d.png' % (i, ))


if __name__ == '__main__':
    main()
