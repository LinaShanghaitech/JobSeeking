import numpy as np
import matplotlib.pyplot as plt

# 梯度下降求y=θ0+θ1x
def getθ(x, y, α):
    θ0 ,θ1 = 0,0
    m = len(x)
    for i in range(1000):
        sum1=0
        for j in range(m):
            sum1 += (θ0+θ1*x[j]-y[j])
        θ0 -= α/m*sum1
        sum2 = 0
        for j in range(m):
            sum2 += ((θ0+θ1*x[j]-y[j])*x[j])
        θ1 -= α/m*sum2
    return [θ0 ,θ1 ]

# 正规方程求y=θ0+θ1x
def getθ2(x, y):
    x_list = []
    for i in range(len(x)):
        x_list.append([1, x[i]])
    x_matrix = np.matrix(x_list)
    y_matrix = np.matrix(y)
    θ = ((x_matrix.T*x_matrix).I*x_matrix.T*(y_matrix.T)).tolist()  # matrix.T求转置，matrix.I求逆，*矩阵相乘,tolist()转为列表
    return [θ[0][0],θ[1][0]]

x, y = [],[]
for sample in open("prices.txt" , "r"):
    _x, _y = sample.split(",")
    x.append(float(_x))
    y.append(float(_y))
x, y = np.array(x), np.array(y) # 转化为Numpy数组待处理
x = (x - x.mean()) / x.std()    # 标准化，Mean表示取均值，std()为标准差，var()是方差

plt.figure()
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.scatter(x, y, c="g", s=6) #s是点的大小,c是颜色‘b’blue‘g’green‘r’red‘c’cyan‘m’magenta‘y’yellow‘k’black‘w’white

list = getθ(x,y,0.2)
x0 = np.linspace(-2, 4 ,100) # 在-2到4上取点绘制直线
y0 = list[0]+list[1]*x0
print("梯度下降实现：y="+str(list[0])+"+"+str(list[1])+"*x")
plt.plot(x0, y0,"g")

list2 = getθ2(x, y)
x1 = np.linspace(-2, 4 ,100) # 在-2到4上取点绘制直线
y1 = list2[0]+list2[1]*x1
print("正规方程实现：y="+str(list2[0])+"+"+str(list2[1])+"*x")
plt.plot(x1, y1,"r")

plt.show()

