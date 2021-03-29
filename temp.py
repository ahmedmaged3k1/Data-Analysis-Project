import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv (r'dataset.csv')
#Calculate MEAN,MODE,Median

mean1= file['Height'].mean()


mode1= file['Height'].max()
median1 = file['Height'].median()
std1 = file['Height'].std()

mean2= file['Weight'].mean()
mode2= file['Weight'].max()
median2 = file['Weight'].median()
std2 = file['Weight'].std()

s1 = pd.Series(file['Weight'])
s2 = pd.Series(file['Height'])
corr = s1.corr(s2)
print("Correlation between Height and Weight is equal to " ,"{:.5f}".format (corr))
    



print('Mean of Height is = ' ,"{:.2f}".format(mean1))
print('Mode of Height is = ' ,"{:.2f}".format(mode1))
print('Median of Height  is = ' ,"{:.2f}".format(median1))
print('Standard Deviation of Height  is = ' ,"{:.2f}".format(std1))

print('Mean of Weight is = ' ,"{:.2f}".format(mean2))
print('Mode of Weight is = ' ,"{:.2f}".format(mode2))
print('Median of Weight is = ' ,"{:.2f}".format(median2))
print('Standard Deviation of Weight is = ' ,"{:.2f}".format(std2))

file.boxplot(column=['Height','Weight'])
file.plot(x="Height",y="Weight",kind= "scatter")



file.hist(column="Weight",bins = 23)
plt.title(" Height Histogram")
plt.ylabel("Frequency")
plt.xlabel("Height/cm")


file.hist(column="Weight",bins = 23)
plt.title(" Weight Histogram")
plt.ylabel("Frequency")
plt.xlabel("Weight/KG")












