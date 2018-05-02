import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

algo = ['StreamKM++', 'CC', 'RCC', 'OnlineCC']
data_name = 'covtype'
k = [10, 20, 30, 40, 50]
skmpp_update = []
cc_update = []
rcc_update = []
onlinecc_update = []


def func(file_name):
    with open(file_name) as f:
        lis = list(map(float, f.read().splitlines()))
        return sum(lis)/len(lis)*1000


# read data
for i in k:
    folder = 'C:/Users/Yu/Desktop/clustering result/' + data_name + '/k-' + str(i) + '/queryinterval-100'
    skmpp_update.append(func(folder + '/skmpp/updatetime.txt'))
    cc_update.append(func(folder + '/cache/updatetime.txt'))
    rcc_update.append(func(folder + '/rcc/updatetime.txt'))
    onlinecc_update.append(func(folder + '/hybrid_12/updatetime.txt'))


# configuration
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.markersize'] = 10
mpl.rcParams['font.size'] = 20
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['legend.fontsize'] = 16
mpl.rcParams['figure.figsize'] = [5.2, 3.76]
mpl.rcParams['legend.frameon'] = False


# line plot
fig, ax = plt.subplots()
width = 0.25
X = np.arange(len(k)) * 2 + 1 - width
ax.bar(X, skmpp_update, width, hatch='-', color='r')
ax.bar(X+width, cc_update, width, hatch='x', color='g')
ax.bar(X+2*width, rcc_update, width, hatch='.', color='b')
ax.bar(X+3*width, onlinecc_update, width, hatch='O', color='m')


# labels
plt.xlabel('number of clusters')
plt.ylabel('update time (ms)')

# xticks
plt.xticks(X+1.5*width, k)

# legend
if data_name == 'covtype':
    plt.legend(algo, ncol=2, columnspacing=0.2, labelspacing=0.2)
    plt.ylim(ymax=0.008)

#plt.show()
plt.savefig("figs/update_k/" + data_name + "_update_vs_k.pdf", dpi=600, bbox_inches='tight', transparent=True)
