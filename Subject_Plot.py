''''
Visually Induced Motion Sickness Dataset
Plot the figure of 2D PCA 
Code Author: Xi Chen
Created on : 2020/12/05
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Algorithm.core import datapreprocessing
from sklearn.decomposition import PCA

data1 = pd.read_csv(r'F:\Machine_Learning\Transductive_Transfer_Learning\subject1.csv')
data2 = pd.read_csv(r'F:\Machine_Learning\Transductive_Transfer_Learning\subject2.csv')
data3 = pd.read_csv(r'F:\Machine_Learning\Transductive_Transfer_Learning\subject3.csv')
data4 = pd.read_csv(r'F:\Machine_Learning\Transductive_Transfer_Learning\subject4.csv')
data5 = pd.read_csv(r'F:\Machine_Learning\Transductive_Transfer_Learning\subject5.csv')
data6 = pd.read_csv(r'F:\Machine_Learning\Transductive_Transfer_Learning\subject6.csv')
data7 = pd.read_csv(r'F:\Machine_Learning\Transductive_Transfer_Learning\subject7.csv')
data8 = pd.read_csv(r'F:\Machine_Learning\Transductive_Transfer_Learning\subject8.csv')

dataS1 = data1.iloc[:,1:-3].values
labelS1 = data1.iloc[:,-2].values

dataS2 = data2.iloc[:,1:-3].values
labelS2 = data2.iloc[:,-2].values

dataS3 = data3.iloc[:,1:-3].values
labelS3 = data3.iloc[:,-2].values

dataS4 = data4.iloc[:,1:-3].values
labelS4 = data4.iloc[:,-2].values

dataS5 = data5.iloc[:,1:-3].values
labelS5 = data5.iloc[:,-2].values

dataS6 = data6.iloc[:,1:-3].values
labelS6 = data6.iloc[:,-2].values

dataS7 = data7.iloc[:,1:-3].values
labelS7 = data7.iloc[:,-2].values

dataS8 = data8.iloc[:,1:-3].values
labelS8 = data8.iloc[:,-2].values

plt.figure(figsize=(12,18))
plt.subplots_adjust(wspace = 0.35)
plt.subplots_adjust(hspace=0.3)

plt.subplot(2,4,1)
scaler1 = PCA(n_components=2)
dataS1 = scaler1.fit_transform(dataS1)
index_1 = np.where(labelS1==0)
plt.scatter(dataS1[index_1,0],dataS1[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
index_2 =np.where(labelS1==1)
plt.scatter(dataS1[index_2,0],dataS1[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
plt.xlabel('PC1',fontsize=12)
plt.ylabel('PC2',fontsize=12)
plt.title('Subject1',fontsize=13)

plt.subplot(2,4,2)
scaler2 = PCA(n_components=2)
dataS2 = scaler2.fit_transform(dataS2)
index_1 = np.where(labelS2==0)
plt.scatter(dataS2[index_1,0],dataS2[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
index_2 =np.where(labelS2==1)
plt.scatter(dataS2[index_2,0],dataS2[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
plt.xlabel('PC1',fontsize=12)
plt.ylabel('PC2',fontsize=12)
plt.title('Subject2',fontsize=13)

plt.subplot(2,4,3)
scaler3 = PCA(n_components=2)
dataS3 = scaler3.fit_transform(dataS3)
index_1 = np.where(labelS3==0)
plt.scatter(dataS3[index_1,0],dataS3[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
index_2 =np.where(labelS3==1)
plt.scatter(dataS3[index_2,0],dataS3[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
plt.xlabel('PC1',fontsize=12)
plt.ylabel('PC2',fontsize=12)
plt.title('Subject3',fontsize=13)

plt.subplot(2,4,4)
scaler4 = PCA(n_components=2)
dataS4 = scaler4.fit_transform(dataS4)
index_1 = np.where(labelS4==0)
plt.scatter(dataS4[index_1,0],dataS4[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
index_2 =np.where(labelS4==1)
plt.scatter(dataS4[index_2,0],dataS4[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
plt.xlabel('PC1',fontsize=12)
plt.ylabel('PC2',fontsize=12)
plt.title('Subject4',fontsize=13)
plt.legend(bbox_to_anchor=(1.57,1.03),loc = 'upper right',fontsize=15)

plt.subplot(2,4,5)
scaler5 = PCA(n_components=2)
dataS5 = scaler5.fit_transform(dataS5)
index_1 = np.where(labelS5==0)
plt.scatter(dataS5[index_1,0],dataS5[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
index_2 =np.where(labelS5==1)
plt.scatter(dataS5[index_2,0],dataS5[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
plt.xlabel('PC1',fontsize=12)
plt.ylabel('PC2',fontsize=12)
plt.title('Subject5',fontsize=13)

plt.subplot(2,4,6)
scaler6 = PCA(n_components=2)
dataS6 = scaler6.fit_transform(dataS6)
index_1 = np.where(labelS6==0)
plt.scatter(dataS6[index_1,0],dataS6[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
index_2 =np.where(labelS6==1)
plt.scatter(dataS6[index_2,0],dataS6[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
plt.xlabel('PC1',fontsize=12)
plt.ylabel('PC2',fontsize=12)
plt.title('Subject6',fontsize=13)

plt.subplot(2,4,7)
scaler7 = PCA(n_components=2)
dataS7 = scaler7.fit_transform(dataS7)
index_1 = np.where(labelS7==0)
plt.scatter(dataS7[index_1,0],dataS7[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
index_2 =np.where(labelS7==1)
plt.scatter(dataS7[index_2,0],dataS7[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
plt.xlabel('PC1',fontsize=12)
plt.ylabel('PC2',fontsize=12)
plt.title('Subject7',fontsize=13)

plt.subplot(2,4,8)
scaler8 = PCA(n_components=2)
dataS8 = scaler8.fit_transform(dataS8)
index_1 = np.where(labelS8==0)
plt.scatter(dataS8[index_1,0],dataS8[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
index_2 =np.where(labelS8==1)
plt.scatter(dataS8[index_2,0],dataS8[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
plt.xlabel('PC1',fontsize=12)
plt.ylabel('PC2',fontsize=12)
plt.title('Subject8',fontsize=13)
plt.show()
# index_3 =np.where(label1==3)
# plt.scatter(data1[index_3,0],data1[index_3,1],marker='+',color = 'g',label = 'Class 3',s = 15)
# index_4 =np.where(label1==4)
# plt.scatter(data1[index_4,0],data1[index_4,1],marker='*',color = 'c',label = 'Class 4',s = 15)
# index_5 =np.where(label1==5)
# plt.scatter(data1[index_5,0],data1[index_5,1],marker='s',color = 'grey',label = 'Class 5',s = 15)
# index_6 =np.where(label1==6)
# plt.scatter(data1[index_6,0],data1[index_6,1],marker='1',color = 'y',label = 'Class 6',s = 15)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Batch1')
#
# plt.subplot(2,5,2)
# scaler3 = PCA(n_components=2)
# data3 = scaler3.fit_transform(data3)
# index_1 = np.where(label3==1)
# plt.scatter(data3[index_1,0],data3[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
# index_2 =np.where(label3==2)
# plt.scatter(data3[index_2,0],data3[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
# index_3 =np.where(label3==3)
# plt.scatter(data3[index_3,0],data3[index_3,1],marker='+',color = 'g',label = 'Class 3',s = 15)
# index_4 =np.where(label3==4)
# plt.scatter(data3[index_4,0],data3[index_4,1],marker='*',color = 'c',label = 'Class 4',s = 15)
# index_5 =np.where(label3==5)
# plt.scatter(data3[index_5,0],data3[index_5,1],marker='s',color = 'grey',label = 'Class 5',s = 15)
# # index_6 =np.where(label3==6)
# # plt.scatter(data2[index_6,0],data2[index_6,1],marker='1',color = 'y',label = 'Class 6',s = 15)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Batch3')
# # plt.xlim(-0.25,1)
# # plt.ylim(-0.2,0.6)
#
# plt.subplot(2,5,3)
# scaler5 = PCA(n_components=2)
# data5 = scaler5.fit_transform(data5)
# index_1 = np.where(label5==1)
# plt.scatter(data5[index_1,0],data5[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
# index_2 =np.where(label5==2)
# plt.scatter(data5[index_2,0],data5[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
# index_3 =np.where(label5==3)
# plt.scatter(data5[index_3,0],data5[index_3,1],marker='+',color = 'g',label = 'Class 3',s = 15)
# index_4 =np.where(label5==4)
# plt.scatter(data5[index_4,0],data5[index_4,1],marker='*',color = 'c',label = 'Class 4',s = 15)
# index_5 =np.where(label5==5)
# plt.scatter(data5[index_5,0],data5[index_5,1],marker='s',color = 'grey',label = 'Class 5',s = 15)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Batch5')
#
# plt.subplot(2,5,4)
# scaler7 = PCA(n_components=2)
# data7 = scaler7.fit_transform(data7)
# index_1 = np.where(label7==1)
# plt.scatter(data7[index_1,0],data7[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
# index_2 =np.where(label7==2)
# plt.scatter(data7[index_2,0],data7[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
# index_3 =np.where(label7==3)
# plt.scatter(data7[index_3,0],data7[index_3,1],marker='+',color = 'g',label = 'Class 3',s = 15)
# index_4 =np.where(label7==4)
# plt.scatter(data7[index_4,0],data7[index_4,1],marker='*',color = 'c',label = 'Class 4',s = 15)
# index_5 =np.where(label7==5)
# plt.scatter(data7[index_5,0],data7[index_5,1],marker='s',color = 'grey',label = 'Class 5',s = 15)
# index_6 =np.where(label7==6)
# plt.scatter(data7[index_6,0],data7[index_6,1],marker='1',color = 'y',label = 'Class 6',s = 15)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Batch7')
#
# plt.subplot(2,5,5)
# scaler9 = PCA(n_components=2)
# data9 = scaler9.fit_transform(data9)
# index_1 = np.where(label9==1)
# plt.scatter(data9[index_1,0],data9[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
# index_2 =np.where(label9==2)
# plt.scatter(data9[index_2,0],data9[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
# index_3 =np.where(label9==3)
# plt.scatter(data9[index_3,0],data9[index_3,1],marker='+',color = 'g',label = 'Class 3',s = 15)
# index_4 =np.where(label9==4)
# plt.scatter(data9[index_4,0],data9[index_4,1],marker='*',color = 'c',label = 'Class 4',s = 15)
# index_5 =np.where(label9==5)
# plt.scatter(data9[index_5,0],data9[index_5,1],marker='s',color = 'grey',label = 'Class 5',s = 15)
# index_6 =np.where(label9==6)
# plt.scatter(data9[index_6,0],data9[index_6,1],marker='1',color = 'y',label = 'Class 6',s = 15)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Batch9')
# plt.legend(bbox_to_anchor=(1.71,1.03),loc = 'upper right',fontsize=15)
#
# plt.subplot(2,5,6)
# scaler2 = PCA(n_components=2)
# data2 = scaler2.fit_transform(data2)
# index_1 = np.where(label2==1)
# plt.scatter(data2[index_1,0],data2[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
# index_2 =np.where(label2==2)
# plt.scatter(data2[index_2,0],data2[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
# index_3 =np.where(label2==3)
# plt.scatter(data2[index_3,0],data2[index_3,1],marker='+',color = 'g',label = 'Class 3',s = 15)
# index_4 =np.where(label2==4)
# plt.scatter(data2[index_4,0],data2[index_4,1],marker='*',color = 'c',label = 'Class 4',s = 15)
# index_5 =np.where(label2==5)
# plt.scatter(data2[index_5,0],data2[index_5,1],marker='s',color = 'grey',label = 'Class 5',s = 15)
# index_6 =np.where(label2==6)
# plt.scatter(data2[index_6,0],data2[index_6,1],marker='1',color = 'y',label = 'Class 6',s = 15)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Batch2')
# plt.xlim(-0.25,1)
# plt.ylim(-0.2,0.6)
#
# plt.subplot(2,5,7)
# scaler4 = PCA(n_components=2)
# data4 = scaler4.fit_transform(data4)
# index_1 = np.where(label4==1)
# plt.scatter(data4[index_1,0],data4[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
# index_2 =np.where(label4==2)
# plt.scatter(data4[index_2,0],data4[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
# index_3 =np.where(label4==3)
# plt.scatter(data4[index_3,0],data4[index_3,1],marker='+',color = 'g',label = 'Class 3',s = 15)
# index_4 =np.where(label4==4)
# plt.scatter(data4[index_4,0],data4[index_4,1],marker='*',color = 'c',label = 'Class 4',s = 15)
# index_5 =np.where(label4==5)
# plt.scatter(data4[index_5,0],data4[index_5,1],marker='s',color = 'grey',label = 'Class 5',s = 15)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Batch4')
#
# plt.subplot(2,5,8)
# scaler6 = PCA(n_components=2)
# data6 = scaler6.fit_transform(data6)
# index_1 = np.where(label6==1)
# plt.scatter(data6[index_1,0],data6[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
# index_2 =np.where(label6==2)
# plt.scatter(data6[index_2,0],data6[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
# index_3 =np.where(label6==3)
# plt.scatter(data6[index_3,0],data6[index_3,1],marker='+',color = 'g',label = 'Class 3',s = 15)
# index_4 =np.where(label6==4)
# plt.scatter(data6[index_4,0],data6[index_4,1],marker='*',color = 'c',label = 'Class 4',s = 15)
# index_5 =np.where(label6==5)
# plt.scatter(data6[index_5,0],data6[index_5,1],marker='s',color = 'grey',label = 'Class 5',s = 15)
# index_6 =np.where(label6==6)
# plt.scatter(data6[index_6,0],data6[index_6,1],marker='1',color = 'y',label = 'Class 6',s = 15)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Batch6')
#
# plt.subplot(2,5,9)
# scaler8 = PCA(n_components=2)
# data8 = scaler8.fit_transform(data8)
# index_1 = np.where(label8==1)
# plt.scatter(data8[index_1,0],data8[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
# index_2 =np.where(label8==2)
# plt.scatter(data8[index_2,0],data8[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
# index_3 =np.where(label8==3)
# plt.scatter(data8[index_3,0],data8[index_3,1],marker='+',color = 'g',label = 'Class 3',s = 15)
# index_4 =np.where(label8==4)
# plt.scatter(data8[index_4,0],data8[index_4,1],marker='*',color = 'c',label = 'Class 4',s = 15)
# index_5 =np.where(label8==5)
# plt.scatter(data8[index_5,0],data8[index_5,1],marker='s',color = 'grey',label = 'Class 5',s = 15)
# index_6 =np.where(label8==6)
# plt.scatter(data8[index_6,0],data8[index_6,1],marker='1',color = 'y',label = 'Class 6',s = 15)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Batch8')
#
# plt.subplot(2,5,10)
# scaler10 = PCA(n_components=2)
# data10 = scaler10.fit_transform(data10)
# index_1 = np.where(label10==1)
# plt.scatter(data10[index_1,0],data10[index_1,1],marker='x',color = 'r',label = 'Class 1',s = 15)
# index_2 =np.where(label10==2)
# plt.scatter(data10[index_2,0],data10[index_2,1],marker='o',color = 'b',label = 'Class 2',s = 15)
# index_3 =np.where(label10==3)
# plt.scatter(data10[index_3,0],data10[index_3,1],marker='+',color = 'g',label = 'Class 3',s = 15)
# index_4 =np.where(label10==4)
# plt.scatter(data10[index_4,0],data10[index_4,1],marker='*',color = 'c',label = 'Class 4',s = 15)
# index_5 =np.where(label10==5)
# plt.scatter(data10[index_5,0],data10[index_5,1],marker='s',color = 'grey',label = 'Class 5',s = 15)
# index_6 =np.where(label10==6)
# plt.scatter(data10[index_6,0],data10[index_6,1],marker='1',color = 'y',label = 'Class 6',s = 15)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.title('Batch10')
#
# plt.show()



