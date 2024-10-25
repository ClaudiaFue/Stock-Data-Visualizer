# Stock-Data-Visualizer
This is for Project 03 in INFOTC 4320
The Team is Scrum Team 6 with members Hesub, Livia, Claudia and Palmer
Claudia is the Scrum Master for this Project

# Scenario
A professor in your department is interested in tracking stock data trends and recently found the Alpha Vantage Links to an external site. website. This site offers an api that returns historical stock data from the past 20 years. The data is returned in json and other formats. There is no way to visualize the data or choose a date range to view the data. The api, by default, returns 20 years of data for all but one of its functions.

The team’s job is to create a python application that queries the Alpha Vantage api, and allows the user to select a date range to view the data, and the type of chart they want to view the data in.

# The application should:

* Ask the user to enter the stock symbol for the company they want data for.
* Ask the user for the chart type they would like.
* Ask the user for the time series function they want the api to use.
* Ask the user for the beginning date in YYYY-MM-DD format.
* Ask the user for the end date in YYYY-MM-DD format.
* The end date should not be before the begin date
* Generate a graph and open in the user’s default browser.
 
