# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 22:56:49 2010
This script goes through a set of files and pulls out data
of interest to output to csv file

@author: Noe
"""
from scipy.io import loadmat
from numpy import squeeze,where
import matplotlib.pyplot as mp		#import of plotting module


files = ['F:\\StageData\\microWedges\\20s\\20sSqueegeeScaling\\20s_10xW_sA_r1\\experiment.mat']
files.append('F:\\StageData\\microWedges\\20s\\20sSqueegeeScaling\\20s_10xW_sB_r1\\experiment.mat')
files.append('F:\\StageData\\microWedges\\20s\\20sSqueegeeScaling\\20s_10xW_sC_r1\\experiment.mat')
files.append('F:\\StageData\\microWedges\\20s\\20sSqueegeeScaling\\20s_10xW_sD_r1\\experiment.mat')
files.append('F:\\StageData\\microWedges\\20s\\20sSqueegeeScaling\\20s_10xW_sE_r1\\experiment.mat')
files.append('F:\\StageData\\microWedges\\20s\\20sSqueegeeScaling\\20s_10xW_sF_r1\\experiment.mat')

mp.figure()
mp.hold(True)
color = ['b','g','r','c','m','y','k']
shape = ['o','x','+','*','s','d','v','p','h','.']
plotHList = []
legendStrList = []

outputData = {}

for indy, file in enumerate(files):
    data = loadmat(file)
    FyPulloffVectorKPa = data['FyPulloffVector']/data['areaSampleSquareCentimeter'] * 10
    FzPulloffVectorKPa = data['FzPulloffVector']/data['areaSampleSquareCentimeter'] * 10   
    currKey = '%.03g cm^2' % data['areaSampleSquareCentimeter']
    outputData[currKey] = []
    for i, depth in enumerate(squeeze(data['distancePreloadMicron'])):
        for j, angle in enumerate(squeeze(data['anglePulloffDegree'])):
            for k in range(data['numTrials']):
                if (angle == 80 and depth == 60):
                    plotHTmp, = mp.plot(-FyPulloffVectorKPa[i,j,k],
                    -FzPulloffVectorKPa[i,j,k],
                    markeredgecolor = color[i],
                    markeredgewidth = 1,
                    marker = shape[indy],
                    markersize = 10, markerfacecolor = 'None')
                    outputData[currKey].append((-FyPulloffVectorKPa[i,j,k],
                    -FzPulloffVectorKPa[i,j,k]))
                elif (angle == 70 and depth == 60):
                    plotHTmp, = mp.plot(-FyPulloffVectorKPa[i,j,k],
                    -FzPulloffVectorKPa[i,j,k],
                    markeredgecolor = color[i],
                    markeredgewidth = 1,
                    marker = shape[indy],
                    markersize = 5, markerfacecolor = 'None')
    
    legendStrList.append('area = %.03g cm$^{2}$' % data['areaSampleSquareCentimeter'])
    plotHList.append(plotHTmp)
    
    
mp.axhline(color = 'k', linewidth = 2)
mp.axvline(color = 'k', linewidth = 2)
mp.legend(plotHList, legendStrList, loc = 'upper right')
mp.ylabel('Normal Pressure (kPa)')
mp.xlabel('Shear Pressure (kPa)')
mp.grid()
mp.draw()
mp.show()