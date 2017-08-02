# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:50:01 2017

@author: vs796
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from medpy.io import load
import numpy as np


sns.set(context = "paper", font = "monospace")

image_data_fs, image_header_fs = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/freesurferINdwi/case104_wmparc-in-bse.nii.gz")
image_data_msd, image_header_msd = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/MSD/case104_MSD.nii")
image_data_fw, image_header_fw = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/FW/case104_FW.nii")
image_data_FA, image_header_FA=load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case104_corr_matrix/case104_FA.nii.gz")
image_data_GK, image_header_GK=load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case104_corr_matrix/case104_GK.nii.gz")
image_data_MFD, image_header_MFD=load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case104_corr_matrix/case104_MFD.nii.gz")
image_data_RTAP, image_header_RTAP=load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case104_corr_matrix/case104_RTAP.nii.gz")
image_data_RTOP, image_header_RTOP=load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case104_corr_matrix/case104_RTOP.nii.gz")
image_data_RTPP, image_header_RTPP=load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case104_corr_matrix/case104_RTPP.nii.gz")
image_data_radial, image_header_RTOP=load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case104_corr_matrix/case104_radial.nii.gz")
image_data_trace, image_header_RTPP=load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case104_corr_matrix/case104_trace.nii.gz")
image_data_axial, image_header_RTOP=load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case104_corr_matrix/case104_axial.nii.gz")

#vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
#vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
#vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])


two_image_fw = np.array(np.reshape(image_data_fw,[110, 110*74]))
two_image_fs = np.array(np.reshape(image_data_fs,[110, 110*74]))
two_image_msd = np.array(np.reshape(image_data_msd,[110, 110*74]))

index = (two_image_fs == 3035)

in_l=np.equal(image_data_fs, 3035)
k=np.where(in_l)
values_msd=image_data_msd[k]
values_fw=image_data_fw[k]
values_FA=image_data_FA[k]
values_GK=image_data_GK[k]
values_MFD=image_data_MFD[k]
values_RTAP=image_data_RTAP[k]
values_RTOP=image_data_RTOP[k]
values_RTPP=image_data_RTPP[k]
values_radial=image_data_radial[k]
values_trace=image_data_trace[k]
values_axial=image_data_axial[k]
values_total=np.sum(image_data_axial[k]+image_data_fw[k])

data= {'CTX-raCG': values_msd, 'CTX-caCG': values_fw, 'CTX-mOF': values_FA, 'CTX-lOF': values_total, 'CTX-IT': values_RTAP, 'CTX-ST': values_RTOP, 'CTX-AG': values_RTPP, 'CTX-SP': values_radial, 'CTX-IP': values_trace, 'CTX-FP': values_axial, 'CTX-TP': values_GK, 'CTX-LO': values_MFD,}
 
d = pd.DataFrame(data)

corrmat = d.corr()
fig, ax =plt.subplots(figsize = (12, 9))

j=sns.heatmap(corrmat,cmap="YlOrRd", vmax=1, square = True, linewidth=0.5)
#j=sns.heatmap(corrmat,cmap="OrRd", vmax=1, square = True,linewidth=0.5)
#j=sns.heatmap(corrmat,cmap="Spectral", vmax=1,vmin=-1, square = True, linewidth=0.5)
#j=sns.heatmap(corrmat,vmax=1,vmin=-1, square = True,linewidth=0.5)
#j.set(xlabel="Network Nodes", ylabel="Network Nodes", title= "Brain Networks")
plt.xlabel('ROIs', size=13)
plt.ylabel('ROIs', size=13)
#plt.title('Brain Networks', size=13)
plt.xticks(rotation=90)
plt.yticks(rotation=360)
sns.set(font="Times")
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/correlation_graphs/correlation_matrix.pdf', bbox_inches = 'tight')
plt.close()

