import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

algo = ['firstseq', 'skmpp', 'cache', 'rcc', 'hybrid_12']
method = ['streamkm++', 'CC', 'RCC']
data_name = 'covtype'
k = 20
query_interval = [100, 500, 1000, 2000, 3000, 4000, 5000]
length = len(query_interval)
firstseq_query = []
skmpp_query = []
cache_query = []
rcc_query = []

# read data
for i in range(length):
    folder = data_name + '/k-' + str(k) + '/queryinterval-' + str(query_interval[i])
    # with open(folder + '/firstseq/querytime' + '.txt') as f:
    #     firstseq_query[i] = sum(list(map(float, f.read().splitlines())))
    with open(folder + '/skmpp/querytime' + '.txt') as f:
        skmpp_query.append(sum(list(map(float, f.read().splitlines()))))
    with open(folder + '/cache/querytime' + '.txt') as f:
        cache_query.append(sum(list(map(float, f.read().splitlines()))))
    with open(folder + '/rcc/querytime' + '.txt') as f:
        rcc_query.append(sum(list(map(float, f.read().splitlines()))))

print(skmpp_query)
print(cache_query)
print(rcc_query)

firstseq_update = []
skmpp_update = []
cache_update = []
rcc_update = []

# read data
for i in range(length):
    folder = data_name + '/k-' + str(k) + '/queryinterval-' + str(query_interval[i])
    # with open(folder + '/firstseq/querytime' + '.txt') as f:
    #     firstseq_update.append(sum(list(map(float, f.read().splitlines()))))
    with open(folder + '/skmpp/updatetime' + '.txt') as f:
        skmpp_update.append(sum(list(map(float, f.read().splitlines()))))
    with open(folder + '/cache/updatetime' + '.txt') as f:
        cache_update.append(sum(list(map(float, f.read().splitlines()))))
    with open(folder + '/rcc/updatetime' + '.txt') as f:
        rcc_update.append(sum(list(map(float, f.read().splitlines()))))

print(skmpp_update)
print(cache_update)
print(rcc_update)

# configuration
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.markersize'] = 10
mpl.rcParams['font.size'] = 20
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['legend.fontsize'] = 17
mpl.rcParams['figure.figsize'] = [5.2, 3.9]
# mpl.rcParams['legend.frameon'] = False


# plot begins
plt.figure(0)
x = range(length)
plt.plot(x, skmpp_query, marker='o', color='r')
plt.plot(x, cache_query, marker='*', color='g')
plt.plot(x, rcc_query, marker='s', color='b')

# x-ticks
plt.xticks(np.arange(length), ('100', '500', '1000', '2000', '3000', '4000', '5000'))

# labels
plt.xlabel('query interval')
plt.ylabel('total query time (second)')

# legend
plt.legend(method)

plt.ylim(ymin=0)

# # show or save
# # plt.show()
plt.savefig("figs/" + data_name + "-query.png", dpi=600, bbox_inches='tight')  # transparent


# update time
plt.figure(1)
plt.plot(x, skmpp_update, marker='o', color='r')
plt.plot(x, cache_update, marker='*', color='g')
plt.plot(x, rcc_update, marker='s', color='b')

# x-ticks
plt.xticks(np.arange(length), ('100', '500', '1000', '2000', '3000', '4000', '5000'))

# labels
plt.xlabel('query interval')
plt.ylabel('total update time (second)')

# legend
plt.legend(method)

plt.ylim(ymin=0)
# plt.show()
plt.savefig("figs/" + data_name + "-update.png", dpi=600, bbox_inches='tight')  # transparent