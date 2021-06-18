# sqlalchemy-challenge
Using SQLAlchemy and Flask to create a Hawaii weather database for 2016-2017.

# Analyzing a years worth of climate data with a json Flask app

This repository uses SQLAlchemy to filter temperature and precipitation data from Hawaii weather stations. Selecting the final years worth of data (8-2016 to 8-2017), it adds that data to a pandas data frame and plots the years worth of precipitation data with Matplotlib. 

![Image of one year precipitation data]
(https://github.com/jshapi16/sqlalchemy-challenge/blob/main/Images/year_precip_data.png?raw=true)

In addition, for the station with the most number of records (filter the station by count), it gives average temperature data including min and max temperature data for the station with the most records. 

# Flask
The last part of this project jsonifies the SQLAlchemy data and creates a Flask app so anyone could pull the needed data for future use. 
