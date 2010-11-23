# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:40:16 2010
This script will read in limit surface data from a Matlab ".mat" files and 
overlay the limit surfaces on a plot
@author: Noe
"""

from scipy.io import loadmat
from matPlotTools import *

files = ['F:\\StageData\\microWedges\\20s\\20sSqueegeeScaling\\20s_10xW_sE_r1\\experiment.mat']
files.append('F:\\StageData\\Hierarchical\\SqueegeeOnPillar\\H3S3\\H3-s3-r1-glass.mat')

LSData = []
for file in files:
    LSData.append(loadmat(file))

for dataset in LSData:
    plotLS_all(dataset)

plotLS_overlay(LSData)