# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:03:41 2010
This is a module with the ability to generate plots from stage data generated
by Matlab
@author: Noe
"""

from numpy import squeeze, zeros
import matplotlib.pyplot as mp		#import of plotting module

def plotLS_all(data):
    FxPulloffVectorKPa = data['FxPulloffVector']/data['areaSampleSquareCentimeter'] * 10
    FyPulloffVectorKPa = data['FyPulloffVector']/data['areaSampleSquareCentimeter'] * 10
    FzPulloffVectorKPa = data['FzPulloffVector']/data['areaSampleSquareCentimeter'] * 10
    
    
    mp.figure()
    mp.hold(True)
    color = ['b','g','r','c','m','y','k']
    shape = ['o','x','+','*','s','d','v','p','h','.']
    
    # create a list of lists to hold the plot handles
    plotH = [[0 for x in range(data['anglePulloffDegree'].size)] for y in range(data['distancePreloadMicron'].size)]
    
    # This loop goes through all the data points and plots them in force space
    for i, depth in enumerate(squeeze(data['distancePreloadMicron'])):
    	for j, angle in enumerate(squeeze(data['anglePulloffDegree'])):
    		for k in range(data['numTrials']):
    			plotH[i][j], = mp.plot(-FyPulloffVectorKPa[i,j,k],
                -FzPulloffVectorKPa[i,j,k],
                markeredgecolor = color[i],
                markeredgewidth = 1,
                marker = shape[j],
                markersize = 10, markerfacecolor = 'None')
    
    # These loops generate the legend information
    
    legendStrList = []
    # This list holds the plot handles that are used to generate the legend
    plotHlist = []
    for i, depth in enumerate(squeeze(data['distancePreloadMicron'])):
        legendStrList.append ('%03d preload' % (depth,))
        plotHlist.append(plotH[i][1])
    for j, angle in enumerate(squeeze(data['anglePulloffDegree'])):
        legendStrList.append('%02d angle' % angle)
        plotHlist.append(plotH[i][j])
    
    #This places the legend outside to the right of the axes
    mp.legend(plotHlist,legendStrList, bbox_to_anchor=(1.05, 1), loc=2)
    # This adjustment makes sure the legend doesnt get cut off
    mp.subplots_adjust(right = 0.75)
    mp.figtext(0.4,0.4,
               ('patch area = %.03g cm^2' % data['areaSampleSquareCentimeter']))
    mp.ylabel('Normal Pressure (kPa)')
    mp.xlabel('Shear Pressure (kPa)')
    mp.grid()
    mp.draw()
    mp.show()

def plotLS_overlay(datasets):
    plotH = []
    mp.figure()
    mp.hold(True)
    
    for x,data in enumerate(datasets):
        FxPulloffVectorKPa = data['FxPulloffVector']/data['areaSampleSquareCentimeter'] * 10
        FyPulloffVectorKPa = data['FyPulloffVector']/data['areaSampleSquareCentimeter'] * 10
        FzPulloffVectorKPa = data['FzPulloffVector']/data['areaSampleSquareCentimeter'] * 10   
        
        
        color = ['b','g','r','c','m','y','k']
        shape = ['o','x','+','*','s','d','v','p','h','.']
        
         # This loop goes through all the data points and plots them in force space
        for i, depth in enumerate(squeeze(data['distancePreloadMicron'])):
            for j, angle in enumerate(squeeze(data['anglePulloffDegree'])):
                for k in range(data['numTrials']):
                    plotHTmp = mp.plot(-FyPulloffVectorKPa[i,j,k],
                    -FzPulloffVectorKPa[i,j,k],
                    markeredgecolor = color[x],
                    markeredgewidth = 1,
                    marker = shape[x],
                    markersize = 10, markerfacecolor = 'None')
        plotH.append(plotHTmp)

    mp.axhline(color = 'k', linewidth = 2)
    mp.axvline(color = 'k', linewidth = 2)
    mp.legend(plotH, ('Squeegee','Hierarchy 3'), loc = 'upper left') # need to make this robust
    mp.ylabel('Normal Pressure (kPa)')
    mp.xlabel('Shear Pressure (kPa)')
    mp.grid()
    mp.draw()
    mp.show()