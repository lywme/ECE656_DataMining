## Yelp Project Report

## ECE 656 

#### Group member 1:   UW ID:20676607    WatIAM: m95yang     Name: Min Yang
#### Group member 2:   UW ID:20759952    WatIAM: y2593li        Name: Yewei Li

#### 1. Introduction


In this project, we analyze the data in the Yelp database to infer 3 different pieces of information beyond the raw data.

We implement the decision tree algorithm in one of our project functions and the experiment is conducted with 3 main following steps:
First, we conduct data cleaning (including sanity checking, check completeness and consistency of data) through the whole database. Then we use some data mining algorithms like decision tree classifier to generate the correlation between the data and its attributes. Lastly, within this step, we divide all the data to the Training set and Test set to validate the accuracy on the decision tree we created. In addition, a graphical user interface (GUI) is implemented to visualize the client-side.

For the purpose of minimizing network traffic, we use a stored procedure instead of a chunk of lines of SQL statements and client/server pattern to implement our project. We use socket to connect client and server applications, pass parameters to server side(we assume that there is an Application Server located with the DB server) and server-side just returns the result of different data mining methods.
#### 2. Data preprocessing

There are 8 entities in this database: business, business_categories, checkin, review, tip, user, user_elite, user_friends. 


##### 2.1. Data cleaning: 1_YelpClean.sql

Before analysis the data, we should implement sanity checking and consistency check, which include as follows:

(1) Check no user/review/tip is before Yelp's foundation(2004-06-01) or in the upcoming future.

the SELECT query expected to return an empty set. Otherwise, we use DELETE clause to delete the corresponding rows.


(2) The business_id and user_id in `review` table must already be exist in corresponding `business` table and `user` table. In the similar way, the user_id in `user_elite` table must already be exist in `user` table.

(3) The year in user_elite table must be less than the yelping_since in user table 


#### 3. Data Analysis: Decision_tree.py

### 3.1 see 2_PlotRatingTrend.py
Q: Bases on the data, which business are declining and which are improving in their ratings?
A: Change the user_id in config.py could see which business are declining and which are improving.

select date, avg(stars) as avg_stars from review 
where business_id = 'wYuPafwLYItJAHFVba9mVg' 
group by date order by date;

### 3.2 see 3_DecisionTree.py
We use decision_tree classifier as the data mining algorithm. And user can change the percentage of validation dataset through the GUI interface.

SELECT B.business_id,U.user_id as user_id,B.stars as other_rate_this_business,
U.average_stars as this_rate_all_business,R.stars as this_rate_this_business
FROM business as B INNER JOIN review as R using (business_id)
INNER JOIN `user` as U using (user_id)
order by B.business_id;


### 3.3 see 4_ReviewLenEffect.py
Q: Does review length affect how other users perceive a review?
A: Graph(4_ReviewLenEffect.png) show that length review on 4000 has the outmost impact on users perceive the data.

select CHAR_LENGTH(text) as review_len,(useful+funny+cool) as user_read from review;


#### 4. Applications for users GUI.py
GUI.py allows user to interact and participate through icons and sidebars in determine the config parameters, such as training data and test set segmentation, whether to do data cleaning, the business_id and choose which data analysis function s/he prefers to interact.

#### 5. Running Environment
Some settings(server address, port, password, etc.) is stored in the config.py and can be changed with GUI
The project works for all the OS including Linux, Windows as well as Mac OS...
The following environment is needed:
Python 3.6 above (with PyQT5, pymysql Libraries)
MySQL 5.6 above

#### 6. Description of each file
GUI.py   Graphical User Interface, executable graphical interface running as client.
1_YelpClean.sql    contains all the data cleaning sql statement
2_PlotRatingTrend    function that predict Business Rating Trend
3_DecisionTree      function for our decision tree algorithm and validation method
4_ReviewLenEffect    function that to predict the review length
client.py     Command Line Interface to connect to Server app
Server.py     Server app running on Application Server
config.py      Store all the settings
ALL The rest files are some figure we generated with our project
