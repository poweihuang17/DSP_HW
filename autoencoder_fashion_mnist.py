from __future__ import division, print_function, absolute_import

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

import scipy.io
f_mnist = scipy.io.loadmat(‘fashion_mnist_dataset.mat’)

#Get the data and labels using
f_mnist[‘X_train’], f_mnist[‘y_train’], f_mnist[‘X_test’], f_mnist[‘y_test’]