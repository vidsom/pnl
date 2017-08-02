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

rtap_array_adhd = []


caselist_adhd = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/caselist_ADHD.csv",'r+')


for line in caselist_adhd:
    casenumber = line.rstrip()
    
    
    image_data_rtap, image_header_rtap = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/RTAP/{0}_RTAP.nii' .format(casenumber))
    image_data_msd, image_header_msd = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/MSD/{0}_MSD.nii' .format(casenumber))

    
    vector_rtap = np.reshape(image_data_rtap, [np.prod(np.array(image_data_rtap.shape))])
    vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])

    
    
    in_l = (vector_msd<= 10)
    keep = np.where(in_l)
    final_vector_rtap = vector_rtap[keep]
    
    
    average_rtap = np.mean(final_vector_rtap)
    rtap_array_adhd.append(average_rtap)


caselist_adhd.close()

age_array_adhd = []

agelist_adhd = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/age_adhd.csv",'r+')

for line in agelist_adhd:
    age =  line.rstrip()
    
    age_array_adhd.append(float(age))
    
agelist_adhd.close()

#####################

rtap_array = []


caselist = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/caselist_control.csv",'r+')


for line in caselist:
    casenumber = line.rstrip()
    
    
    image_data_rtap, image_header_rtap = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/RTAP/{0}_RTAP.nii' .format(casenumber))
    image_data_msd, image_header_msd = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/MSD/{0}_MSD.nii' .format(casenumber))
    
    
    vector_rtap = np.reshape(image_data_rtap, [np.prod(np.array(image_data_rtap.shape))])
    vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])

    
    in_l = (vector_msd<= 10)
    keep = np.where(in_l)
    final_vector_rtap = vector_rtap[keep]
    
    
    average_rtap = np.mean(final_vector_rtap)
    rtap_array.append(average_rtap)


caselist.close()

age_array = []

agelist = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/age_control.csv",'r+')

for line in agelist:
    age =  line.rstrip()
    
    age_array.append(float(age))
    
agelist.close()


data={'RTAP': rtap_array,'AGE': age_array }
d = pd.DataFrame(data)

data1={'RTAP ADHD': rtap_array_adhd, 'AGE ADHD': age_array_adhd}
d1 = pd.DataFrame(data1)


f, ax = plt.subplots()
ax.set(xlim=(7.8, 14.1), ylim=(700, 2300))


sns.plt.title('RTAP and Age Correlation', size = 21)

    
z, x = (pearsonr(age_array, rtap_array))

t, s = (pearsonr(age_array_adhd, rtap_array_adhd))


sns.regplot(x="AGE", y="RTAP", robust=True, data=d, ci = None, scatter_kws = {'color':'red'}, line_kws = {'color':'red'})

sns.regplot(x="AGE ADHD", y="RTAP ADHD", robust=True, data=d1, ci = None, scatter_kws = {'color':'blue'}, line_kws = {'color':'blue'})
    

sns.plt.ylabel("Return-to-the-Axis Probability", size = 16)
sns.plt.xlabel("Age", size = 16)


green_line = mpatches.Patch(color = 'red')
    
blue_line = mpatches.Patch(color = 'blue')

plt.legend([green_line, blue_line], ['Control = {0}' .format(z), 'ADHD = {0}' .format(t)], prop = {'size': 12})

    
#plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/final_graphs/correlation_age_rtap.png', bbox_inches = 'tight')
    
    
sns.plt.show()