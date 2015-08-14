import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(style="white", palette="muted", color_codes=True)
rs = np.random.RandomState(10)
d = rs.normal(size=100)
print d
sns.distplot(d, hist=False, color="g", kde_kws={"shade": True})
sns.plt.show()