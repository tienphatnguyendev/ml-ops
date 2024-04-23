from .data_visualizer import DataVisualizer
import seaborn as sns
import matplotlib.pyplot as plt

colors = [
    "#03256C",
    "#2541B2",
    "#1768AC",
    "#E5D549",
]
sns.set_palette(sns.color_palette(colors))


class CategoricalVisualizer(DataVisualizer):
    def plot_distribution(self, cols, figsize=(20, 15), cols_per_row=3):
        """
        Plots distribution plots for specified categorical columns of a DataFrame.

        Parameters:
        - cols (list): List of numeric column names to plot.
        """
        fig, axes = self.setup_plot(len(cols), cols_per_row, figsize)
        axes = axes.flatten()
        sns.countplot(data=self.df, x=cols[0])
        for i, col in enumerate(cols):
            if col in self.df.columns:
                sns.countplot(data=self.df, x=col, ax=axes[i])
                axes[i].set_title(f"Distribution of {col}")
            else:
                print(f"Column {col} not found in DataFrame.")

        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)

        plt.tight_layout()
        plt.show()
