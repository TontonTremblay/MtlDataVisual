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
print x
datax = []
datay = []
dataf = []
for i in range(1,len(data)):
	#get all the data point for that year
	y = map(lambda v:  float(v),data[i][1:-1])
	

	for j in range(len(x)):
		dataf.append([ x[j],y[j]])


dataf = np.array(dataf)




f, ax = plt.subplots(figsize=(7, 7))
sns.set_style("white")

# sns.palplot(sns.color_palette("cubehelix", 8))
cmap = sns.cubehelix_palette(light=1, as_cmap=True)

sns.kdeplot(dataf, shade=True,cmap=cmap, ax=ax)
sns.plt.axis([x[0], x[-1], 0, 250])
sns.plt.title("Adolescent Fertility Rate (15-19) per 1000")
sns.plt.xlabel("years")
sns.plt.ylabel("Birth rate per 1000")

# sns.plt.show()
sns.plt.savefig("output.png")