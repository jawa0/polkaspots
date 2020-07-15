"""Generate images of randomly-placed disks of a given radius. If the position
   of a new disk would cause it to overlap by more than one radius with
   existing disks, then a new position is generated. This repeats until the
   generated position is acceptable, or until a max number of tries is hit."""

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
    arg_parser.add_argument('-d', '--dots', required=True)
    args = arg_parser.parse_args(sys.argv[1:])

    side_px = int(args.side)

    radius_px = int(args.radius)
    max_overlap_squared = (1 * radius_px)**2

    nb_dots = int(args.dots)
    nb_images = int(args.images)

    img_prefix = f'dots_radius_{radius_px}_count_{nb_dots:02d}'
    pos_prefix = f'positions_radius_{radius_px}_count_{nb_dots:02d}'

    for i in range(nb_images):
        surf = cr.ImageSurface(cr.FORMAT_RGB24, side_px, side_px)
        ctx = cr.Context(surf)

        ctx.set_source_rgb(1, 1, 1)
        ctx.rectangle(0, 0, side_px, side_px)
        ctx.fill()

        ctx.set_source_rgb(0, 0, 0)
        generated_dots = []
        for _ in range(nb_dots):
            sanity_max_tries = 500
            nb_tries = 0
            good_position = False
            while not good_position and nb_tries < sanity_max_tries:
                centre_x = random.uniform(radius_px, side_px - radius_px - 1)
                centre_y = random.uniform(radius_px, side_px - radius_px - 1)

                all_good = True
                for dot in generated_dots:
                    dist_sq = dist_squared(centre_x, centre_y, dot[0], dot[1])
                    if dist_sq < max_overlap_squared:
                        all_good = False    # too close
                        break
                good_position = all_good
                nb_tries += 1

            if not good_position:
                print("Error: could not place disk without excessive overlap.")
                print(f"Tried {nb_tries} times. Exiting.")
                sys.exit(1)
            else:
                generated_dots.append((centre_x, centre_y))

            ctx.new_sub_path()
            ctx.arc(centre_x, centre_y, radius_px, 0, 2 * pi)
            ctx.fill()

        # Save image out.
        surf.write_to_png(f'{img_prefix}_{i:05d}.png')

        # Also save out generated dot centres.
        with open(f'{pos_prefix}_{i:05d}.csv', 'wt') as pos_out:
            for dot in generated_dots:
                pos_out.write(f'{dot[0]}, {dot[1]}\n')


def dist_squared(x_0, y_0, x_1, y_1):
    """Compute the squared distance between the two points (x_0, y_0) and
       (x_1, y_1)."""

    return (x_0 - x_1)**2 + (y_0 - y_1)**2


if __name__ == '__main__':
    main()
