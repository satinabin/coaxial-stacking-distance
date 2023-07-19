# 导入numpy和matplotlib库
import numpy as np
import matplotlib.pyplot as plt

# 读入mpi_0_last_conf.dat文件，跳过前三行，只取前三列作为坐标
coords = np.loadtxt("mpi_0_last_conf.dat", skiprows=3, usecols=(0,1,2))

# 计算每个粒子与下一行粒子的距离，用欧几里得公式
distances = np.sqrt(np.sum((coords[1:] - coords[:-1])**2, axis=1))

# 将距离乘以0.8518，单位为nm
distances = distances * 0.8518

# 输出每个距离并从零标序号，保存到distances.txt文件中
with open("distances.txt", "w") as f:
    for i, d in enumerate(distances):
        f.write(f"{i}: {d:.4f} nm\n")

    # 在文件最后一行输出所有距离的平均值
    mean = np.mean(distances)
    f.write(f"Average: {mean:.4f} nm\n")

# 画出散点图，并对数据做线性回归，保存到plot.png文件中
plt.scatter(np.arange(len(distances)), distances)
plt.xlabel("Index")
plt.ylabel("Distance (nm)")
slope, intercept = np.polyfit(np.arange(len(distances)), distances, 1)
plt.plot(np.arange(len(distances)), slope * np.arange(len(distances)) + intercept, color="red")
plt.savefig("plot.png")
# 在图上显示斜率和截距
plt.text(0.8, 0.9, f"y = {slope:.4f}x + {intercept:.4f}", transform=plt.gca().transAxes)