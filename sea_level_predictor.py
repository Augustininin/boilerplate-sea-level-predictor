import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot

    #Creat a figure and axis in API oriented objects
    fig, ax = plt.subplots()
    
    #get the data from the dataframe from the two columns 
    # Years for x axis and Sea level for y axis
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    #Draw the scatter plot with the x and y values
    ax.scatter(x, y)

    
    
    # Create first line of best fit
    
    # Calculate the y values using the linear regression parameters
    res_all = linregress(x, y)
    # Create an array of years from the minimum year in the data to 2050
    years_all = np.arange(x.min(), 2051)
    # Calculate the corresponding y values for the line of best fit
    y_all_fit = res_all.slope * years_all + res_all.intercept
    ax.plot(years_all, y_all_fit)

    # Create second line of best fit
    # Filter the dataframe for years 2000 and later
    df_2000 = df[df['Year'] >= 2000]
    # Calculate the y values using the linear regression parameters for years 2000 and later
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    #Create an array of years from 2000 to 2050
    years_2000 = np.arange(2000, 2051)
    #Calculate the corresponding y values for the line of best fit
    y_2000_fit = res_2000.slope * years_2000 + res_2000.intercept
    ax.plot(years_2000, y_2000_fit)


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return ax