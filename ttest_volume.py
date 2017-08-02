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
df = pd.read_csv('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/volume_thickness_072717/Volume_GM_WM_SBC.csv', skiprows = range(37,70))

left_gm = df.lhCortexVol
right_gm = df.rhCortexVol
gm = df.CortexVol
left_wm = df.lhCorticalWhiteMatterVol
right_wm = df.rhCorticalWhiteMatterVol
wm = df.CorticalWhiteMatterVol
subcortical = df.SubCortGrayVol
case = df.Subject

####################control########
dfc = pd.read_csv('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/volume_thickness_072717/Volume_GM_WM_SBC.csv', skiprows = range(1,37))

left_gm1 = dfc.lhCortexVol
right_gm1 = dfc.rhCortexVol
gm1 = dfc.CortexVol
left_wm1 = dfc.lhCorticalWhiteMatterVol
right_wm1 = dfc.rhCorticalWhiteMatterVol
wm1 = dfc.CorticalWhiteMatterVol
subcortical1 = dfc.SubCortGrayVol
case_control = dfc.Subject
################Making Space #########
subject =[]
left_gm=[]
right_gm=[]
gm=[]
left_wm=[]
right_wm=[]
wm=[]
subcor=[]

for x in range(0,len(case)):
    sub=('ADHD')
    subject.append(sub)
    l_gm=df.lhCortexVol[x]
    left_gm.append(l_gm)
    r_gm=df.rhCortexVol[x]
    right_gm.append(r_gm)
    gmatter=df.CortexVol[x]
    gm.append(gmatter)
    l_wm=df.lhCorticalWhiteMatterVol[x]
    left_wm.append(l_wm)
    r_wm=df.rhCorticalWhiteMatterVol[x]
    right_wm.append(r_wm)
    wmatter=df.CorticalWhiteMatterVol[x]
    wm.append(wmatter)
    subcorr=  df.SubCortGrayVol[x] 
    subcor.append(subcorr)
    
for y in range(0,len(case_control)):
    sub1=('Control')
    subject.append(sub1)
    l_gm1=dfc.lhCortexVol[y]
    left_gm.append(l_gm1)
    r_gm1=dfc.rhCortexVol[y]
    right_gm.append(r_gm1)
    gmatter1=dfc.CortexVol[y]
    gm.append(gmatter1)
    l_wm1=dfc.lhCorticalWhiteMatterVol[y]
    left_wm.append(l_wm1)
    r_wm1=dfc.rhCorticalWhiteMatterVol[y]
    right_wm.append(r_wm1)
    wmatter1=dfc.CorticalWhiteMatterVol[y]
    wm.append(wmatter1)
    subcorr1=  dfc.SubCortGrayVol[y] 
    subcor.append(subcorr1)
    
data={'Group': subject,'Left Gray Matter': left_gm, 'Right Gray Matter': right_gm, 'Gray Matter':gm,
      'Left White Matter': left_wm, 'Right White Matter': right_wm, 'White Matter': wm, 
      'Subcortical Gray Matter': subcor }    
    
d=pd.DataFrame(data)
##############gray matter############
sns.set(style="whitegrid", palette="Set2")
sns.boxplot(x="Group", y="Gray Matter", data=d, whis=np.inf)
sns.swarmplot(x="Group", y="Gray Matter", color="0.1", data=d, size = 6)
sns.plt.title('Gray Matter: Volume', size=20)
plt.xlabel("Group", size = 15)
plt.ylabel("Gray Matter Volume Values", size = 15)
print(stats.ttest_ind(gm[0:36], gm[36:69], equal_var = False))
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/tables/gray_volume.pdf', bbox_inches = 'tight')

############white matter###########
sns.set(style="whitegrid", palette="Set2")
sns.boxplot(x="Group", y="White Matter", data=d, whis=np.inf)
sns.swarmplot(x="Group", y="White Matter", color="0.1", data=d, size = 6)
sns.plt.title('White Matter: Volume', size=20)
plt.xlabel("Group", size = 15)
plt.ylabel("White Matter Volume Values", size = 15)
print(stats.ttest_ind(wm[0:36], wm[36:69], equal_var = False))
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/tables/white_volume.pdf', bbox_inches = 'tight')

########subcortical ###############
sns.set(style="whitegrid", palette="Set2")
sns.boxplot(x="Group", y="Subcortical Gray Matter", data=d, whis=np.inf)
sns.swarmplot(x="Group", y="Subcortical Gray Matter", color="0.1", data=d, size = 6)
sns.plt.title('Subcortical Gray Matter: Volume', size=20)
plt.xlabel("Group", size = 15)
plt.ylabel("Subcortical Gray Matter Volume Values", size = 15)
print(stats.ttest_ind(subcor[0:36], subcor[36:69], equal_var = False))
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/tables/subcortical_volume.pdf', bbox_inches = 'tight')

#########left white matter###############
sns.set(style="whitegrid", palette="Set2")
sns.boxplot(x="Group", y="Left White Matter", data=d, whis=np.inf)
sns.swarmplot(x="Group", y="Left White Matter", color="0.1", data=d, size = 6)
sns.plt.title('Left Cortical White Matter Matter: Volume', size=20)
plt.xlabel("Group", size = 15)
plt.ylabel("Left Cortical White Matter Volume Values", size = 15)
print(stats.ttest_ind(left_wm[0:36], left_wm[36:69], equal_var = False))
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/tables/left_white_volume.pdf', bbox_inches = 'tight')

##########right white matter###############
sns.set(style="whitegrid", palette="Set2")
sns.boxplot(x="Group", y="Right White Matter", data=d, whis=np.inf)
sns.swarmplot(x="Group", y="Right White Matter", color="0.1", data=d, size = 6)
sns.plt.title('Right Cortical White Matter: Volume', size=20)
plt.xlabel("Group", size = 15)
plt.ylabel("Right Cortical White Matter Volume Values", size = 15)
print(stats.ttest_ind(right_wm[0:36], right_wm[36:69], equal_var = False))
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/tables/right_white_volume.pdf', bbox_inches = 'tight')

###########left gray matter############
sns.set(style="whitegrid", palette="Set2")
sns.boxplot(x="Group", y="Left Gray Matter", data=d, whis=np.inf)
sns.swarmplot(x="Group", y="Left Gray Matter", color="0.1", data=d, size = 6)
sns.plt.title('Left Hemisphere Gray Matter: Volume', size=20)
plt.xlabel("Group", size = 15)
plt.ylabel("Left Cortex Gray Matter Volume Values", size = 15)
print(stats.ttest_ind(left_gm[0:36], left_gm[36:69], equal_var = False))
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/tables/left_gray_volume.pdf', bbox_inches = 'tight')


##########right gray matter########
sns.set(style="whitegrid", palette="Set2")
sns.boxplot(x="Group", y="Right Gray Matter", data=d, whis=np.inf)
sns.swarmplot(x="Group", y="Right Gray Matter", color="0.1", data=d, size = 6)
sns.plt.title('Right Hemisphere Gray Matter: Volume', size=20)
plt.xlabel("Group", size = 15)
plt.ylabel("Right Cortex Gray Matter Volume Values", size = 15)
print(stats.ttest_ind(right_gm[0:36], right_gm[36:69], equal_var = False))
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/tables/right_gray_volume.pdf', bbox_inches = 'tight')

