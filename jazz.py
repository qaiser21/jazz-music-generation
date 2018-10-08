from __future__ import print_function
import IPython
import sys
import numpy as np
from grammar import *
from music21 import *
from qa import *
from preprocess import *
from music_utils import *
from data_utils import *
from keras.models import load_model, Model
from keras.layers import Dense, Activation, Dropout, Input, LSTM, Reshape, Lambda, RepeatVector
from keras.initializers import glorot_uniform
fromm keras.utils import to_categorical
from keras.optimizers import Adam
from keras import backend as k


IPython.display.Audio('./data/30s_seq.mp3')

X,Y, n_values, indices_values = load_music_utils()

n_a = 64

reshapor = Reshape((1,78))
LSTM_cell = LSTM(n_a, return_state=True)
densor = Dense(n_values, activation = 'softmax')

def djmodel(Tx, n_a, n_values):


