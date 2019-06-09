import numpy as np

'''逻辑回归'''
# Hθ
def getH(θ, _x):
    θx = θ[0]
    for i in range(len(_x)):
        θx += θ[i+1]*_x[i]
    if θx >= 0:
        return 1.0 / (1 + np.exp(-θx))
    else:
        return np.exp(θx) / (1 + np.exp(θx))
    # return 1/(1+np.exp(-θx))  #这样直接返回结果会导致RuntimeWarning: overflow encountered in exp

# 不带正则化的逻辑回归
def lr(x,y, α):
    θ = [0]
    for i in range(len(x)):
        θ.append(0)

    m=len(x[0])
    for ii in range(100):
        sum = 0
        for j in range(m):
            _x = []
            for jj in range(len(x)):
                _x.append(x[jj][m-1])
            sum+=(getH(θ,_x)-y[j])
        θ[0] -= α*sum/m
        for i in range(len(x)):
            sum = 0
            for j in range(m):
                _x = []
                for jj in range(len(x)):
                    _x.append(x[jj][m-1])
                sum += ((getH(θ, _x) - y[j])*x[i][j])
            θ[i] -= α * sum/m
    return θ

# 带正则化的逻辑回归
def lr_r(x,y, α):
    θ = [0]
    for i in range(len(x)):
        θ.append(0)

    m=len(x[0])
    for ii in range(100):
        sum = 0
        for j in range(m):
            _x = []
            for jj in range(len(x)):
                _x.append(x[jj][m-1])
            sum+=(getH(θ,_x)-y[j])
        θ[0] -= α*sum/m
        for i in range(len(x)):
            sum = 0
            for j in range(m):
                _x = []
                for jj in range(len(x)):
                    _x.append(x[jj][m-1])
                sum += ((getH(θ, _x) - y[j])*x[i][j])
            θ[i] = θ[i]*(1-1000*α/m) - α * sum/m # 定义惩罚项λ=1000
    return θ

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

θ=[1.0838212187817922, -0.045955968961057296, 0.2900506418097455, -0.3127799856789351, 0.137783064865873, 2.4100461504016066, 1.7189506195292905, 1.582471758324859, 1.4126993687049045, 1.3885654177918474, 1.119129407787314, -0.060791017217695656, -0.05068254473086228, -0.037071324667241855, 0.0264489989904585, -0.005852121886165663, 0.014332012489780702, -0.7075552647477504, -0.6615940786053858, -0.2321243465015359, -0.5072334204862982, -0.27004565251264956, -0.34783918371064676, 0]
# lr(x,y,0.2)  #本来应当调用这一行计算不带正则化的逻辑回归的结果，但是为了加快运算速度，之前计算过该值，且这部分程序没变化的情况下直接调用List运行更快
θ1= lr_r(x,y,0.2)

# 测试不带正则化的逻辑回归效果
def test(θ , test):
    sum = θ[0]
    for i in range(1, len(θ)):
        sum += θ[i]*(test[i-1]-mean[i-1])/std[i-1]
    if sum>0:return 1
    else:return 0

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

# 测试集测试不带正则化的逻辑回归
y_equal_1_right = 0     # 正确值是y=1时正确的个数
y_equal_1_wrong = 0     # 正确值是y=1时错误的个数
y_equal_0_right = 0     # 正确值是y=0时正确的个数
y_equal_0_wrong = 0     # 正确值是y=0时错误的个数
for i in range(len(x[0])):
    lst = []
    for j in range(len(x)):
        lst.append(x[j][i])
    if y[i]==1:
        if test(θ,lst) == 1:y_equal_1_right+=1
        else:y_equal_1_wrong+=1
    elif y[i]==0:
        if test(θ,lst) == 0:y_equal_0_right+=1
        else:y_equal_0_wrong+=1

print("不带正则化的逻辑回归--正确答案y=1时，正确的个数："+str(y_equal_1_right)+"，错误的个数："+str(y_equal_1_wrong)+"正确率："+str(y_equal_1_right/(y_equal_1_right+y_equal_1_wrong)))
print("不带正则化的逻辑回归--正确答案y=0时，正确的个数："+str(y_equal_0_right)+"，错误的个数："+str(y_equal_0_wrong)+"正确率："+str(y_equal_0_right/(y_equal_0_right+y_equal_0_wrong)))

# 测试集测试带正则化的逻辑回归
y_equal_1_right = 0     # 正确值是y=1时正确的个数
y_equal_1_wrong = 0     # 正确值是y=1时错误的个数
y_equal_0_right = 0     # 正确值是y=0时正确的个数
y_equal_0_wrong = 0     # 正确值是y=0时错误的个数
for i in range(len(x[0])):
    lst = []
    for j in range(len(x)):
        lst.append(x[j][i])
    if y[i]==1:
        if test(θ1,lst) == 1:y_equal_1_right+=1
        else:y_equal_1_wrong+=1
    elif y[i]==0:
        if test(θ1,lst) == 0:y_equal_0_right+=1
        else:y_equal_0_wrong+=1

print("带正则化的逻辑回归--正确答案y=1时，正确的个数："+str(y_equal_1_right)+"，错误的个数："+str(y_equal_1_wrong)+"正确率："+str(y_equal_1_right/(y_equal_1_right+y_equal_1_wrong)))
print("带正则化的逻辑回归--正确答案y=0时，正确的个数："+str(y_equal_0_right)+"，错误的个数："+str(y_equal_0_wrong)+"正确率："+str(y_equal_0_right/(y_equal_0_right+y_equal_0_wrong)))