#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:53:57 2017

@author: vs796
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from medpy.io import load


white_matter = {3028,3027,3032,3020,3019,3018,3014,3003,3012,3024,3017,3002,3026,3011,3013,3005,3021,3008,3029,3031,3025,3022,3023,3010,3009,3015,3030,3033,3034,3007,3006,3016,4028,4027,4032,4040,4019,4018,4014,4003,4012,4024,4017,4002,4026,4011,4013,4005,4021,4008,4029,4031,4025,4022,4023,4020,4009,4015,4030,4033,4034,4007,4006,4016}
gray_matter = {1028,1027,1032,1020,1019,1018,1014,1003,1012,1024,1017,1002,1026,1011,1013,1005,1021,1008,1029,1031,1025,1022,1023,1010,1009,1015,1030,1033,1034,1007,1006,1016,2028,2027,2032,2020,2019,2018,2014,2003,2012,2024,2017,2002,2026,2011,2013,2005,2021,2008,2029,2031,2025,2022,2023,2020,2009,2015,2030,2033,2034,2007,2006,2016}
sub_cortical = {50,51,58,54,49,52,60,53,11,12,18,26,10,13,28,17}
cerebellum = {7,8,46,47}
left_wm = {3028,3027,3032,3020,3019,3018,3014,3003,3012,3024,3017,3002,3026,3011,3013,3005,3021,3008,3029,3031,3025,3022,3023,3010,3009,3015,3030,3033,3034,3007,3006,3016}
right_wm = {4028,4027,4032,4040,4019,4018,4014,4003,4012,4024,4017,4002,4026,4011,4013,4005,4021,4008,4029,4031,4025,4022,4023,4020,4009,4015,4030,4033,4034,4007,4006,4016}
left_gm = {1028,1027,1032,1020,1019,1018,1014,1003,1012,1024,1017,1002,1026,1011,1013,1005,1021,1008,1029,1031,1025,1022,1023,1010,1009,1015,1030,1033,1034,1007,1006,1016}
right_gm = {2028,2027,2032,2020,2019,2018,2014,2003,2012,2024,2017,2002,2026,2011,2013,2005,2021,2008,2029,2031,2025,2022,2023,2020,2009,2015,2030,2033,2034,2007,2006,2016}

segment = [white_matter, gray_matter, sub_cortical, cerebellum, left_wm, right_wm, left_gm, right_gm]
segment_name = ('white_matter', 'gray_matter', 'sub_cortical', 'cerebellum', 'left_wm', 'right_wm', 'left_gm', 'right_gm')
region = ('White Matter', 'Gray Matter', 'Subcortical Gray Matter', 'Cerebellum', 'Left Cortical White Matter', 'Right Cortical White Matter', 'Left Cortical Gray Matter', 'Right Cortical Gray Matter')

t_statistic = []
p_value = []

for count , element in enumerate(segment):
    print(count)
    print(element)
    rtop_array = []
    rtop_all = []
    subject = []
    rtop_array1 = []
    
    case = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/caselist.txt",'r+')
    
    for line in case:
        casenumber = line.rstrip()
    
    
        image_data_rtop, image_header_rtop = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/RTOP/{0}_RTOP.nii' .format(casenumber))
        image_data_fs, image_header_fs = load("/rfanfs/pnl-zorro/projects/ADHD/freesurferInDWISpace_07232017_GIBBS_CORRECTED/{0}/wmparc-in-bse_2mm.nii" .format(casenumber))
        image_data_msd, image_header_msd = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/MSD/{0}_MSD.nii' .format(casenumber))

    
        vector_rtop = np.reshape(image_data_rtop, [np.prod(np.array(image_data_rtop.shape))])
        vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
        vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])

            
        id=[]
        id_msd=[]
        for i in element:
            gray=(vector_fs==i)
            k=np.where(gray)
            shape=vector_rtop[k]
            shape_2=vector_msd[k]
            id_msd.append(shape_2)
            id.append(shape)
    
        gray_rtop=np.concatenate((id[0:len(id)]))
        gray_msd=np.concatenate((id_msd[0:len(id_msd)]))
        
        
        in_l = (gray_msd<= 10)
        keep = np.where(in_l)
        final_gray_rtop = gray_rtop[keep]
    
        
        average_gray_rtop = np.mean(final_gray_rtop)
        average_gray_all = np.mean(final_gray_rtop)
        rtop_all.append(average_gray_all)
        if casenumber.startswith('case1'):
            rtop_array.append(average_gray_rtop)
            sub = ('ADHD')
            subject.append(sub)
        else:
            rtop_array1.append(average_gray_rtop)
            sub1 = ('Control')
            subject.append(sub1)
        
    
    case.close()
    
    #############
    
    
    data={'Values': rtop_all,'Group': subject }
    
    d = pd.DataFrame(data)
    ROI=region[count]
    roi = segment_name[count]
    
    t, s = (stats.ttest_ind(rtop_array, rtop_array1, equal_var = False))
    print(stats.ttest_ind(rtop_array, rtop_array1, equal_var = False))
    
    t_statistic.append(t)
    p_value.append(s)

    from math import sqrt
    cohens_d = (np.mean(rtop_array) - np.mean(rtop_array1)) / (sqrt((np.std(rtop_array) ** 2 + np.std(rtop_array1) ** 2) / 2))
    print(cohens_d)

    sns.set(style="whitegrid", palette="Set2")
    sns.boxplot(x="Group", y="Values", data=d, whis=np.inf)
    sns.swarmplot(x="Group", y="Values", color="0.1", data=d, size = 4.5)
    ax = sns.swarmplot(x="Group", y="Values", color="0.1", data=d, size = 4.5, label = 't-value = {} \np-value = {} \ncohens-d = {}' .format(t,s,cohens_d))
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[:1], labels[:1], prop = {'size':10.5}, loc = 9)
    sns.plt.title('{0}: RTOP'.format(ROI), size=20)
    plt.xlabel("Group", size = 16)
    plt.ylabel("RTOP Values", size = 16)
#    plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/new_graphs/{0}_rtop.png' .format(roi), bbox_inches = 'tight')
    plt.show()    


    
    