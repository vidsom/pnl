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


from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from medpy.io import load
import numpy as np
import seaborn as sns
import pandas as pd


correlation_constant = []


caselist = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/caselist.txt",'r+')


for line in caselist:
    casenumber = line.rstrip()
    
    
    image_data_msd, image_header_msd = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/MSD/{0}_MSD.nii' .format(casenumber))
    image_data_fw, image_header_fw = load('/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/FW/{0}_FW.nii' .format(casenumber))
    image_data_fs, image_header_fs = load("/rfanfs/pnl-zorro/projects/ADHD/MultiGaussian_NoV2016/GMM_07292017/wmparc/{0}_wmparc.nii" .format(casenumber))
    
    
    vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
    vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])
    vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
    
    
    in_l = (vector_msd <= 15)
    keep = np.where(in_l)
    final_vector_msd = vector_msd[keep]
    final_vector_fw = vector_fw[keep]
    
    in_k = (final_vector_msd != 0)
    keep1 = np.where(in_k)
    ultimate_vector_msd = final_vector_msd[keep1]
    ultimate_vector_fw = final_vector_fw[keep1]

    in_m = (ultimate_vector_fw != 1.0)
    keep2 = np.where(in_m)
    last_vector_msd = ultimate_vector_msd[keep2]
    last_vector_fw = ultimate_vector_fw[keep2]

    data={'MSD': last_vector_msd, 'FW': last_vector_fw}
    d = pd.DataFrame(data)

    f, ax = plt.subplots()    
    
    
    sns.regplot(x="FW", y="MSD", robust = True, data = d, ci = None, scatter_kws = {'color':'red','s': 8}, line_kws = {'color':'blue'})

    
    
    t, s = (pearsonr(last_vector_fw, last_vector_msd))
    
    
    plt.ylabel("Mean Square Displacement", size = 16)
    plt.xlabel("Free Water", size = 16)
    
    blue_line = mpatches.Patch(color = 'blue', label = 'R = {0}' .format(t))
    plt.legend(handles = [blue_line], prop = {'size': 13})

    plt.title(casenumber, size = 20)
    
#    plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/final_graphs/msdfw_correlation_{0}.png' .format(casenumber), bbox_inches = 'tight')
    
    
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



with open('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/final_graphs/MSD_FW_correlation.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in final_csv:
        writer.writerow(row)



caselist.close()