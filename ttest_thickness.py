#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:53:43 2017

@author: vs796
"""

from scipy import stats
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
###############ADHD################
df = pd.read_csv('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/volume_thickness_072717/Cortical_thickness.csv', skiprows = range(37,70))

left_gm = df.lh_MeanThickness_thickness
right_gm = df.rh_MeanThickness_thickness
case = df.Subject

####################control########
dfc = pd.read_csv('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/volume_thickness_072717/Cortical_thickness.csv', skiprows = range(1,37))

left_gm1 = dfc.lh_MeanThickness_thickness
right_gm1 = dfc.rh_MeanThickness_thickness
case_control = dfc.Subject
################Making Space #########
subject =[]
left_gm=[]
right_gm=[]

for x in range(0,len(case)):
    sub=('ADHD')
    subject.append(sub)
    l_gm=df.lh_MeanThickness_thickness[x]
    left_gm.append(l_gm)
    r_gm=df.rh_MeanThickness_thickness[x]
    right_gm.append(r_gm)

    
for y in range(0,len(case_control)):
    sub1=('Control')
    subject.append(sub1)
    l_gm1=dfc.lh_MeanThickness_thickness[y]
    left_gm.append(l_gm1)
    r_gm1=dfc.rh_MeanThickness_thickness[y]
    right_gm.append(r_gm1)

    
data={'Group': subject,'Left Gray Matter': left_gm, 'Right Gray Matter': right_gm}    
    
d=pd.DataFrame(data)

###########left gray matter############
sns.set(style="whitegrid", palette="Set2")
sns.boxplot(x="Group", y="Left Gray Matter", data=d, whis=np.inf)
sns.swarmplot(x="Group", y="Left Gray Matter", color="0.1", data=d, size = 6)
sns.plt.title('Left Hemisphere Gray Matter: Thickness', size=20)
plt.xlabel("Group", size = 15)
plt.ylabel("Left Cortex Gray Matter Thickness Values", size = 15)
print(stats.ttest_ind(left_gm[0:36], left_gm[36:69], equal_var = False))
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/tables/left_gray_thickness.png', bbox_inches = 'tight')


##########right gray matter########
sns.set(style="whitegrid", palette="Set2")
sns.boxplot(x="Group", y="Right Gray Matter", data=d, whis=np.inf)
sns.swarmplot(x="Group", y="Right Gray Matter", color="0.1", data=d, size = 6)
sns.plt.title('Right Hemisphere Gray Matter: Thickness', size=20)
plt.xlabel("Group", size = 15)
plt.ylabel("Right Cortex Gray Matter Thickness Values", size = 15)
print(stats.ttest_ind(right_gm[0:36], right_gm[36:69], equal_var = False))
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/tables/right_gray_thickness.png', bbox_inches = 'tight')

