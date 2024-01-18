import matplotlib.pyplot as plt

x_list = [i for i in range(1,11)]
y_list = [i*2 for i in range(1,11)]

print(x_list)
print(y_list)

plt.plot(x_list,y_list)
plt.show()