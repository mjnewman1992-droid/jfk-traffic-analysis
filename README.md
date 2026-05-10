# JFK Traffic Analysis

This project is a Python data visualization analysis of passenger traffic at John F. Kennedy International Airport (JFK). It compares annual passenger volume across airport terminals and visualizes how passengers arrived at JFK in 2024 using bar and pie charts.

## Project Overview

The goal of this project is to explore airport traffic patterns at JFK by looking at:

- passenger volume by terminal
- each terminal's share of total airport traffic
- estimated daily passenger averages
- transportation mode share for how passengers arrived at the airport

The project uses manually defined traffic and transportation data, then transforms that data into pandas DataFrames for analysis and visualization.

## Features

- Bar chart comparing annual passenger counts by terminal
- Pie chart showing transportation mode share
- Calculation of total airport passenger volume
- Calculation of percentage share by terminal
- Calculation of average daily passengers by terminal

## Tools Used

- Python
- pandas
- numpy
- matplotlib

## File

- `jfk_traffic.py` — main Python script for the analysis and visualizations

## Output

The script produces:

- a printed dataframe showing terminal passenger counts, percent share, and daily average
- a bar chart of passenger volume by terminal
- a pie chart of transportation mode percentages

## Example Questions This Project Explores

- Which JFK terminal handled the most passengers in 2024?
- What share of total airport traffic came from each terminal?
- How do passengers most commonly get to JFK?
- What is the estimated average daily passenger load by terminal?

## Future Improvements

- Replace hardcoded values with a CSV or live dataset
- Add more airport traffic metrics
- Improve chart styling and formatting
- Build an interactive dashboard version
- Compare multiple years of passenger traffic

## Author

Michael Newman
