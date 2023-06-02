
import matplotlib.pyplot as pla
pla.style.available

pla.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
pla.rcParams['axes.unicode_minus']=False #用来正常显示负号

squares=[1,4,9,16,25]
pla.style.use('seaborn')
fig,ax = pla.subplots()

ax.plot(squares, linewidth = 5)

ax.set_title("平方数", fontsize = 24)

ax.set_xlabel("值", fontsize = 14)

ax.set_ylabel("平方", fontsize = 14)

ax.tick_params(axis='both', labelsize = 14)

pla.show()



import matplotlib.pyplot as plt
x_values = list(range(5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolors='none',s=5)
plt.title('digits',fontsize=14)
plt.xlabel('value',fontsize=10)
plt.ylabel('digit',fontsize=10)
plt.show()

