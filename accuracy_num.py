import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

algo = ['Sequential', 'StreamKM++', 'CC', 'RCC', 'OnlineCC']
data_name = 'intrusion'
n = 581012
if data_name == 'power':
    n = 2049280
elif data_name == 'intrusion':
    n = 494021
elif data_name == 'synthetic':
    n = 200000

interval = int(n / 6)
seq_cost = []
skmpp_cost = []
cc_cost = []
rcc_cost = []
onlinecc_cost = []


def func(file_name):
    with open(file_name) as f:
        cost = list(map(float, f.read().splitlines()))
        cost.insert(0, 0)
    return cost[0:len(cost)-1]


# read data
folder = 'C:/Users/Yu/Desktop/clustering result/' + data_name + '/k-30' + '/queryinterval-100'
seq_cost = func(folder + '/firstseq/accuracy.txt')
skmpp_cost = func(folder + '/skmpp/accuracy.txt')
cc_cost = func(folder + '/cache/accuracy.txt')
rcc_cost = func(folder + '/rcc/accuracy.txt')
onlinecc_cost = func(folder + '/hybrid_12/accuracy.txt')


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
X = range(0, 7)
X = [i*interval for i in X]
print(X)
print(skmpp_cost)
# plt.plot(X, seq_cost, marker='+', color='c')
plt.plot(X, skmpp_cost, marker='s', color='r')
plt.plot(X, cc_cost, marker='x', color='g')
plt.plot(X, rcc_cost, marker='*', color='b')
plt.plot(X, onlinecc_cost, marker='o', color='m')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))

# labels
plt.xlabel('number of points')
plt.ylabel('k-means cost')

# legend
if data_name == 'covtype':
    plt.legend(algo, columnspacing=0.2, labelspacing=0.2)
    # plt.ylim(ymax=16)

# plt.show()
plt.savefig("figs/accuracy_num/" + data_name + "_cost_vs_num.pdf", dpi=600, bbox_inches='tight', transparent=True)
