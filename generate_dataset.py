"""Generate dataset of images containing dots, using polkaspots.py, across a 
   range of dot radii and dot counts."""

import os
import subprocess
import sys

if __name__ == '__main__':
    # python polkaspots.py --side 256 --radius 2 --dots 10 --images 100
    NB_IMAGES = 100
    IMAGE_SIDE = 256
    radii = range(2, 40+1)
    dot_counts = range(1, 10+1)

    ARG_IMAGE_SIDE = str(IMAGE_SIDE)
    ARG_NB_IMAGES = str(NB_IMAGES)

    ROOT_DIR = os.path.abspath('.')
    IMG_DIR = os.path.abspath('./img')

    for radius in radii:
        print('radius', radius)
        ARG_RADIUS = str(radius)
        for nb_dots in dot_counts:
            print('nb_dots', nb_dots)
            path = f'{IMG_DIR}/radius{radius:02d}/{nb_dots:02d}'
            os.makedirs(path)

            subprocess.call(['python', f'{ROOT_DIR}/polkaspots.py', \
                             '--side', ARG_IMAGE_SIDE,  \
                             '--radius', ARG_RADIUS,    \
                             '--dots', str(nb_dots),    \
                             '--images', ARG_NB_IMAGES],\
                             cwd=path)

