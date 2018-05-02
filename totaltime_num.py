import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

algo = ['StreamKM++', 'CC', 'RCC', 'OnlineCC']
data_name = 'synthetic'
skmpp_total = []
cc_total = []
rcc_total = []
onlinecc_total = []


def func(file_name1, file_name2):
    with open(file_name1) as f:
        update = list(map(float, f.read().splitlines()))
    with open(file_name2) as f:
        query = list(map(float, f.read().splitlines()))
    total = []
    for i in range(len(query)):
        time = query[i]
        for j in range(100):
            time += update[i*100+j]
        total.append(time*1000/100)
    return sample(total)


def sample(lis):
    num = 6
    sample_lis = []
    interval = int(len(lis)/num)
    print(interval)
    accum_lis = []
    accum_val = 0
    index = 0
    for i in range(len(lis)):
        accum_val += lis[i]
        index += 1
        accum_lis.append(accum_val/index)

    for i in range(1, num+1):
        sample_lis.append(accum_lis[i*interval])
    return sample_lis


# read data
folder = 'C:/Users/Yu/Desktop/clustering result/' + data_name + '/k-30' + '/queryinterval-100'
skmpp_total = func(folder + '/skmpp/updatetime.txt', folder + '/skmpp/querytime.txt')
cc_total = func(folder + '/cache/updatetime.txt', folder + '/cache/querytime.txt')
rcc_total = func(folder + '/rcc/updatetime.txt', folder + '/rcc/querytime.txt')
onlinecc_total = func(folder + '/hybrid_12/updatetime.txt', folder + '/hybrid_12/querytime.txt')


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
X = range(1, len(skmpp_total)+1)
X = [i*333*100 for i in X]  # covtype 968 power 3415 intrusion 823 synthetic 333
plt.plot(X, skmpp_total, marker='s', color='r')
plt.plot(X, cc_total, marker='x', color='g')
plt.plot(X, rcc_total, marker='*', color='b')
plt.plot(X, onlinecc_total, marker='o', color='m')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

# labels
plt.xlabel('number of points')
plt.ylabel('runtime (ms)')


# legend
if data_name == 'covtype':
    plt.legend(algo, ncol=2, columnspacing=0.2, labelspacing=0.2)
    # plt.ylim(ymax=16)

# plt.show()
plt.savefig("figs/total_num/" + data_name + "_total_vs_num.pdf", dpi=600, bbox_inches='tight', transparent=True)
