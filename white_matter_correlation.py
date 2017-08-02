import csv
correlation = []
with open('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/FW_MSD_correlation.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    header = 0
    i = 0
    for row in reader:
        if i > 0:
            correlation.append(row)
        else:
            header = row
        i = i + 1

"""

edit /rfanfs/pnl-zorro/projects/ADHD/Heterogenity-Final/RunHeterogeneity.m
Frontal = 1028,1027,1032,1020,1019,1018,1014,1003,1012,1024,1017,1002,1026,2028,2027,2032,2020,2019,2018,2014,2003,2012,2024,2017,2002,2026
Parietal = 1008,1029,1031,1025,1022,1023,1010,2008,2029,2031,2025,2022,2023,2010
Occipital = 1011,1013,1005,1021,2011,2013,2005,2021
Temporal = 1009,1015,1030,1033,1034,1007,1006,1016,2009,2015,2030,2033,2034,2007,2006,2016
White Matter = 3028,3027,3032,3020,3019,3018,3014,3003,3012,3024,3017,3002,3026,3011,3013,3005,3021,3008,3029,3031,3025,3022,3023,3010,3009,3015,3030,3033,3034,3007,3006,3016,4028,4027,4032,4040,4019,4018,4014,4003,4012,4024,4017,4002,4026,4011,4013,4005,4021,4008,4029,4031,4025,4022,4023,4020,4009,4015,4030,4033,4034,4007,4006,4016
Grey Matter = 1028,1027,1032,1020,1019,1018,1014,1003,1012,1024,1017,1002,1026,1011,1013,1005,1021,1008,1029,1031,1025,1022,1023,1010,1009,1015,1030,1033,1034,1007,1006,1016,2028,2027,2032,2020,2019,2018,2014,2003,2012,2024,2017,2002,2026,2011,2013,2005,2021,2008,2029,2031,2025,2022,2023,2020,2009,2015,2030,2033,2034,2007,2006,2016

"""


from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from medpy.io import load
import numpy as np
import pandas as pd
import seaborn as sns

correlation_constant = []


caselist = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case_list_temp.csv",'r+')


for line in caselist:
    casenumber = line.rstrip()


    image_data_msd, image_header_msd = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/MSD/{0}_MSD.nii' .format(casenumber))
    image_data_fw, image_header_fw = load('/rfanfs/pnl-zorro/projects/ADHD/FW1000/Fwnii/{0}_FW.nii.gz' .format(casenumber))
    image_data_fs, image_header_fs = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/freesurferINdwi/{0}_wmparc-in-bse.nii.gz" .format(casenumber))
    

    vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
    vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])
    vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
    


    white_matter = {3028,3027,3032,3020,3019,3018,3014,3003,3012,3024,3017,3002,3026,3011,3013,3005,3021,3008,3029,3031,3025,3022,3023,3010,3009,3015,3030,3033,3034,3007,3006,3016,4028,4027,4032,4040,4019,4018,4014,4003,4012,4024,4017,4002,4026,4011,4013,4005,4021,4008,4029,4031,4025,4022,4023,4020,4009,4015,4030,4033,4034,4007,4006,4016}
    
    id=[]
    for i in white_matter:
        white=(vector_fs==i)
        k=np.where(white)
        shape=vector_fw[k]
        id.append(shape)
    
    white_fw=np.concatenate((id[0:len(id)]))
    
    id1=[]
    for i in white_matter:
        white=(vector_fs==i)
        k1=np.where(white)
        shape1=vector_msd[k1]
        id1.append(shape1)
        
    white_msd=np.concatenate((id1[0:len(id1)]))
    
    
    in_l = (white_msd <= 15)
    keep = np.where(in_l)
    final_white_msd = white_msd[keep]
    final_white_fw = white_fw[keep]
    
    in_k = (final_white_msd != 0)
    keep1 = np.where(in_k)
    ultimate_white_msd = final_white_msd[keep1]
    ultimate_white_fw = final_white_fw[keep1]

    in_m = (ultimate_white_fw != 1.0)
    keep2 = np.where(in_m)
    last_white_msd = ultimate_white_msd[keep2]
    last_white_fw = ultimate_white_fw[keep2]

    
    data={'MSD': last_white_msd, 'FW': last_white_fw}
    d = pd.DataFrame(data)
    
    f, ax = plt.subplots()
       

    t, s = (pearsonr(last_white_fw, last_white_msd))
    
    sns.regplot(x="FW", y="MSD", robust = True, data = d, ci = None, scatter_kws = {'color':'red','s': 8}, line_kws = {'color':'blue'})


    plt.ylabel("White Matter Mean Square Displacement", size = 16)
    plt.xlabel("White Matter Free Water", size = 16)
    
    blue_line = mpatches.Patch(color = 'blue', label = 'R = {0}' .format(t))
    plt.legend(handles = [blue_line], prop = {'size': 14})

    plt.title(casenumber, size = 20)
    
    plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/new_graphs/White_Matter/white_msdfw_correlation_{0}.png' .format(casenumber), bbox_inches = 'tight')
    
    
    plt.show()
    
    correlation_constant.append(t)


final_csv = []
c = 0
for r in correlation:
    a = []
    print r
    first_val = r[0]
    third_val = r[2]
    
    a.append(first_val)
    a.append(correlation_constant[c])
    a.append(third_val)
    
    final_csv.append(a)
    c = c + 1



with open('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/new_graphs/white_matter_correlation.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in final_csv:
        writer.writerow(row)



caselist.close()