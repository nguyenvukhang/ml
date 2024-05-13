import numpy as np, pandas as pd
from keras.datasets import mnist
from os import path

data_dir = path.join(path.dirname(__file__), "data")

X, y = mnist.load_data(path=path.join(data_dir, "mnist"))

print(X.shape())
