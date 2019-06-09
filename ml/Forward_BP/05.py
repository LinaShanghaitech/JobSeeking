# _*_ coding: utf-8 _*_

import numpy as np


def tanh(x):
    return np.tanh(x)


def tanh_derivative(x):
    return 1 - np.tanh(x) * np.tanh(x)


# sigmod函数
def logistic(x):
    return 1 / (1 + np.exp(-x))


# sigmod函数的导数
def logistic_derivative(x):
    return logistic(x) * (1 - logistic(x))


class NeuralNetwork:
    def __init__(self, layers, activation='tanh'):
        """
               神经网络算法构造函数
               :param layers: 神经元层数,为一个List,如[3,4,1]表示输入层3个神经元，第一个隐藏层4个，输出层一个神经元
               :param activation: 激活函数
               :return:none
        """
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_derivative
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_derivative

        # 随机产生权重值，也称为参数，即θ矩阵
        self.weights = []
        # 初始化权重（随机）
        for i in range(1, len(layers) - 1):  # 不算输入层，循环
            self.weights.append((2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1) * 0.001)
        self.weights.append((2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1) * 0.001)
        # print("初始化时权重矩阵:" + str(self.weights))

    def fit(self, x, y, learning_rate=0.2, epochs=20000):
        """
        训练神经网络
        :param x: 数据集,输入1000×23的数据集，表示特征数为23个，数据数量为1000
        :param y: 分类标记
        :param learning_rate: 学习率（默认0.2）
        :param epochs: 训练次数（最大循环次数，默认20000）
        :return: none
        """
        x = np.atleast_2d(x) # 令x至少为2维
        temp = np.ones([x.shape[0], x.shape[1] + 1])  # 生成全是1的矩阵，但是多一个偏置项
        temp[:, 0:-1] = x # 将数据项前加偏置项
        x = temp
        y = np.array(y)

        for k in range(epochs):  # 循环epochs次
            i = np.random.randint(x.shape[0])  # 随机产生一个数，对应行号，即数据集编号
            a = [x[i]]  # 抽出这行的数据集

            # 迭代将输出数据更新在a的最后一行
            for l in range(len(self.weights)):
                a.append(self.activation(np.dot(a[l], self.weights[l])))
            # print(a)

            # 减去最后更新的数据，得到误差
            error = a[-1] - y[i]    # 误差，相当于δ
            deltas = [error * self.activation_deriv(a[-1])]
            # print(error)
            # print("deltas:"+str(deltas))

            # 求梯度
            for l in range(len(a) - 2, 0, -1):
                deltas.append(deltas[-1].dot(self.weights[l].T) * self.activation_deriv(a[l]))
            # print("-----------------------------------")
            # print(deltas)
            # 反向排序
            deltas.reverse()
            # print("-----------------------------------")
            # print(deltas)
            # print("-----------------------------------")
            # 梯度下降法更新权值
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] -= learning_rate * layer.T.dot(delta)
        # print(self.weights)

    def predict(self, x ):
        x = np.array(x)
        temp = np.ones(x.shape[0] + 1)
        temp[0:-1] = x
        a = temp
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        # print("预测值："+str(a)+"实际值："+str(y))
        return a

# ------------------------------------------------
# 以下都是数据处理
# ------------------------------------------------
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
nn = NeuralNetwork([23, 46, 1], 'logistic') # 若要改变神经网络层数在此改变即可，如[23,46,46,1]表示再添加一层46神经元的隐藏层，但是添加了之后得到的最终正确率依然只有80%左右
y = np.array(y)
nn.fit(x, y)


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
for i in range(len(x)):
    if y[i] == 1:
        if nn.predict((x[i]-mean)/std) >0.5:
            y_equal_1_right+=1
        else:
            y_equal_1_wrong+=1
    else:
        if nn.predict((x[i]-mean)/std)<0.5:
            y_equal_0_right+=1
        else:
            y_equal_0_wrong+=1

print("正确答案y=1时，正确的个数："+str(y_equal_1_right)+"，错误的个数："+str(y_equal_1_wrong)+"正确率："+str(y_equal_1_right/(y_equal_1_right+y_equal_1_wrong)))
print("正确答案y=0时，正确的个数："+str(y_equal_0_right)+"，错误的个数："+str(y_equal_0_wrong)+"正确率："+str(y_equal_0_right/(y_equal_0_right+y_equal_0_wrong)))
print("总计："+str(y_equal_0_right+y_equal_1_right)+"，错误的个数："+str(y_equal_0_wrong+y_equal_1_wrong)+"正确率："+str((y_equal_0_right+y_equal_1_right)/(y_equal_0_right+y_equal_0_wrong+y_equal_1_right+y_equal_1_wrong)))