#!/usr/local/bin/python3
import os, sys
import pandas as pd
import numpy as np
import math
import keras
from keras import *
from keras.models import load_model
import subprocess

def physicochemical(xdir, sequence):
    pdir = xdir + '/../features_generation/physicochemical'
    print(pdir)
    subprocess.call(('{0}/phsicochemical.py'.format(pdir), '{0}'.format(sequence)))
    return

def main():
    xdir = sys.argv[0]
    xdir = os.path.dirname(xdir)
    sequence = sys.argv[1]
    print(xdir)
    physicochemical(xdir, sequence)


if __name__ == '__main__':
    main()
