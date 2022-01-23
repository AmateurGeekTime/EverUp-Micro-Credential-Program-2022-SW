# -*- coding: utf-8 -*-
"""COVID19_DATA_ANALYSIS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R-E5sRnIkin8e5JrbQ3UV8-zHxecC7YR

<a href="https://colab.research.google.com/github/niteen11/lagcc_data_analytics_micro_credential/blob/master/Unit%203%20-%20Python%20Advanced/Mini%20Project/COVID19_DATA_ANALYSIS.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# COVID 19 Data Analysis

**Description:** This script will read the latest data from the New York Times' county-level COVID-19 database at https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv, filter the data for a chosen county in a chosen state, calculate the daily count of new cases and new deaths, print the most recent 28 days' worth of data for the selected county, and save the county's data for all dates to a comma-separated value (.csv) file on your computer. The printed data can be copied and pasted directly into a spreadsheet for further analysis and visualization.

**Note:** For information about the data, see https://github.com/nytimes/covid-19-data.

**Note:** After you have run the script one time in a given Anaconda environment, you may reduce the script's execution time by adding a `#` in front of `pip install pandas`. For example, `#pip install pandas` instead of `pip install pandas`. The `#` will tell Python to skip the code without running it.

# Task 1 : Environment Set up

Import all required libraries that are needed for data analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

"""# Task 2 :  Data Collection

Use nytimes github repository as a data source to collect the covid 19 data in real time and ingest it into colab notebook for data anlysis purpose
"""

df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')

df.head()

df.shape

df.columns

"""# Task 3 : Data Wrangling and EDA (Exploratory Data Analysis)

Analyzing New York state data for Covid 19
"""

ny_df = df[df['state']=='New York']

ny_df.head()

ny_df.shape

ny_df.tail()

#first death in NY
first_ny_death = ny_df[ny_df['deaths']!=0]
first_ny_death.head()

#total number of cases
ny_df['cases'].max()

# not a correct way of calculating total count bcoz data is cumulative
ny_df['cases'].sum()

"""Finding new covid 19 cases on daily basis (new cases added everyday)"""

#new cases for NY
# type(ny_df['cases'])

newcase = []
previuos_case = 0
for index, row in ny_df.iterrows():
  current_case = row['cases']
  newcase_count = current_case - previuos_case
  previuos_case = current_case
  newcase.append(newcase_count)
  # print(newcase_count)

ny_df['new_cases'] = newcase

ny_df.head(10)

ny_df['new_cases'].sum()

ny_cases = ny_df['cases']
ny_deaths = ny_df['deaths']
ny_dates = ny_df['date']
ny_new_cases = ny_df['new_cases']

type(ny_new_cases)

ny_df.plot(kind='bar')

plt.figure(figsize=(15,7))
plt.bar(x=ny_dates, height=ny_new_cases, color='red')
plt.xticks(rotation=90)
plt.show()

"""# Task4: Understand NY covid 19 data in last 30 days"""

ny_cases_30 = ny_df['cases'][-31:-1]
ny_deaths_30 = ny_df['deaths'] [-31:-1]
ny_dates_30 = ny_df['date'][-31:-1]
ny_new_cases_30 = ny_df['new_cases'][-31:-1]

# ny_dates_30

plt.figure(figsize=(15,7))
plt.bar(x=ny_dates_30, height=ny_new_cases_30, color='red')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(15,7))
plt.bar(x=ny_dates_30, height=ny_deaths_30, color='blue')
plt.xticks(rotation=90)
plt.show()

"""# Comparing Covid 19 data with different states

Let's compare the Covid 19 cases after July for states: New York, California, Florida, Texas, Arizona
"""

states = ['New York', 'California','Florida', 'Texas','Arizona']

plt.figure(figsize=(15,7))
for state in states:
  df_st = df[(df['state']==state) & (df['date']>='2020-11-01')]
  plt.plot(df_st['date'],
           df_st['cases'],
           linewidth=2
           )
  plt.xticks(rotation=90)
plt.legend(states)
plt.show()

"""# Conclusion

Below are the conclusions:



1.   Conclusion 1
     --Your text here
2.   Conclusion 2
     --Your text here>
"""

# This data is up-to-date as of 2022-01-12. As of 2022-01-12, there is a total of 4,299,066 COVID cases since the first case on 2020-03-14. In terms of death, there is a total of 60638 deaths from COVID in NY. The first death took place on 2020-03-14. From the bar graph of NY COVID data, we can see a gradual growth in cases, as shown by the orange bars. They are significanly higher than death counts, as shown by the green bars. Examining daily new cases in NY, we see that there were 3 climatic points where the new cases are at its highest before the cases begin to decline. The first point is about 10,000 new cases in a single day, second is about 20,000 new cases. Currently, the cases seem to be at its highest point, with over 80,000 new cases in a single day.If we look closely at the data of new cases in NY within the last 30 days, we noticed that there is unreported data during 2021-12-25. After 2021-12-26, the cases had fluctuate between 40,000 to about 85,000 cases a day. On the other hand, we can observe a slow rise in daily deaths in NY in the last 30 days. In comparison to 5 US states (NY, CA, FL, TX, AZ), we can examine a similar trend in all five states in terms of slow growth and faster growth periods in COVID cases. In general, CA has the highest overall cases while AZ had the lowest overall cases of the 5 states we are examining. After 2020-11-01, the cases for all five states are increasing steadily.

# Group 2: Emily Chiu, Kevin Chong, Qianbing Chen