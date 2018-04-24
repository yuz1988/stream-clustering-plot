import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

algo = ['firstseq', 'skmpp', 'cache', 'rcc', 'hybrid_12']
data_name = 'covtype'
k = 20
queryinterval = 100

folder = data_name + '/k-' + str(k) + '/queryinterval-' + str(queryinterval)
with open(folder + '/firstseq/querytime' + '.txt') as f:
    firstseq_query = list(map(float, f.read().splitlines()))
with open(folder + '/skmpp/querytime' + '.txt') as f:
    skmpp_query = list(map(float, f.read().splitlines()))
with open(folder + '/cache/querytime' + '.txt') as f:
    cache_query = list(map(float, f.read().splitlines()))
with open(folder + '/rcc/querytime' + '.txt') as f:
    rcc_query = list(map(float, f.read().splitlines()))

print(sum(skmpp_query))
print(sum(cache_query))
print(sum(rcc_query))


with open(folder + '/firstseq/updatetime' + '.txt') as f:
    firstseq_update = list(map(float, f.read().splitlines()))
with open(folder + '/skmpp/updatetime' + '.txt') as f:
    skmpp_update = list(map(float, f.read().splitlines()))
with open(folder + '/cache/updatetime' + '.txt') as f:
    cache_update = list(map(float, f.read().splitlines()))
with open(folder + '/rcc/updatetime' + '.txt') as f:
    rcc_update = list(map(float, f.read().splitlines()))

print(sum(skmpp_update))
print(sum(cache_update))
print(sum(rcc_update))

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


# # msg transmitted
# plt.figure(0)
# plt.plot(exact[0], exact[2], marker='o', color='r')
# plt.plot(baseline[0], baseline[2], marker='*', color='g')
# plt.plot(uniform[0], uniform[2], marker='s', color='b')
# plt.plot(nonuniform[0], nonuniform[2], marker='+', color='k')
#
# # labels
# plt.xlabel('number of sites')
# plt.ylabel('number of messages')
#
# # xlim, ylim
# plt.ylim(ymin=0)
#
# # legend
# plt.legend(method, ncol=2)
#
# # show or save
# # plt.show()
# plt.savefig("figs/" + data_name + "-message.pdf", dpi=600, bbox_inches='tight')


# runtime delay
# plt.figure(1)
# plt.plot(exact[0], exact[3], marker='o', color='r')
# plt.plot(baseline[0], baseline[3], marker='*', color='g')
# plt.plot(uniform[0], uniform[3], marker='s', color='b')
# plt.plot(nonuniform[0], nonuniform[3], marker='+', color='k')
#
# # labels
# plt.xlabel('number of sites (Hepar II)')
# plt.ylabel('training time (sec)')
#
# # xlim, ylim
# plt.ylim(ymin=0, ymax=950)
#
# # legend
# plt.legend(method, ncol=2, columnspacing=0.5, frameon=False, fancybox=True)
#
# # show or save
# # plt.show()
# plt.savefig("figs/" + data_name + "-cluster.png", dpi=800, bbox_inches='tight', transparent=True)
#
#
# # Throughput
# pd.options.mode.chained_assignment = None
# num_vec = 500 * 1000
# exact[3] = num_vec / exact[3]
# baseline[3] = num_vec / baseline[3]
# uniform[3] = num_vec / uniform[3]
# nonuniform[3] = num_vec / nonuniform[3]
#
# plt.figure(2)
# plt.plot(exact[0], exact[3], marker='o', color='r')
# plt.plot(baseline[0], baseline[3], marker='*', color='g')
# plt.plot(uniform[0], uniform[3], marker='s', color='b')
# plt.plot(nonuniform[0], nonuniform[3], marker='+', color='k')
#
# # labels
# plt.xlabel('number of sites (Alarm)')
# plt.ylabel('throughput (events/sec)')
#
# # xlim, ylim
# plt.ylim(ymin=0)
# # if data_name == 'alarm':
# #     plt.ylim(ymax=2800)
# # elif data_name == 'hepar2':
# #     plt.ylim(ymax=1200)
#
# # legend
# # if data_name == 'alarm':
# #     plt.legend(method, ncol=2, bbox_to_anchor=(0.5, -0.05),
# #                loc='lower center', columnspacing=0.5)
#
# # show or save
# # plt.show()
# plt.savefig("figs/" + data_name + "-throughput.png", dpi=800, bbox_inches='tight')