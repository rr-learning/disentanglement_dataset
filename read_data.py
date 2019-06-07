#!/usr/bin/env python

import imageio
import numpy as np
import os
import glob
import re
import argparse

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts 

def main():
    parser = argparse.ArgumentParser(description='Read img files and save them in a numpy array.')
    parser.add_argument('--img_folder', type=str, default=None, help='path to the images.')
    parser.add_argument('--destination_folder', type=str, default=None, help='path to store the numpy arrays.')
    args = parser.parse_args()
    imgs_list = []
    for infile in sorted(glob.glob(os.path.join(args.img_folder ,'*.png')), key=numericalSort):
        imgs_list.append(imageio.imread(infile))

    imgs_array = np.asarray(imgs_list, dtype = np.uint8)
    np.savez(args.destination_folder, images = imgs_array)
    print ('Done!')

if __name__ == '__main__':
    main()
