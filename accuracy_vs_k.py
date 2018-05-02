import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

algo = ['Sequential', 'StreamKM++', 'CC', 'RCC', 'OnlineCC', 'KMeans++']
data_name = 'intrusion'
k = [10, 20, 30, 40, 50]
seq_accuracy = []
skmpp_accuracy = []
cc_accuracy = []
rcc_accuracy = []
online_accuracy = []
kmpp_accuracy = []


def func(file_name):
    with open(file_name) as f:
        lis = list(map(float, f.read().splitlines()))
        return lis[len(lis)-1]


# read data
for i in k:
    folder = 'C:/Users/Yu/Desktop/clustering result/' + data_name + '/k-' + str(i) + '/queryinterval-100'
    seq_accuracy.append(func(folder + '/firstseq/accuracy.txt'))
    skmpp_accuracy.append(func(folder + '/skmpp/accuracy.txt'))
    cc_accuracy.append(func(folder + '/cache/accuracy.txt'))
    rcc_accuracy.append(func(folder + '/rcc/accuracy.txt'))
    online_accuracy.append(func(folder + '/hybrid_12/accuracy.txt'))

    folder1 = 'C:/Users/Yu/Desktop/clustering result/' + data_name + '/k-' + str(i)
    kmpp_accuracy.append(func(folder1 + '/kmpp/accuracy.txt'))


print(seq_accuracy)
print(skmpp_accuracy)
print(cc_accuracy)
print(rcc_accuracy)
print(online_accuracy)
print(kmpp_accuracy)


# configuration
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.markersize'] = 10
mpl.rcParams['font.size'] = 20
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['legend.fontsize'] = 14
mpl.rcParams['figure.figsize'] = [5.2, 3.76] # intrusion hight=4.1
mpl.rcParams['legend.frameon'] = False


# bar plot
fig, ax = plt.subplots()
width = 0.25
X = np.arange(len(k)) * 2 + 1 - width

# ax.bar(X, seq_accuracy, width, hatch='/', color='c')  # intrusion not draw sequential
ax.bar(X+width, skmpp_accuracy, width, hatch='-', color='r')
ax.bar(X+2*width, cc_accuracy, width, hatch='x', color='g')
ax.bar(X+3*width, rcc_accuracy, width, hatch='.', color='b')
ax.bar(X+4*width, online_accuracy, width, hatch='O', color='m')
ax.bar(X+5*width, kmpp_accuracy, width, hatch='*', color='y')

# labels
plt.xlabel('number of clusters')
plt.ylabel('k-means cost')

# xticks
# plt.xticks(X+2.5*width, k)
plt.xticks(X+3*width, k) # intrusion

# legend
if data_name == 'covtype':
    plt.legend(algo, ncol=2, columnspacing=0.2, labelspacing=0.2)
    plt.ylim(ymax=7e11)

plt.savefig("figs/accuracy_k/" + data_name + "_cost_vs_k.pdf", dpi=600, bbox_inches='tight', transparent=True)
