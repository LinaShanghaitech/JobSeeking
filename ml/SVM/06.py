import numpy as np
from sklearn.svm import SVC

# SVM
x, y = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],[]
for sample in open("credit_card_clients.txt", "r"):
    aaa,_x1, _x2, _x3, _x4, _x5, _x6,  _x7, _x8, _x9, _x10, _x11, _x12,_x13,_x14,_x15,_x16,_x17,_x18,_x19,_x20,_x21,_x22,_x23,_y = sample.split("	")
    x[0].append(int(_x1))
    x[1].append(int(_x2))
    x[2].append(int(_x3))
    x[3].append(int(_x4))
    x[4].append(int(_x5))
    x[5].append(int(_x6))
    x[6].append(int(_x7))
    x[7].append(int(_x8))
    x[8].append(int(_x9))
    x[9].append(int(_x10))
    x[10].append(int(_x11))
    x[11].append(int(_x12))
    x[12].append(int(_x13))
    x[13].append(int(_x14))
    x[14].append(int(_x15))
    x[15].append(int(_x16))
    x[16].append(int(_x17))
    x[17].append(int(_x18))
    x[18].append(int(_x19))
    x[19].append(int(_x20))
    x[20].append(int(_x21))
    x[21].append(int(_x22))
    x[22].append(int(_x23))
    y.append(int(_y))
# print(x)
x[0], x[1], x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],x[17],x[18],x[19],x[20],x[21],x[22],y = np.array(x[0]), np.array(x[1]), np.array(x[2]), np.array(x[3]), np.array(x[4]), np.array(x[5]), np.array(x[6]), np.array(x[7]), np.array(x[8]), np.array(x[9]), np.array(x[10]),  np.array(x[11]), np.array(x[12]), np.array(x[13]), np.array(x[14]), np.array(x[15]), np.array(x[16]), np.array(x[17]), np.array(x[18]), np.array(x[19]), np.array(x[20]), np.array(x[21]), np.array(x[22]),np.array(y) # 转化为Numpy数组待处理
# 记录下标准值供测试使用
mean ,std= [],[]
for i in range(len(x)):
    mean.append(x[i].mean())
    std.append(x[i].std())
x[0] = (x[0] - x[0].mean()) / x[0].std()  # 标准化，Mean表示取均值，std()为标准差，var()是方差
x[1] = (x[1] - x[1].mean()) / x[1].std()
x[2] = (x[2] - x[2].mean()) / x[2].std()
x[3] = (x[3] - x[3].mean()) / x[3].std()
x[4] = (x[4] - x[4].mean()) / x[4].std()
x[5] = (x[5] - x[5].mean()) / x[5].std()
x[6] = (x[6] - x[6].mean()) / x[6].std()
x[7] = (x[7] - x[7].mean()) / x[7].std()
x[8] = (x[8] - x[8].mean()) / x[8].std()
x[9] = (x[9] - x[9].mean()) / x[9].std()
x[10] = (x[10] - x[10].mean()) / x[10].std()
x[11] = (x[11] - x[11].mean()) / x[11].std()
x[12] = (x[12] - x[12].mean()) / x[12].std()
x[13] = (x[13] - x[13].mean()) / x[13].std()
x[14] = (x[14] - x[14].mean()) / x[14].std()
x[15] = (x[15] - x[15].mean()) / x[15].std()
x[16] = (x[16] - x[16].mean()) / x[16].std()
x[17] = (x[17] - x[17].mean()) / x[17].std()
x[18] = (x[18] - x[18].mean()) / x[18].std()
x[19] = (x[19] - x[19].mean()) / x[19].std()
x[20] = (x[20] - x[20].mean()) / x[20].std()
x[21] = (x[21] - x[21].mean()) / x[21].std()
x[22] = (x[22] - x[22].mean()) / x[22].std()

x = np.array(x).T   # 输入的数据是一行对应一组数据，对应23个数据，23个特征，共4000多个数据，4000多行
y = np.array(y)
clf = SVC() # 核心代码，定义函数，可以带参数，这里全部用默认
clf.fit(x,y)    # 核心训练函数，注意x,y进入的格式

# 获取测试集
x, y = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],[]
for sample in open("credit_card_test.txt", "r"):
    aaa,_x1, _x2, _x3, _x4, _x5, _x6,  _x7, _x8, _x9, _x10, _x11, _x12,_x13,_x14,_x15,_x16,_x17,_x18,_x19,_x20,_x21,_x22,_x23,_y = sample.split("	")
    x[0].append(int(_x1))
    x[1].append(int(_x2))
    x[2].append(int(_x3))
    x[3].append(int(_x4))
    x[4].append(int(_x5))
    x[5].append(int(_x6))
    x[6].append(int(_x7))
    x[7].append(int(_x8))
    x[8].append(int(_x9))
    x[9].append(int(_x10))
    x[10].append(int(_x11))
    x[11].append(int(_x12))
    x[12].append(int(_x13))
    x[13].append(int(_x14))
    x[14].append(int(_x15))
    x[15].append(int(_x16))
    x[16].append(int(_x17))
    x[17].append(int(_x18))
    x[18].append(int(_x19))
    x[19].append(int(_x20))
    x[20].append(int(_x21))
    x[21].append(int(_x22))
    x[22].append(int(_x23))
    y.append(int(_y))
x = np.array(x).T
y = np.array(y)

y_equal_1_right = 0     # 正确值是y=1时正确的个数
y_equal_1_wrong = 0     # 正确值是y=1时错误的个数
y_equal_0_right = 0     # 正确值是y=0时正确的个数
y_equal_0_wrong = 0     # 正确值是y=0时错误的个数
logis_line = 0.1
for i in range(len(x)):
    if y[i] == 1:
        if clf.predict([(x[i]-mean)/std]) ==1:  # 预测函数，要注意clf.predict([[]])里面都要有两层[]
            y_equal_1_right+=1
        else:
            y_equal_1_wrong+=1
    else:
        if clf.predict([(x[i]-mean)/std])==0:   # 预测
            y_equal_0_right+=1
        else:
            y_equal_0_wrong+=1

print("正确答案y=1时，正确的个数："+str(y_equal_1_right)+"，错误的个数："+str(y_equal_1_wrong)+"，正确率："+str(y_equal_1_right/(y_equal_1_right+y_equal_1_wrong)))
print("正确答案y=0时，正确的个数："+str(y_equal_0_right)+"，错误的个数："+str(y_equal_0_wrong)+"，正确率："+str(y_equal_0_right/(y_equal_0_right+y_equal_0_wrong)))
print("总计正确："+str(y_equal_0_right+y_equal_1_right)+"，错误："+str(y_equal_0_wrong+y_equal_1_wrong)+"，正确率："+str((y_equal_0_right+y_equal_1_right)/(y_equal_0_right+y_equal_0_wrong+y_equal_1_right+y_equal_1_wrong)))
