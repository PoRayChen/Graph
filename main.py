import matplotlib.pyplot as plt
Month = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
High = [38, 41, 49.8, 60.7, 70.9, 79, 84.2, 82.4, 74.7, 63.5, 53.1, 42.9]
Low = [26.2, 28.1, 35.1, 44.2, 54.2, 63.3, 68.8, 67.7, 60.3, 49.6, 41, 31.6]

plt.plot(Month, High, color='red')
plt.plot(Month, Low, color='blue')
plt.xlabel('Month')
plt.ylabel('Tempture')
plt.title('NYC tempture')
plt.show()