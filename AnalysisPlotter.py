from collections import Counter
import matplotlib.pyplot as plt


class Plotter:

    def __init__(self):
        pass

    @staticmethod
    def plot_observations(observations):
        number = len(observations)
        top_results = dict(Counter(observations).most_common(number))
        plt.bar(list(top_results.keys()), top_results.values(), color='g')
        plt.xticks(rotation=90, fontsize=9)
        plt.title('Top {} observations'.format(number))
        plt.ylabel('Count')
        plt.show()

    @staticmethod
    def plot_moods(df):
        pie_chart = df.Mood.value_counts().plot(kind='pie', autopct='%1.1f%%', explode = (0.1, 0, 0))
        pie_chart.set_title('Sentiment percentages')
        plt.show()

