import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

algo = ['StreamKM++', 'CC', 'RCC', 'OnlineCC']
data_name = 'covtype'
k = [10, 20, 30, 40, 50]
skmpp_query = []
cc_query = []
rcc_query = []
onlinecc_query = []


def func(file_name):
    with open(file_name) as f:
        lis = list(map(float, f.read().splitlines()))
        return sum(lis)/len(lis)*1000/100


# read data
for i in k:
    folder = 'C:/Users/Yu/Desktop/clustering result/' + data_name + '/k-' + str(i) + '/queryinterval-100'
    skmpp_query.append(func(folder + '/skmpp/querytime.txt'))
    cc_query.append(func(folder + '/cache/querytime.txt'))
    rcc_query.append(func(folder + '/rcc/querytime.txt'))
    onlinecc_query.append(func(folder + '/hybrid_12/querytime.txt'))


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
ax.bar(X, skmpp_query, width, hatch='-', color='r')
ax.bar(X+width, cc_query, width, hatch='x', color='g')
ax.bar(X+2*width, rcc_query, width, hatch='.', color='b')
ax.bar(X+3*width, onlinecc_query, width, hatch='O', color='m')
ax.set_yscale('log')


# labels
plt.xlabel('number of clusters')
plt.ylabel('query time (ms)')

# xticks
plt.xticks(X+1.5*width, k)

# legend
if data_name == 'covtype':
    plt.legend(algo, ncol=2, columnspacing=0.2, labelspacing=0.2)
    plt.ylim(ymax=40)

# plt.show()
plt.savefig("figs/query_k/" + data_name + "_query_vs_k.pdf", dpi=600, bbox_inches='tight', transparent=True)
