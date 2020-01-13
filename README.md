# polkaspots
Counting dots with deep learning

There’s a script file polkaspots.py that can generate images of a given resolution, containing a desired number of dots, of a specified size. Currently generated images are RGB, but I’ll add an option for B/W. Also currently the dots may overlap due to random positioning, but I may later add an option to prevent overlaps. There’s also an iPython/Jupyter notebook starting on the process of training a DL model to output the number of dots in a given image. I want to play around with various architectures and assumptions, eventually.

In the img folder there's a generated dataset of 128x128 pixel images of 10-pixel radius black dots on white backgrounds. Subdirectories each contain 10k images with 0-9 dots each, except for the 0 dot image -- there's only one (symmetry).
