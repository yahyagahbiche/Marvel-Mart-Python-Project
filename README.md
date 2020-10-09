# Marvel Mart Python Project
In this project, I worked on cleaning data, ran some computations using functions, and performed cross-reference statistics of 50,000 dataset
The libraries that I used were: **Numpy** and **Pandas**. 
For this project I used **for** and **while** loops, dictionaries, funcitons, lists, file processing.  

## Part 1: Cleaning the data
It came to our attention that some of the data was either incorrectly entered or missing entirely! This is going to throw off our calculations if it is left unchecked. We were grateful to discover none of it happened in our accounting columns of the data for that would be very detrimental but we aren't sure where the missing/incorrect data is elsewhere. Here's what we do know to help your investigation into finding the missing/incorrect data. Of the columns that we have, we know the missing/incorrect data comes from these columns:
- Country (either missing OR will be a number as a string)
- Item Type (either missing OR won't be a valid Item Type from the other ones listed)
- Order Priority (either missing OR won't be a valid priority code)
- Order ID (either missing OR won't be a number)

If you find incorrect/missing data and its text type for that column, change it to NULL. If you find incorrect/missing data and its a number type for that column, change it to 0. (or 0.0 if its a float). Test for missing values FIRST then if you find the ones that are missing, you don't have to test those for incorrect values. You need to change the values, then rewrite to a new CSV file called Marvel_Mart_Sales_clean.csv so it can be used later with the correct values.

## Part 2: General Statistics
First, we would like you to get us some general statistics from the data. I suggest you create a dictionary of lists with the keys being the heads of the CSV file and the list attached to it being all of the values for that heading. Duplicates should be included here.
1.	Produce the following and write it to a text file called Marvel_Mart_Rankings.txt. Be sure to use append so that you can append data rather than writing over top of the previous data. Be sure to include a newline between each append to the file. When writing to the file, please output in a text form such as:

Countries Most Sales:
- Country 1: (sales number)
- Country 2: (sales number)
...
(Answer question) "The country we should build our shipping center is ______ because ____..." 

- **A.** We want to know which countries we sell the most to so we can pick a new location to build a shipping center. Rank the Top 10 countries we sell to the most to least along with the number of sales we've had with that country. We have shipping centers in Trinidad and Tobago, Guinea, and Maldives right now. Which country should we build a shipping center in based on most sales and lack of shipping center? Please justify your reasoning.

- **B.** Provide a count for how many online and offline orders we take. Which do we take more of? You do not need to justify your answer.

- **C.** Rank the top 3 years we did the most sales (brought in most profit) in to the least sales. (Just the years, not the whole dates).  Use the Order Date, not the Ship Date. Please list the years and the amount sold. Answer the question "Which year did we sell the most in?"

(Note from instructor: doing large number sums with floats in Python usually produces scientific notation but we don't want that. You can turn that off by putting the following line under the import statements at the start of the script: pd.set_option('display.float_format', lambda x: '%.3f' % x)

2.	Now you will save these calculations below to a text file called Marvel_Mart_Calc.txt. When writing to the file, please output format such as:

Sums:
Units Sold: (Number)
Unit Cost: (Number)
Total Revenue: (Number)
Total Cost: (Number)
Total Profit: (Number)
(Newline)
Averages:
Units Sold: (Number)
...
(Newline)
Maximums:
Units Sold:
...

- **A** Produce the data above for the sum of each one.
- **B.** Produce the data above for the average of each one. (Average Units Sold, Average Cost, etc)
- **C.** Produce the data above for the maximum of each one. (Max Units Sold, Max Cost, etc.)

