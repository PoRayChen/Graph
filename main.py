import matplotlib as plt
Month = ()
High = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
Low = [449.48, 553.57, 696.783, 870.133, 1000.
             4, 1309.1]

plt.plot(Month, High, color='red')
plt.plot(Month, Low, color='blue')
plt.xlabel('Month')
plt.ylabel('Tempture')
plt.title('Pakistan India Population till 2010')
plt.show()