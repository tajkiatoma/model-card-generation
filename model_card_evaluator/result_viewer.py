from pathlib import Path

import seaborn as sns
import matplotlib.ticker as mtick
from matplotlib import pyplot as plt

from util import constants


def plot_one_violin(data, lower_bound, upper_bound, save_file_path: Path):
    fig = plt.figure(figsize=(5, 1.5))
    with sns.axes_style('white'):
        fig.add_subplot()
        ax = sns.violinplot(x=data, cut=0, orient='h', color=constants.PLOT_COLOR)
        sns.despine(ax=ax, top=True, right=True, left=False)

    plt.xlabel('')
    plt.xlim(lower_bound, upper_bound)

    # plt.gca().xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout()

    save_file_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(save_file_path, dpi=300)
    plt.show()
