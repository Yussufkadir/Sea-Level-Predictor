import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope1, intercept1, rval1, pval1, err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extended_years = pd.Series(range(1880,2051))
    line_of_best_fit_1 = slope1 * extended_years + intercept1
    plt.plot(extended_years, line_of_best_fit_1)
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, rval2, pval2, err2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    extended_years_2 = pd.Series(range(2000,2051))
    line_of_best_fit_2 = slope2 * extended_years_2 + intercept2
    plt.plot(extended_years_2, line_of_best_fit_2)
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
