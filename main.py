# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import matplotlib.pyplot as pla

pla.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
pla.rcParams['axes.unicode_minus']=False #用来正常显示负号

squares=[1,4,9,16,25]

fig,ax = pla.subplots()

ax.plot(squares, linewidth = 5)

ax.set_title("平方数", fontsize = 24)

ax.set_xlabel("值", fontsize = 14)

ax.set_ylabel("平方", fontsize = 14)

ax.tick_params(axis='both', labelsize = 14)

pla.show()

# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
