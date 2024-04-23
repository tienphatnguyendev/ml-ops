from .data_visualizer import DataVisualizer
import seaborn as sns
import matplotlib.pyplot as plt

colors = [
    "#191D88",
    "#1450A3",
    "#337CCF",
    "#FFC436",
]
sns.set_palette(sns.color_palette(colors))


class NumericVisualizer(DataVisualizer):
    def plot_distribution(self, cols, bins=10, figsize=(20, 15), cols_per_row=3):
        """
        Plots distribution plots for specified numeric columns of a DataFrame.

        Parameters:
        - cols (list): List of numeric column names to plot.
        """
        fig, axes = self.setup_plot(len(cols), cols_per_row, figsize)

        for i, col in enumerate(cols):
            if col in self.df.columns:
                sns.histplot(self.df[col], kde=True, ax=axes[i], bins=bins)
                axes[i].set_title(f"Distribution of {col}")
            else:
                print(f"Column {col} not found in DataFrame.")

        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)

        plt.tight_layout()
        plt.show()
