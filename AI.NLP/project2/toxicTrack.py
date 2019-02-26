import sys, os, re, csv, codecs, numpy as np, pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation
from keras.layers import Bidirectional, GlobalMaxPool1D
from keras.models import Model
from keras import initializers, regularizers, constraints, optimizers, layers

train = pd.read_csv('../track_toxic_data/train.csv')
test = pd.read_csv('../track_toxic_data/test.csv')

print(train.head())