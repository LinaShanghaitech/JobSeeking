import numpy as np


# 梯度下降求向量θ
def getθ(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, y, α):
    θ0 ,θ1,θ2,θ3,θ4,θ5,θ6,θ7,θ8,θ9,θ10,θ11 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    m = len(x1)
    for i in range(1500): # 循环次数达到1500次及以上后与正规方程求解相差无几
        sum=0
        for j in range(m):
            sum += (θ0+θ1*x1[j]+θ2*x2[j]+θ3*x3[j]+θ4*x4[j]+θ5*x5[j]+θ6*x6[j]+θ7*x7[j]+θ8*x8[j]+θ9*x9[j]+θ10*x10[j]+θ11*x11[j]-y[j])
        θ0 -= α/m*sum
        sum = 0
        for j in range(m):
            sum += ((θ0+θ1*x1[j]+θ2*x2[j]+θ3*x3[j]+θ4*x4[j]+θ5*x5[j]+θ6*x6[j]+θ7*x7[j]+θ8*x8[j]+θ9*x9[j]+θ10*x10[j]+θ11*x11[j]-y[j])*x1[j])
        θ1 -= α/m*sum
        sum = 0
        for j in range(m):
            sum += ((θ0 + θ1 * x1[j] + θ2 * x2[j] + θ3 * x3[j] + θ4 * x4[j] + θ5 * x5[j] + θ6 * x6[j] + θ7 * x7[j] + θ8 * x8[j] + θ9 * x9[j] + θ10 * x10[j] + θ11 * x11[j] - y[j]) * x2[j])
        θ2 -= α / m * sum
        sum = 0
        for j in range(m):
            sum += ((θ0 + θ1 * x1[j] + θ2 * x2[j] + θ3 * x3[j] + θ4 * x4[j] + θ5 * x5[j] + θ6 * x6[j] + θ7 * x7[j] + θ8 *x8[j] + θ9 * x9[j] + θ10 * x10[j] + θ11 * x11[j] - y[j]) * x3[j])
        θ3 -= α / m * sum
        sum = 0
        for j in range(m):
            sum += ((θ0 + θ1 * x1[j] + θ2 * x2[j] + θ3 * x3[j] + θ4 * x4[j] + θ5 * x5[j] + θ6 * x6[j] + θ7 * x7[j] + θ8 *x8[j] + θ9 * x9[j] + θ10 * x10[j] + θ11 * x11[j] - y[j]) * x4[j])
        θ4 -= α / m * sum
        sum = 0
        for j in range(m):
            sum += ((θ0 + θ1 * x1[j] + θ2 * x2[j] + θ3 * x3[j] + θ4 * x4[j] + θ5 * x5[j] + θ6 * x6[j] + θ7 * x7[j] + θ8 *x8[j] + θ9 * x9[j] + θ10 * x10[j] + θ11 * x11[j] - y[j]) * x5[j])
        θ5 -= α / m * sum
        sum = 0
        for j in range(m):
            sum += ((θ0 + θ1 * x1[j] + θ2 * x2[j] + θ3 * x3[j] + θ4 * x4[j] + θ5 * x5[j] + θ6 * x6[j] + θ7 * x7[j] + θ8 *x8[j] + θ9 * x9[j] + θ10 * x10[j] + θ11 * x11[j] - y[j]) * x6[j])
        θ6 -= α / m * sum
        for j in range(m):
            sum += ((θ0 + θ1 * x1[j] + θ2 * x2[j] + θ3 * x3[j] + θ4 * x4[j] + θ5 * x5[j] + θ6 * x6[j] + θ7 * x7[j] + θ8 *x8[j] + θ9 * x9[j] + θ10 * x10[j] + θ11 * x11[j] - y[j]) * x7[j])
        θ7 -= α / m * sum
        for j in range(m):
            sum += ((θ0 + θ1 * x1[j] + θ2 * x2[j] + θ3 * x3[j] + θ4 * x4[j] + θ5 * x5[j] + θ6 * x6[j] + θ7 * x7[j] + θ8 *x8[j] + θ9 * x9[j] + θ10 * x10[j] + θ11 * x11[j] - y[j]) * x8[j])
        θ8 -= α / m * sum
        for j in range(m):
            sum += ((θ0 + θ1 * x1[j] + θ2 * x2[j] + θ3 * x3[j] + θ4 * x4[j] + θ5 * x5[j] + θ6 * x6[j] + θ7 * x7[j] + θ8 *x8[j] + θ9 * x9[j] + θ10 * x10[j] + θ11 * x11[j] - y[j]) * x9[j])
        θ9 -= α / m * sum
        for j in range(m):
            sum += ((θ0 + θ1 * x1[j] + θ2 * x2[j] + θ3 * x3[j] + θ4 * x4[j] + θ5 * x5[j] + θ6 * x6[j] + θ7 * x7[j] + θ8 *x8[j] + θ9 * x9[j] + θ10 * x10[j] + θ11 * x11[j] - y[j]) * x10[j])
        θ10 -= α / m * sum
        for j in range(m):
            sum += ((θ0 + θ1 * x1[j] + θ2 * x2[j] + θ3 * x3[j] + θ4 * x4[j] + θ5 * x5[j] + θ6 * x6[j] + θ7 * x7[j] + θ8 *x8[j] + θ9 * x9[j] + θ10 * x10[j] + θ11 * x11[j] - y[j]) * x11[j])
        θ11 -= α / m * sum
    return [θ0 ,θ1,θ2,θ3,θ4,θ5,θ6,θ7,θ8,θ9,θ10,θ11 ]

# 正规方程求向量θ
def getθ2(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, y):
    x_list = []
    for i in range(len(x1)):
        x_list.append([1, x1[i], x2[i], x3[i], x4[i], x5[i], x6[i], x7[i], x8[i], x9[i], x10[i], x11[i]])
    x_matrix = np.matrix(x_list)
    y_matrix = np.matrix(y)
    θ = ((x_matrix.T*x_matrix).I*x_matrix.T*(y_matrix.T)).tolist()  # matrix.T求转置，matrix.I求逆，*矩阵相乘,tolist()转为列表
    re_list = []
    for i in range(len(θ)):
        re_list.append(θ[i][0])
    return re_list

x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, y = [],[],[],[],[],[],[],[],[],[],[],[]
for sample in open("wine.txt", "r"):
    _x1, _x2, _x3, _x4, _x5, _x6,  _x7, _x8, _x9, _x10, _x11, _y = sample.split(";")
    x1.append(float(_x1))
    x2.append(float(_x2))
    x3.append(float(_x3))
    x4.append(float(_x4))
    x5.append(float(_x5))
    x6.append(float(_x6))
    x7.append(float(_x7))
    x8.append(float(_x8))
    x9.append(float(_x9))
    x10.append(float(_x10))
    x11.append(float(_x11))
    y.append(float(_y))
x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, y = np.array(x1), np.array(x2), np.array(x3), np.array(x4), np.array(x5), np.array(x6), np.array(x7), np.array(x8), np.array(x9), np.array(x10), np.array(x11), np.array(y) # 转化为Numpy数组待处理
x1 = (x1 - x1.mean()) / x1.std()    # 标准化，Mean表示取均值，std()为标准差，var()是方差
x2 = (x2 - x2.mean()) / x2.std()
x3 = (x3 - x3.mean()) / x3.std()
x4 = (x4 - x4.mean()) / x4.std()
x5 = (x5 - x5.mean()) / x5.std()
x6 = (x6 - x6.mean()) / x6.std()
x7 = (x7 - x7.mean()) / x7.std()
x8 = (x8 - x8.mean()) / x8.std()
x9 = (x9 - x9.mean()) / x9.std()
x10 = (x10 - x10.mean()) / x10.std()
x11 = (x11 - x11.mean()) / x11.std()

list = getθ(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, y ,0.2)
print("梯度下降得到："+str(list))

list2 = getθ2(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, y)
print("正规方程得到："+str(list2))

