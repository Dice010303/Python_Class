import matplotlib.pyplot as plt

x_list = [i for i in range(-5,6)]
y_list = [i*i*-1 for i in range(-5,6 )]

print(x_list)
print(y_list)

plt.plot(x_list,y_list)
plt.show()