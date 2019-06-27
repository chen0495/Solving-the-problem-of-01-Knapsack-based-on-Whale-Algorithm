#鲸鱼0-1背包
import numpy as np
import time

str=input("输入各个背包的价值： ")
v=np.array(list(map(int,str.split(","))))  #价值
str=input("输入各个背包的重量： ")
w=np.array(list(map(int,str.split(",")))) #重量or体积
x_best=np.zeros((len(v),len(v))) #4只鲸鱼目前的位置,0/1表示;
x_best=np.array(x_best)
bw=int(input("输入背包大小："))  #背包大小
start = time.clock()#计时开始
x_max=int(len(v))  #迭代次数
for i in range(len(v)):
    x_best[i][i]=1
#初始化鲸鱼位置
#print(x_best)

def update_position():
    max_sum=0
    max_i=0
    for i in range(len(v)):
        tmp_x=x_best[i]*v
        tmp_weight=x_best[i]*w
        tmp_sum=sum(tmp_x)
        tmp_w=sum(tmp_weight)
        if tmp_w>bw:
            tmp_sum=0
        if tmp_sum>max_sum:
            max_sum=tmp_sum
            max_i=i
    return max_i
#更新离目标最近的鲸鱼
#print(update_position())

for i in range(x_max):
    tmp_best_i=update_position()
    for j in range(len(v)):
        if x_best[tmp_best_i][j]==1:
            for k in range(len(v)):
                x_best[k][j]=1
    if i==x_max-1:
        print("Answer is: ")
        print(x_best[tmp_best_i])#输出解
        print(sum(x_best[tmp_best_i]*v))#输出最终结果
        print("耗时: ",time.clock() - start)#输出计时结果


