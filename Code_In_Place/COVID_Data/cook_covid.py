
"""
This program is intended to read the data from a csv containing COVID19 case numbers for April in 2020
and display it as an animated line plot.
"""

import datetime
import pandas
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# reads in aprilcovid.csv data, takes out dates and makes the index column
covid = pandas.read_csv('aprilcovid.csv', parse_dates=['Date'], index_col='Date')


def main():
    # creates a plot of specific dimensions
    fig = plt.figure(figsize=(11, 7))
    # makes the x axis labels/increments rotated by 70 degrees so they're not one on top of the other
    plt.xticks(rotation=70)
    # sets the minimum and maximum values for the x axis
    plt.xlim(datetime.date(2020, 4, 1), datetime.date(2020, 4, 30))
    # sets the minimum and maximum values for the y axis
    plt.ylim(np.min(covid)[0], (np.max(covid)[0]+10000))
    # labels x axis
    plt.xlabel('Date in April', fontsize=16)
    # labels y axis
    plt.ylabel('Total Cases', fontsize=16)
    # changes y-axis labels because they were showing up in scientific notation before applying style='plain'
    plt.ticklabel_format(axis='y', style='plain')
    # moved the plot over so the x and y labels are visible
    plt.subplots_adjust(left=.15, bottom=.25)
    # titles the plot
    plt.title('US COVID-19 Total Cases in April', fontsize=18)
    # animates the plot
    anim = matplotlib.animation.FuncAnimation(fig, animate, frames=30, repeat=True)
    # still working on the animation
    plt.show()


def animate(i):
    data = covid.iloc[:(i+1)]
    p = sns.lineplot(x=data.index, y=data['Number of Cases'], data=data, color='r')
    p.tick_params(labelsize=17)
    plt.setp(p.lines, linewidth=6)


if __name__ == '__main__':
    main()
