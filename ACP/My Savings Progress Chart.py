import matplotlib.pyplot as plt
Weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
savings = [200, 400, 550, 670]
plt.plot(Weeks, savings, marker='o', color='blue', linestyle='-', linewidth=2)
plt.title('My Savings Progress Chart - Line Chart')
plt.xlabel('Weeks')
plt.ylabel('Savings (rupees)')
plt.grid(True)
plt.ylim(0, 800)
plt.show()
plt.bar(Weeks, savings, color='orange')
plt.title('My Savings Progress Bar Chart')
plt.xlabel('Weeks')
plt.ylabel('Savings (rupees)')
plt.show()