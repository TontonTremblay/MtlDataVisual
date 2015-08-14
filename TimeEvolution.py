import csv
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from pylab import *
import seaborn as sns


f = open("data.csv")
data = []
try:
    reader = csv.reader(f)
    for row in reader:
        data.append( row )
finally:
    f.close()

# print data[0] 


x = data[0][1:-1]
x = map(lambda v: int(v),x)
# print x

dataf = []
for i in range(len(x)):
    i +=1
    t = []
    for j in range(1,len(data)):
        t.append(float(data[j][i]))

    dataf.append([x[i-1],t])

# dataf = np.array(dataf)
# print dataf[0]
maxValuey = []

sns.set_style("white")
sns.despine()

for i,d in enumerate(dataf):
    ax = sns.distplot(np.array(d[1]), hist=False, color="g", kde_kws={"shade": True})
    # maxValuey.append( sns.plt.axis()[3])
# print max(maxValuey)
    sns.plt.axis([0, 250, 0, 0.012])
    sns.plt.title("Teen Fertility Rate (age 15-19) per 1000")
    sns.plt.xlabel("Birth rate")
    sns.plt.ylabel("Distribution")
    
    ax.annotate(d[0], size="large",ha="left",xy=(220,0.011))

    # sns.plt.show()
    sns.plt.savefig("output/"+str(d[0])+".png")
    sns.plt.clf()
    # break