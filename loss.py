x = [1, 2, 3]
y = [5, 1, 3]

# y = x
m1 = 1
b1 = 0

# y = 0.5x + 1
m2 = 0.5
b2 = 1

y_predicted1 = []
for i in range(len(x)):
    y_predicted1.append(x[i]*m1+b1)

y_predicted2 = []
for i in range(len(x)):
    y_predicted2.append(x[i]*m2+b2)

    total_loss1 = 0
    total_loss2 = 0

for i in range(len(x)):
    total_loss1 += (y[i]-y_predicted1[i])**2

for i in range(len(x)):
    total_loss2 += (y[i]-y_predicted2[i])**2


print(total_loss1)
print(total_loss2)
better_fit = 2
