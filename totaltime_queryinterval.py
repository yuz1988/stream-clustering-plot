import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

algo = ['StreamKM++', 'CC', 'RCC', 'OnlineCC']
data_name = 'covtype'
q = [50, 100, 200, 400, 800, 1600, 3200]
skmpp_total = []
cc_total = []
rcc_total = []
onlinecc_total = []


def func(file_name1, file_name2):
    with open(file_name1) as f:
        lis = list(map(float, f.read().splitlines()))
        update = sum(lis)
    with open(file_name2) as f:
        lis = list(map(float, f.read().splitlines()))
        query = sum(lis)
    return update + query


# read data
for i in q:
    folder = 'C:/Users/Yu/Desktop/clustering result/' + data_name + '/k-30' + '/queryinterval-' + str(i)
    skmpp_total.append(func(folder + '/skmpp/updatetime.txt', folder + '/skmpp/querytime.txt'))
    cc_total.append(func(folder + '/cache/updatetime.txt', folder + '/cache/querytime.txt'))
    rcc_total.append(func(folder + '/rcc/updatetime.txt', folder + '/rcc/querytime.txt'))
    onlinecc_total.append(func(folder + '/hybrid_12/updatetime.txt', folder + '/hybrid_12/querytime.txt'))


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
plt.plot(q, skmpp_total, marker='s', color='r')
plt.plot(q, cc_total, marker='x', color='g')
plt.plot(q, rcc_total, marker='*', color='b')
plt.plot(q, onlinecc_total, marker='o', color='m')
ax.set_xscale('log')
# ax.set_yscale('log')


# labels
plt.xlabel('query interval')
plt.ylabel('total time (seconds)')

# xticks
plt.xticks(q, q)

# legend
if data_name == 'covtype':
    plt.legend(algo, columnspacing=0.2, labelspacing=0.2)
    # plt.ylim(ymax=16)

# plt.show()
plt.savefig("figs/total_q/" + data_name + "_total_vs_q.pdf", dpi=600, bbox_inches='tight', transparent=True)
