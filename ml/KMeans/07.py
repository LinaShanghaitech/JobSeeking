import numpy as np
import matplotlib.pyplot as plt
import random

# 求二范数方
def get2(x1,x2,y1,y2):
    return pow(x1-y1,2)*pow(x2-y2,2)

# K-means,这里让k=2吧
def k_means(x1,x2):
    c1,c2 = random.randint(0,99),random.randint(0,99)
    len_x = len(x1)
    center1,center2= [x1[c1],x2[c1]],[x1[c2],x2[c2]]    # 聚类中心
    for iii in range(1000):
        center1_cluster, center2_cluster = [], []# 属于不同聚类中心的集合
        for i in range(len_x):
            if get2(center1[0],center1[1],x1[i],x2[i]) > get2(center2[0],center2[1],x1[i],x2[i]):
                center2_cluster.append(i)
            else:center1_cluster.append(i)
        sum1,sum2=0,0
        for i in range(len(center1_cluster)):
            sum1+=x1[center1_cluster[i]]
            sum2+=x2[center1_cluster[i]]
        center1[0]=sum1/len(center1_cluster)
        center1[1]=sum2/len(center1_cluster)
        sum1, sum2 = 0, 0
        for i in range(len(center2_cluster)):
            sum1 += x1[center2_cluster[i]]
            sum2 += x2[center2_cluster[i]]
        center2[0] = sum1 / len(center2_cluster)
        center2[1] = sum2 / len(center2_cluster)
    return [center1_cluster,center2_cluster,center1,center2]    # 转为list传回，center1_cluster里存的是Index,在把中心传回绘制

x1, x2 = [],[]
for sample in open("census1990_train.txt", "r"):
    # 原始数据太多需要占位
    a1,_x1,a2,a3,a4,a5,_x2,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67 = sample.split(",")
    x1.append(float(_x1))
    x2.append(float(_x2))
x1, y2 = np.array(x1), np.array(x2) # 转化为Numpy数组待处理
plt.figure()
plt.xlabel("age(10)")
plt.ylabel("class")
re_list = k_means(x1,x2)
# 第一簇绘制
x1_1,x1_2=[],[]
for i in range(len(re_list[0])):
    x1_1.append(x1[re_list[0][i]])
    x1_2.append(x2[re_list[0][i]])
plt.scatter(x1_1, x1_2, c="r", s=6) #s是点的大小,c是颜色‘b’blue‘g’green‘r’red‘c’cyan‘m’magenta‘y’yellow‘k’black‘w’white
plt.scatter(re_list[2][0], re_list[2][1], c="r", s=36)
# 第一簇绘制
x2_1,x2_2=[],[]
for i in range(len(re_list[1])):
    x2_1.append(x1[re_list[1][i]])
    x2_2.append(x2[re_list[1][i]])
plt.scatter(x2_1, x2_2, c="b", s=6)
plt.scatter(re_list[3][0], re_list[3][1], c="b", s=36)
plt.show()

