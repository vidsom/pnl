#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:18:05 2017

@author: vs796
"""

from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from medpy.io import load
import numpy as np
import seaborn as sns
import pandas as pd

rtop_array_adhd = []
rtop_array = []


caselist = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/caselist.txt",'r+')


for line in caselist:
    casenumber = line.rstrip()
    
    
    image_data_rtop, image_header_rtop = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/RTOP/{0}_RTOP.nii' .format(casenumber))
    image_data_msd, image_header_msd = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/MSD/{0}_MSD.nii' .format(casenumber))
    
    vector_rtop = np.reshape(image_data_rtop, [np.prod(np.array(image_data_rtop.shape))])
    vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])

    in_l = (vector_msd<= 10)
    keep = np.where(in_l)
    final_vector_rtop = vector_rtop[keep]    
    
    average_rtop = np.mean(vector_rtop)
    if casenumber.startswith('case1'):
        rtop_array_adhd.append(average_rtop)
    else:
        rtop_array.append(average_rtop)


caselist.close()

age_array_adhd = []

agelist_adhd = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/age_adhd.csv",'r+')

for line in agelist_adhd:
    age =  line.rstrip()
    
    age_array_adhd.append(float(age))
    
agelist_adhd.close()

#####################


age_array = []

agelist = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/age_control.csv",'r+')

for line in agelist:
    age =  line.rstrip()
    
    age_array.append(float(age))
    
agelist.close()


data={'RTOP': rtop_array,'AGE': age_array }
d = pd.DataFrame(data)

data1={'RTOP ADHD': rtop_array_adhd, 'AGE ADHD': age_array_adhd}
d1 = pd.DataFrame(data1)


f, ax = plt.subplots()
ax.set(xlim=(7.8, 14.1), ylim=(35000, 220000))


sns.plt.title('RTOP and Age Correlation', size = 21)

    
z, x = (pearsonr(age_array, rtop_array))

t, s = (pearsonr(age_array_adhd, rtop_array_adhd))


sns.regplot(x="AGE", y="RTOP", robust=True, data=d, ci = None, scatter_kws = {'color':'red'}, line_kws = {'color':'red'})

sns.regplot(x="AGE ADHD", y="RTOP ADHD", robust=True, data=d1, ci = None, scatter_kws = {'color':'blue'}, line_kws = {'color':'blue'})
    

sns.plt.ylabel("Return-to-the-Origin Probability", size = 16)
sns.plt.xlabel("Age", size = 16)


green_line = mpatches.Patch(color = 'red')
    
blue_line = mpatches.Patch(color = 'blue')

plt.legend([green_line, blue_line], ['Control = {0}' .format(z), 'ADHD = {0}' .format(t)], prop = {'size': 12})

    
#plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/final_graphs/correlation_age_rtop.png', bbox_inches = 'tight')
    
    
sns.plt.show()