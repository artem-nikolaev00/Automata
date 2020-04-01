import matplotlib.pyplot as plt

lines = [10000, 100000]
number = [1, 10]
REG = [0.03663729999999976, 0.36030850000000214]
SMC = [0.46962290000000007, 4.8826401]
PLY = [0.3116515999999998, 3.1611903000000003]

plt.title('Time/count')
plt.xlabel('Count, x * 10^4')
plt.ylabel('Time, s')
plt.grid()

plt.plot(number, REG, label='REG')
plt.plot(number, SMC, label='SMC')
plt.plot(number, PLY, label='PLY')



plt.legend()

plt.show()