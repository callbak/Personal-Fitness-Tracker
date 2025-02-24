import pandas as pd
import plotly.express as px

# Read in the dataset, Store the result in a data frame --
fitness_data = pd.read_csv("fitness_data.csv")
print(fitness_data)

# Check for missing values --
missing_values = fitness_data.isnull().sum()
if missing_values.sum()==0:
    print("There is no missing values in the dataset.")
else:     
    print(missing_values)
    ## Which rows have missing values
    missing_values_rows = fitness_data[fitness_data.isnull().any(axis=1)]
    print(missing_values_rows)

# Exploring the data --
## Summary statistics
summary_statistics = fitness_data.describe()
print(summary_statistics)

## Check types of each column
data_types = fitness_data.dtypes
print(data_types)

## Convert the date column to a datetime format
fitness_data['date'] = pd.to_datetime(fitness_data['date'])

# Creating useful new columns --
## Rename some columns to more convenient names
fitness_data.rename(columns={'weight':'body_weight_kg','workout_duration':'workout_duration_minutes'}, inplace=True)

## Adding new columns
fitness_data['weight_lbs'] = fitness_data['body_weight_kg'] * 2.20462
fitness_data['day_of_week'] = fitness_data['date'].dt.day_name()
fitness_data['weekend'] = fitness_data['day_of_week'].isin(['Saturday','Sunday'])
fitness_data['sleep_debt'] = fitness_data['sleep_hours'] - 7.5
fitness_data['cumulative_sleep_debt'] = fitness_data['sleep_debt'].cumsum()

print(fitness_data)

# Visualizing trends across single and multiple variables --
## Visualize the number of steps frequency
fig = px.histogram(fitness_data,x='steps',nbins=30,title='Number of steps frequency')
fig.update_layout(xaxis_title='Number of steps', yaxis_title='Frequency', bargap=0.1)
fig.show()

## Line chart for the number of steps overtime, marking the weekends
fig = px.line(fitness_data,x='date',y='steps',title='Number of steps over time')
weekend_data=fitness_data[fitness_data['weekend']]
fig.add_scatter(x=weekend_data['date'], y=weekend_data['steps'], mode='markers', name='Weekend', marker=dict(color='red', size=8))
fig.update_layout(xaxis_title='Date', yaxis_title='Number of steps')
fig.show()

## Visualize the distribution of calories burned
fig = px.histogram(fitness_data,x='total_calories_burned',nbins=30,title='Histogram fo Total Calories Burned')
fig.update_layout(xaxis_title='Total Calories Burned', yaxis_title='Frequency', bargap=0.1)
fig.show()

## Line chart for the number of calories burned overtime, marking the weekends
fig = px.line(fitness_data,x='date',y='total_calories_burned',title='Number of calories burned over time')
weekend_data=fitness_data[fitness_data['weekend']]
fig.add_scatter(x=weekend_data['date'], y=weekend_data['total_calories_burned'], mode='markers', name='Weekend', marker=dict(color='red', size=8))
fig.update_layout(xaxis_title='Date', yaxis_title='Total Calories Burned')
fig.show()

## Visualize weight trend over time
fig = px.line(fitness_data,x='date',y='body_weight_kg',title='Weight Trend Over Time')
fig.update_layout(xaxis_title='Date',yaxis_title='Weight (kg)')
fig.show()

## Visualize sleep metrics over time
fig = px.line(fitness_data,x='date',y='sleep_hours',title='Sleep Over Time')
fig.update_layout(xaxis_title='Date',yaxis_title='Sleep Hours')
fig.show()

## Comparing sleep hours in weekdays and weekends
fig = px.box(fitness_data,x='weekend',y='sleep_hours',title='Sleep Hours : Weekdays vs. Weekends')
fig.update_layout(xaxis_title='Weekend(True/False)',yaxis_title='Sleep Hours')
fig.show()

## Visualize average sleep by day of week
fig = px.bar(fitness_data.groupby('day_of_week')['sleep_hours'].mean().reset_index(),x='day_of_week',y='sleep_hours',title='Average Sleep by Day of Week')
fig.update_layout(xaxis_title='Day of Week',yaxis_title='Sleep Hours')
fig.show()

## Visualize Number of steps vs. Calories burned
fig = px.scatter(fitness_data,x='steps',y='total_calories_burned',title='Number of Steps vs. Calories Burned')
fig.update_layout(xaxis_title='Number of Steps',yaxis_title='Number of Calories Burned')
fig.show()

## Visualizing how many different workout types are in the dataset
num_workout_types = fitness_data['workout_type'].nunique()
print(num_workout_types)

## Visualizing trends across workout types
fig = px.box(fitness_data,x='workout_type',y='workout_duration_minutes',title='Workout Duration by Type')
fig.update_layout(xaxis_title='Workout Type',yaxis_title='Wokrout Duration (Minutes)')
fig.show()