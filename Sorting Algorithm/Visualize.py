"""Visualizer"""

import matplotlib
matplotlib.use("Qt5Agg")  # external window
import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def visualize(title, sortFunc, arr):
        plt.close("all")  # close previous figures

        generator = sortFunc(arr)  # generator from your sorting function

        fig, ax = plt.subplots(figsize=(15, 8))
        fig.canvas.set_window_title("My Sorting Visualizer") 
        ax.set_title(title, fontsize=22, fontweight='bold', color='green', fontname='Comic Sans MS')
        bars = ax.bar(range(len(arr)), arr, color='blue')

        for state in generator:
            for i, bar in enumerate(bars):
                bar.set_height(state[i])
            plt.pause(0.5)

        plt.show()

