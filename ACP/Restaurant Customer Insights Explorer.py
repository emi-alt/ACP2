import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
df.dropna()
print("HEAD - 3")
print(df.head(3))
print()
print('DATASET INFO')
print(df.info())
print()
#step 2
sns.barplot(data=df, x='day', y='total_bill', hue='sex')
plt.title('Barplot of Total Bill by Day and Sex')
plt.show()
sns.countplot(data=df, x='day', hue='sex')
plt.title('Countplot of Day by Sex')
plt.show()
#step 3  
sns.boxplot(data=df, x='day', y='total_bill')
plt.title('Boxplot of Total Bill by Day and Sex')
plt.show()
sns.stripplot(data=df, x='day', y='total_bill', jitter=True)
plt.title('Stripplot of Total Bill by Day and Sex')
plt.show()
sns.swarmplot(data=df, x='day', y='total_bill')
plt.title('Swarmplot of Total Bill by Day and Sex')
plt.show()
#step 4
sns.jointplot(data=df, x='total_bill', y='tip', hue='sex')
plt.title('Jointplot of Total Bill and Tip by Sex')
plt.show()
sns.jointplot(data=df, x='total_bill', y='tip', hue='sex', kind='kde')
plt.title('Jointplot of Total Bill and Tip by Sex')
plt.show()
#step 5
sns.pairplot(data=df,vars=['total_bill','tip','size'], hue='sex')
plt.title('Pairplot of Total Bill, Tip and Size by Sex')
plt.show()
#step 6
sns.pointplot(data=df, x='day', y='total_bill', hue='sex')
plt.title('Pointplot of Total Bill by Day and Sex')
plt.show()
sns.lmplot(data=df, x='total_bill', y='tip')
plt.title('LMplot of Total Bill and Tip')
plt.show()

#pointplot
#LMplot
#jointplot