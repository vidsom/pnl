from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from medpy.io import load
import numpy as np
import seaborn as sns
import pandas as pd

white_matter = {3028,3027,3032,3020,3019,3018,3014,3003,3012,3024,3017,3002,3026,3011,3013,3005,3021,3008,3029,3031,3025,3022,3023,3010,3009,3015,3030,3033,3034,3007,3006,3016,4028,4027,4032,4040,4019,4018,4014,4003,4012,4024,4017,4002,4026,4011,4013,4005,4021,4008,4029,4031,4025,4022,4023,4020,4009,4015,4030,4033,4034,4007,4006,4016}
gray_matter = {1028,1027,1032,1020,1019,1018,1014,1003,1012,1024,1017,1002,1026,1011,1013,1005,1021,1008,1029,1031,1025,1022,1023,1010,1009,1015,1030,1033,1034,1007,1006,1016,2028,2027,2032,2020,2019,2018,2014,2003,2012,2024,2017,2002,2026,2011,2013,2005,2021,2008,2029,2031,2025,2022,2023,2020,2009,2015,2030,2033,2034,2007,2006,2016}
sub_cortical = {50,51,58,54,49,52,60,53,11,12,18,26,10,13,28,17}

segment = [white_matter, gray_matter, sub_cortical]
segment_name = ('white_matter', 'gray_matter', 'sub_cortical')
region = ('White Matter', 'Gray Matter', 'Subcortical Gray Matter')

for count , element in enumerate(segment):



    msd_array_adhd = []
    
    
    caselist_adhd = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/caselist_age_adhd.csv",'r+')
    
    
    for line in caselist_adhd:
        casenumber = line.rstrip()
        
        
        image_data_msd, image_header_msd = load('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/MSD/{0}_MSD.nii' .format(casenumber))
        image_data_fs, image_header_fs = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/freesurferINdwi/{0}_wmparc-in-bse.nii.gz" .format(casenumber))
        
        vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])
        vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
        
        
        id=[]
        for i in element:
            gray=(vector_fs==i)
            k=np.where(gray)
            shape=vector_msd[k]
            id.append(shape)
        
        gray_msd=np.concatenate((id[0:len(id)]))
        
        in_l = (gray_msd <= 10)
        keep = np.where(in_l)
        final_gray_msd = gray_msd[keep]


        in_k = (final_gray_msd != 0)
        keep1 = np.where(in_k)
        ultimate_gray_msd = final_gray_msd[keep1]
        
        average_msd = np.mean(ultimate_gray_msd)
        msd_array_adhd.append(average_msd)
    
    
    caselist_adhd.close()
    
    adhdp_t = []
    
    list_adhd = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/ADHDp_T.csv",'r+')
    
    for line in list_adhd:
        measure =  line.rstrip()
        
        adhdp_t.append(float(measure))
        
    list_adhd.close()
    
    
    
    data={'MSD': msd_array_adhd, 'ADHD': adhdp_t}
    d = pd.DataFrame(data)
    
    ROI = region[count]
    roi = segment_name[count]


    f, ax = plt.subplots()
    ax.set(xlim=(50, 85), ylim=(3.00, 3.6))
    
    
    sns.plt.title('MSD and ADHDp_T Correlation: {0}' .format(ROI), size = 21)
    
    
    t, s = (pearsonr(adhdp_t, msd_array_adhd))
    
    
    sns.regplot(x="ADHD", y="MSD", robust = True, data = d, ci = None, scatter_kws = {'color':'red'}, line_kws = {'color':'blue'})
        
    
    sns.plt.ylabel("Mean Squared Displacement", size = 16)
    sns.plt.xlabel("ADHDp_T", size = 16)
    
        
    blue_line = mpatches.Patch(color = 'blue', label = 'R = {} and p = {}' .format(t,s))
    plt.legend(handles = [blue_line], prop = {'size': 12})
    
        
    plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/correlation_graphs/correlation_ADHDp_T_msd_{0}.png' .format(roi), bbox_inches = 'tight')
        
        
    sns.plt.show()