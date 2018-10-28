import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
color_list = sns.color_palette('deep') + sns.color_palette('bright')

def DrawCurve(x, y_list, std_list, xlabel='', ylabel='', title='', name_list=[], store_path='', is_show=True, fig=plt.figure()):
    '''
    Draw the curve like ROC
    :param x: the vector of the x
    :param y_list: the list of y vectors. Each of the vector should has same length with x
    :param xlabel: the name of the y axis
    :param ylabel: the name of the x axis
    :param title: the tile of the figure,
    :param name_list: the legend name list corresponding to y list
    :param store_path: the store path, supporting jpg and esp format
    :param is_show: Boolen, if it was set to True, the figure would show.
    :return:
    '''
    if not isinstance(y_list, list):
        y_list = [y_list]

    fig.clear()
    axes = fig.add_subplot(1, 1, 1)
    # y_array = np.array(y_list)
    # std_array = np.array(std_list)
    # one_se = np.max(y_array) - std_array[np.where(y_array == np.max(y_array))]
    # line = np.ones((1, len(x)))*one_se
    sub_color_list = []
    for index in range(len(y_list)):
        sub_y_list = y_list[index]
        sub_std_list = std_list[index]
        sub_one_se = max(sub_y_list) - sub_std_list[sub_y_list.index(max(sub_y_list))]
        line = np.ones((1, len(x))) * sub_one_se
        line_list = line.tolist()

        # axes.plot(x, y_list[index], color=color_list[index])

        axes.errorbar(x, sub_y_list, yerr=sub_std_list, fmt='-o',
                      color=color_list[index], elinewidth=2, capsize=4, alpha=0.7, marker='.')
    axes.set_xticks(np.linspace(1, len(x), len(x)))
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_title(title)
    if name_list != []:
        axes.legend(name_list, loc=4)
    for index in range(len(y_list)):
        sub_y_list = y_list[index]
        sub_std_list = std_list[index]
        sub_one_se = max(sub_y_list) - sub_std_list[sub_y_list.index(max(sub_y_list))]
        line = np.ones((1, len(x))) * sub_one_se
        line_list = line.tolist()

        for index in range(len(sub_y_list)):
            if sub_y_list[index] >= sub_one_se:
                best_auc_value = sub_y_list[index]
                best_auc_feature_number = index+1
                break
        # axes.annotate(r'best point', color='r', xy=(best_auc_feature_number, best_auc_value),
        #         #               xytext=(len(x)/2, 0.5),
        #         #               textcoords='offset points', fontsize=12,
        #         #               arrowprops=dict(facecolor="red", headlength=8, headwidth=4, width=4))
        axes.plot(x, line_list[0], color='orange', linewidth=1, linestyle="--")
        axes.plot(best_auc_feature_number, best_auc_value, 'H', linewidth=20, color='black')

    if store_path:
        # plt.tight_layout()
        fig.set_tight_layout(True)
        if store_path[-3:] == 'jpg':
            fig.savefig(store_path, dpi=300, format='jpeg')
        elif store_path[-3:] == 'eps':
            fig.savefig(store_path, dpi=1200, format='eps')
    if is_show:
        axes.show()

    # plt.close(fig)
    return axes

def DrawBar(x_ticks, y_list, ylabel='', title='', name_list=[], store_path='', is_show=True, fig=plt.figure()):
    if not isinstance(y_list, list):
        y_list = [y_list]

    fig.clear()
    axes = fig.add_subplot(1, 1, 1)
    width = 0.3

    x = np.arange(len(x_ticks))
    for index in range(len(y_list)):
        axes.bar(x + width * index, y_list[index], width, color=color_list[index])

    axes.set_ylabel(ylabel)
    axes.set_title(title)
    axes.set_xticks(x + width * (len(y_list) - 1) / 2)
    axes.set_xticklabels(x_ticks)

    if name_list != []:
        axes.legend(name_list, loc=4)

    if store_path:
        # plt.tight_layout()
        fig.set_tight_layout(True)
        if store_path[-3:] == 'jpg':
            fig.savefig(store_path, dpi=300, format='jpeg')
        elif store_path[-3:] == 'eps':
            fig.savefig(store_path, dpi=1200, format='eps')
    if is_show:
        axes.show()

    # plt.close(fig)
    return axes
