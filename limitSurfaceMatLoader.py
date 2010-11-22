# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 15:22:25 2010
This script will load Matlab '.mat' files from the stage's experimental data 
and plot the results
@author: Noe
"""
from numpy import arange, squeeze, zeros
from scipy.io import loadmat
import matplotlib.pyplot as mp		#import of plotting module

file = 'F:\\StageData\\microWedges\\20s\\20sSqueegeeScaling\\20s_10xW_sA_r1\\experiment.mat'

LSdata = loadmat(file)

FxPulloffVectorKPa = LSdata['FxPulloffVector']/LSdata['areaSampleSquareCentimeter'] * 10
FyPulloffVectorKPa = LSdata['FyPulloffVector']/LSdata['areaSampleSquareCentimeter'] * 10
FzPulloffVectorKPa = LSdata['FzPulloffVector']/LSdata['areaSampleSquareCentimeter'] * 10


mp.figure()
mp.hold(True)
color = ['b','g','r','c','m','y','k']
shape = ['o','x','+','*','s','d','v','p','h','.']

plotH = [[0 for x in range(LSdata['anglePulloffDegree'].size)] for y in range(LSdata['distancePreloadMicron'].size)]
# This loop goes through all the data points and plots them in force space
for i, depth in enumerate(squeeze(LSdata['distancePreloadMicron'])):
	for j, angle in enumerate(squeeze(LSdata['anglePulloffDegree'])):
		for k in range(LSdata['numTrials']):
			plotH[i][j], = mp.plot(-FyPulloffVectorKPa[i,j,k],
            -FzPulloffVectorKPa[i,j,k],
            color = color[i],
            marker = shape[j],
            markersize = 10)

# These loops help generate the legend information
legendStrList = []
plotHlist = []
ind = 0
for i, depth in enumerate(squeeze(LSdata['distancePreloadMicron'])):
    legendStrList.append ('%03d preload' % (depth,))
    plotHlist.append(plotH[i][1])
for j, angle in enumerate(squeeze(LSdata['anglePulloffDegree'])):
    legendStrList.append('%02d angle' % angle)
    plotHlist.append(plotH[i][j])
    
mp.legend(plotHlist,legendStrList, bbox_to_anchor=(1.05, 1), loc=2)
# This adjustment makes sure the legend doesnt get cut off
mp.subplots_adjust(right = 0.75)
mp.grid()
mp.draw()
mp.show()