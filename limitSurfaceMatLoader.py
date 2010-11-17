# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 15:22:25 2010
This script will load Matlab '.mat' files from the stage's experimental data 
and plot the results
@author: Noe
"""

from scipy.io import loadmat
file = 'F:\\StageData\\microWedges\\20s\\20sSqueegeeScaling\\20s_10xW_sA_r1\\experiment.mat'

myMat = loadmat(file)

