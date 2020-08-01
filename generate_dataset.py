"""Generate dataset of images containing dots, using polkaspots.py, across a
   range of dot radii and dot counts."""

import glob
import os
import shutil
import subprocess

if __name__ == '__main__':
    # python polkaspots.py --side 256 --radius 2 --dots 10 --images 100
    NB_IMAGES = 200
    IMAGE_SIDE = 256
    radii = range(2, 40+1)
    dot_counts = range(0, 10+1)

    ARG_IMAGE_SIDE = str(IMAGE_SIDE)
    ARG_NB_IMAGES = str(NB_IMAGES)

    CUR_DIR = os.path.abspath('.')
    DATA_ROOT = os.path.abspath(os.path.join(CUR_DIR, 'polkaspots_dataset'))
    IMG_DIR = os.path.abspath(os.path.join(DATA_ROOT, 'images'))
    POS_DIR = os.path.abspath(os.path.join(DATA_ROOT, 'positions'))

    for radius in radii:
        print('radius', radius)

        ARG_RADIUS = str(radius)
        for nb_dots in dot_counts:
            print('nb_dots', nb_dots)

            img_path = f'{IMG_DIR}/radius{radius:02d}/{nb_dots:02d}'
            os.makedirs(img_path)

            pos_path = f'{POS_DIR}/radius{radius:02d}/{nb_dots:02d}'
            os.makedirs(pos_path)

            subprocess.call(['python', f'{CUR_DIR}/polkaspots.py', \
                             '--side', ARG_IMAGE_SIDE,  \
                             '--radius', ARG_RADIUS,    \
                             '--dots', str(nb_dots),    \
                             '--images', ARG_NB_IMAGES],\
                             cwd=img_path)

            csvs = glob.glob(f'{img_path}/*.csv')
            for csv in csvs:
                shutil.move(csv, pos_path)
