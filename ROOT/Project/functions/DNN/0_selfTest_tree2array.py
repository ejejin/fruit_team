##!/usr/bin/env python
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import keras.backend as K
import math

from ROOT import TFile, TTree, TCut, TH1F
from subprocess import call
from os.path import isfile
from array import array

from root_numpy import fill_hist
from root_numpy import root2array, tree2array, array2root
from root_numpy import testdata

from keras import callbacks
from keras.models import Sequential
from keras.layers import Input
from keras.layers.core import Dense, Activation, Dropout
from keras.layers import BatchNormalization
from keras.regularizers import l1, l2
from keras import initializers
from keras import layers
from keras.optimizers import SGD, Adam
from keras.constraints import maxnorm


####################################### SELF SETTING !!!!! 

#data = TFile.Open('/Users/leejunho/Desktop/tensorflow/input_TTZ_DelphesEvalGen_5275k.root')
data = TFile.Open("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/carbon_copied_data/Aqi_Beijing_day_tree_cut.root")
tree = data.Get('Aqi_Beijing_day_f')


upper_limit = 1000   # 1000


EPOCHS = 100
#NODENUM = 128
NODENUM = 100
BATCH_SIZE_train = 10  # 500
BATCH_SIZE_test = 1  # 1
OPTIMIZER = 'adam'  #'adam', 'Adamax', 'adagrad', 'sgd', 'adadelta', 'RMSprop', 'Nadam', 'TFOptimizer'
KERNAL_INIT = 'he_uniform'  #truncated_normal, glorot_uniform, random_uniform, he_uniform, he_normal
L2 = 1e-5  #1e-5
DROP_RATE = 0.0  # 0.2
MAXNORM = 10000000 #5
ACTIVATION = "relu"

LOAD_WEIGHTS = False   #True #False

###############################################################################################################



####################################### Input DATA Sets !!!!! 
#b_AQI_     = tree2array(tree,branches="AQI")
b_CO_      = tree2array(tree,branches="CO")
b_NO2_     = tree2array(tree,branches="NO2")
b_O3_8h_   = tree2array(tree,branches="O3_8h")
b_PM10_    = tree2array(tree,branches="PM10")
#b_PM2p5_   = tree2array(tree,branches="PM2p5")
b_SO2_     = tree2array(tree,branches="SO2")
###############################################################################################################
##################################### Target DATA !!!!!
b_TARGET_   = tree2array(tree,branches="PM2p5")
###############################################################################################################


##################################### Pick valid Input/Target DATA  (TARGET is output data) !!!!!
#b_AQI      = np.zeros(b_AQI_.size)
b_CO       = np.zeros(b_CO_.size)
b_NO2      = np.zeros(b_NO2_.size)
b_O3_8h    = np.zeros(b_O3_8h_.size)
b_PM10     = np.zeros(b_PM10_.size)
#b_PM2p5    = np.zeros(b_PM2p5_.size)
b_SO2      = np.zeros(b_SO2_.size)

b_TARGET     = np.zeros(b_TARGET_.size)

for i in range(b_TARGET.size):
#    b_AQI[i]    = b_AQI_[i]
    b_CO[i]     = b_CO_[i]
    b_NO2[i]    = b_NO2_[i]
    b_O3_8h[i]  = b_O3_8h_[i]
    b_PM10[i]   = b_PM10_[i]
#    b_PM2p5[i]  = b_PM2p5_[i]
    b_SO2[i]    = b_SO2_[i]

    b_TARGET[i] = b_TARGET_[i]

###############################################################################################################



##################################### ARRAY is input DATA !!!!!
ARRAY = np.stack((b_CO,b_NO2,b_O3_8h,b_PM10,b_SO2))

print(ARRAY.shape)
ARRAY = ARRAY.T
print(ARRAY.shape)
print(ARRAY[:2])
print(b_TARGET[:2])
###############################################################################################################


ndim = ARRAY.shape[1]  
nEvents = ARRAY.shape[0]

data_train = ARRAY[0:upper_limit]
target_train = b_TARGET[0:upper_limit]
data_test = ARRAY[(upper_limit+1):ARRAY.shape[0]]
target_test = b_TARGET[(upper_limit+1):ARRAY.shape[0]]


ijkl = 0
modelRegress = Sequential()
#modelRegress.add(Dropout(DROP_RATE, input_shape=(ndim,)))
#modelRegress.add(Dense(NODENUM, kernel_initializer=KERNAL_INIT, activation=ACTIVATION, W_regularizer=l2(L2), kernel_constraint=maxnorm(3))) 
modelRegress.add(Dense(NODENUM, kernel_initializer=KERNAL_INIT, activation=ACTIVATION, W_regularizer=l2(L2), input_dim=ndim, kernel_constraint=maxnorm(MAXNORM)))
#modelRegress.add(BatchNormalization())
#modelRegress.add(Activation(ACTIVATION))
modelRegress.add(Dropout(DROP_RATE))
ijkl = ijkl + 1


modelRegress.add(Dense(NODENUM, kernel_initializer=KERNAL_INIT, activation=ACTIVATION, W_regularizer=l2(L2),kernel_constraint=maxnorm(MAXNORM)))
modelRegress.add(Dropout(DROP_RATE))
ijkl = ijkl + 1



modelRegress.add(Dense(NODENUM, kernel_initializer=KERNAL_INIT, activation=ACTIVATION, W_regularizer=l2(L2)))  #additional layer
modelRegress.add(Dropout(DROP_RATE))
ijkl = ijkl + 1

modelRegress.add(Dense(NODENUM, kernel_initializer=KERNAL_INIT, activation=ACTIVATION, W_regularizer=l2(L2)))  #additional layer
modelRegress.add(Dropout(DROP_RATE))
ijkl = ijkl + 1

modelRegress.add(Dense(NODENUM, kernel_initializer=KERNAL_INIT, activation=ACTIVATION, W_regularizer=l2(L2)))  #additional layer
modelRegress.add(Dropout(DROP_RATE))
ijkl = ijkl + 1



modelRegress.add(Dense(1, kernel_initializer=KERNAL_INIT,  activation='linear')) #sigmoid
modelRegress.compile(loss='mean_squared_error', optimizer=OPTIMIZER)
if(LOAD_WEIGHTS == True):  modelRegress.load_weights(LOAD_MODEL_WEIGHTS,by_name=True)
modelRegress.summary()
history_callback = modelRegress.fit(data_train, target_train, validation_data=(data_test, target_test), epochs=EPOCHS, batch_size=BATCH_SIZE_train)


predict_train = modelRegress.predict(data_train, batch_size=BATCH_SIZE_test)
predict_test = modelRegress.predict(data_test, batch_size=BATCH_SIZE_test)

f = TFile("self_tree_EN"+str(upper_limit)+"_LN"+str(ijkl)+"_E"+str(EPOCHS)+"_NN"+str(NODENUM)+"_B"+str(BATCH_SIZE_train)+"_"+str(OPTIMIZER)+"_L"+str(L2)+"_DR"+str(DROP_RATE)+".root", "recreate")


hist_target_train = TH1F('TrainData','TrainData',100,0,300)
hist_target_test = TH1F('TestData','TestData',100,0,300)
hist_output_train = TH1F('OutputDataTrain','OutputDataTrain',100,0,300)
hist_output_test = TH1F('OutputDataTest','OutputDataTest',100,0,300)

tree_train = TTree('tree_train','tree_train')
Ttrain = np.zeros(1, dtype=float)
Otrain = np.zeros(1, dtype=float)
tree_train.Branch('target_train',Ttrain,'target_train/D')
tree_train.Branch('output_train',Otrain,'output_train/D')
for ij1 in range(upper_limit):
	Ttrain[0] = target_train[ij1] 
	Otrain[0] = predict_train[ij1]		
	tree_train.Fill()

tree_test = TTree('tree_test','tree_test')
Ttest = np.zeros(1, dtype=float)
Otest = np.zeros(1, dtype=float)
tree_test.Branch('target_test',Ttest,'target_test/D')
tree_test.Branch('output_test',Otest,'output_test/D')
for ij2 in range(ARRAY.shape[0]-upper_limit-1):
	Ttest[0] = target_test[ij2]
	Otest[0] = predict_test[ij2]
	tree_test.Fill()


#Plots: projection selon l'axe X (premiere variable)
fill_hist(hist_target_train, target_train)
fill_hist(hist_target_test, target_test)
fill_hist(hist_output_train, predict_train[:,0])
fill_hist(hist_output_test, predict_test[:,0])

f.Write()
f.Close()

