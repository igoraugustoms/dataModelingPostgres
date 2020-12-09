# Heading Purpose

The purpose of this project is to help an imaginary startup called Sparkify. The company wants to analyze data they've been collecting on songs and user activity on their music app. The goal is to undestand what songs users are listening to. 

To do that, I created a star schema model. The fact table is called songlplays and contains records in log data associated with song plays. To filter that, we defined four dimension tables: 

Users - Data about users in their platform  

Songs - Songs in their app  

Artists - Artists who have songs en their app  

Time - Dimension that has start time, hour, day, week, month, yeark and weekday.   

All the data comes from two JSONs logs. One has logs on user, and the other has metadata on the songs. 

The ETL pipeline builds first dimensions. After that, it's necessary to use artists table, songs table and the JSON data to build the fact table. 

An example of query: SELECT level, count * FROM PLAYSONGS GROUP BY level ORDER BY 2 DESC

How to execute project: First, you need to open create_tables.py and check host, dbname, user and password. After that, you should execute create_tables.py on terminal. This file will create and connect with database sparkifydb. Then, will create all dimensions and fact table  

Then, you should execute sql_queries.py on terminal. This file makes ETL process. It reads all JSONs files at filepath data/song_data and data/log_data. 

You shouldn't run sql_queries.py. This is only an auxiliary file that contains some queries used by etl.py 

The file test.ipynb connects with sparkifydb. There, you can rull the cells and test if all the data were inserted.

You shouldn't concern about etl.ipynb. There, you can find the same steps at etl.py. I've used ETL.ipynb only to create the logic before implementation.

You can find all logs at folder data.