SEED=123

import os
os.environ['HOME'] = '/root'
#os.environ['PYTHONUNBUFFERED'] = '1'

#numerical libs
import numpy as np
import random
import PIL
import cv2

random.seed(SEED)
np.random.seed(SEED)

import matplotlib
matplotlib.use('TkAgg')
#matplotlib.use('Qt4Agg')
#matplotlib.use('Qt5Agg')



# torch libs
import torch
import torchvision.transforms as transforms
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
from torch.utils.data.sampler import *

import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch.optim as optim


# std libs
import pickle
from timeit import default_timer as timer   #ubuntu:  default_timer = time.time,  seconds
from datetime import datetime
import csv
import pandas as pd
import pickle
import glob
import sys
#from time import sleep

import matplotlib.pyplot as plt


'''
updating pytorch
    https://discuss.pytorch.org/t/updating-pytorch/309
    
    ./conda config --add channels soumith

'''