'''
Python Project - Marvel Mart Project
Yahya Gahbiche
2/28/2020
'''

# Part 1: Cleaning the data

#importing libraries and the formatting setting 
import pandas as pd
import numpy as np
import csv
pd.set_option('display.float_format', lambda x: '%.3f' % x)

#importing data
data = pd.read_csv("DataSamples/Marvel_Mart_Sales_Project_Master.csv", delimiter =',')

# cleaning Country column: Filling in cells that have float type with NULL
AllCountries = data["Country"]
for i in range(len(AllCountries)):
    try:
        conv = float (AllCountries[i])
        AllCountries[i] = "NULL"
    except:
        1==1

# Filling in empty cells of Countries with NULL
data['Country'] = data['Country'].fillna("NULL")

# Cleaning Item type column
data['Item Type'] = data['Item Type'].fillna("NULL")

# cleaning Order Priority column: Filling blank cells with NULL
data['Order Priority'] = data['Order Priority'].fillna("NULL")

# cleaning Order ID column: Replacing any incorrect cell values (strings) with NULL

data['Order ID'] = data['Order ID'].replace("Meat","NULL")
data['Order ID'] = data['Order ID'].replace("Snacks","NULL")
data['Order ID'] = data['Order ID'].replace("Fruits","NULL")
data['Order ID'] = data['Order ID'].replace("Cosmetics","NULL")

# save the file "data" into a csv:
data.to_csv('DataSamples/Marvel_Mart_Sales_clean.csv', index=False)

# Part 2: General Statistics

# Creating lists for each column
RegionList = []
for i in data['Region']:
    RegionList.append(i)
CountryList = []
for i in data['Country']:
    CountryList.append(i)
ItemTypeList = []
for i in data['Item Type']:
    ItemTypeList.append(i)
SalesChannelList =[]
for i in data["Sales Channel"]:
    SalesChannelList.append(i)
OrderPriorityList = []
for i in data["Order Priority"]:
    OrderPriorityList.append(i)
OrderDateList = []
for i in data["Order Date"]:
    OrderDateList.append(i)
OrderIDList = []
for i in data["Order ID"]:
    OrderIDList.append(i)
ShipDateList = []
for i in data['Ship Date']:
    ShipDateList.append(i)
UnitSoldList = []
for i in data["Units Sold"]:
    UnitSoldList.append(i)
UnitPriceList = []
for i in data['Unit Price']:
    UnitPriceList.append(i)
UnitCostList = []
for i in data['Unit Cost']:
    UnitCostList.append(i)
TotalRevenueList = []
for i in data['Total Revenue']:
    TotalRevenueList.append(i)
TotalCostList = []
for i in data['Total Cost']:
    TotalCostList.append(i)
TotalProfitList = []
for i in data['Total Profit']:
    TotalProfitList.append(i)
    
dictionaryStat = pd.DataFrame({"Region": RegionList,
                   "Country": CountryList,
                   "Item Type": ItemTypeList,
                   "Sales Channel": SalesChannelList,
                   "Order Priority": OrderPriorityList,
                   "Order Date": OrderDateList,
                   "Order ID": OrderIDList,
                   "Ship Date": ShipDateList,
                   "Units Sold": UnitSoldList,
                   "Unit Price": UnitPriceList,
                   "Unit Cost": UnitCostList,
                   "Total Revenue": TotalRevenueList,
                   "Total Cost": TotalCostList,
                   "Total Profit": TotalProfitList})

# 1 (A)
transactionCount = (dictionaryStat["Country"].value_counts().head(n=10))
print(transactionCount)
output = (f"Countries Most Sale Transactions:\nTrinidad and Tobago: 321\nGuinea: 318\nCape Verde: 315\nMaldives: 311\nFinland: 310\nDemocratic Republic of the Congo: 308\nSamoa: 306\nMalta: 305\nChina: 303\nFrance: 303")   
print(output)
shippingCenter = ("\n\nThe country we should build our shipping center is Cape Verde.\nGiven that we already have shipping centers in Trinidad and Tobago, Guinea, and Maldives (ranked top 1,2, and 4 respectively), \nCape Verde is the country ranked third with most transactions. ")                                    
with open("DataSamples/Marvel_Mart_Rankings.txt", "a+") as reader:
    reader.writelines("Question 1 (A):\n\n")
    reader.writelines(output)
    reader.writelines(shippingCenter)
with open("DataSamples/Marvel_Mart_Rankings.txt", "r") as reader:
    for line in reader:
        print(line, end = '')
#1 (B)

#Count of Online orders
        
countChannel = dictionaryStat["Sales Channel"].value_counts()  
print(countChannel)      

#final answer to 1 (B)
resultChannel = ("Online     25033\nOffline    24962")
final_answer = (f"\nWe take more online than offline orders.\n\n")

#writing final answer in the text file:
with open ("DataSamples/Marvel_Mart_Rankings.txt", "a+") as reader:
    reader.writelines("\n\nQuestion 1 (B):\n\n")
    reader.writelines(resultChannel)
    reader.writelines(final_answer)
with open ("DataSamples/Marvel_Mart_Rankings.txt", "r") as reader:
    for line in reader:
        print(line, end = '')

# 1 (C)

df = pd.DataFrame({"Order Date": OrderDateList, "Total Profit": TotalProfitList})
print(df)

convertDate = pd.to_datetime(df["Order Date"])
print(convertDate)
df['Year'] = convertDate.dt.year
print(df)

groupbyDate = df.groupby('Year')
top3years = groupbyDate.sum()
sortDates = top3years.sort_values('Total Profit', ascending = False)
top3years = sortDates.head(n=3)
print(top3years)

with open("DataSamples/Marvel_Mart_Rankings.txt", "a+") as reader:
    reader.writelines("Question 1 (C):\n\n")
    reader.writelines(f"{top3years}\n\n")
    reader.writelines("The highest profit generated by sales was in made in 2011 with the amount of $2,622,615,160.240.")
with open("DataSamples/Marvel_Mart_Rankings.txt", "r") as reader:
    for line in reader:
        print(line, end = '')

#2 
        
#Sums
        
UnitSold_sum = sum(UnitSoldList)

UnitCost_sum = sum(UnitCostList)
UnitCostrounded_sum = round(UnitCost_sum,2)

TotalRevenue_sum = sum(TotalRevenueList)
TotalRevenuerounded_sum = round(TotalRevenue_sum, 2)

TotalCost_sum = sum(TotalCostList)
TotalCostrounded_sum = round(TotalCost_sum, 2)

TotalProfit_sum = sum(TotalProfitList)
TotalProfitrounded_sum = round(TotalProfit_sum, 2)

results1 = (f"Sums:\nUnits Sold: {UnitSold_sum}\nUnit Cost: ${UnitCostrounded_sum}\nTotal Revenue: ${TotalRevenuerounded_sum}\nTotal Cost: ${TotalCostrounded_sum}\nTotal Profit: ${TotalProfitrounded_sum}\n")
print(results1)


#Averages
UnitSold_avg = UnitSold_sum / len(UnitSoldList)
UnitSoldrounded_avg = round(UnitSold_avg,2)

UnitCost_avg = UnitCost_sum/ len(UnitCostList)
UnitCostrounded_avg = round(UnitCost_avg, 2)

TotalRevenue_avg = TotalRevenue_sum / len(TotalRevenueList)
TotalRevenuerounded_avg = round(TotalRevenue_avg, 2)

TotalCost_avg = TotalCost_sum / len(TotalCostList)
TotalCostrounded_avg = round(TotalCost_avg, 2)

TotalProfit_avg = TotalProfit_sum / len(TotalProfitList)
TotalProfitrounded_avg = round(TotalProfit_avg, 2)

results2 = (f"\nAverages:\nUnits Sold: {UnitSoldrounded_avg}\nUnit Cost: ${UnitCostrounded_avg}\nTotal Revenue: ${TotalRevenuerounded_avg}\nTotal Cost: ${TotalCostrounded_avg}\nTotal Profit: ${TotalProfitrounded_avg}\n")
print(results2)

# Maximums

UnitSold_max = max(UnitSoldList)

UnitCost_max = max(UnitCostList)

TotalRevenue_max = max(TotalRevenueList)

TotalCost_max = max(TotalCostList)

TotalProfit_max = max(TotalProfitList)

results3 =(f"\nMaximums:\nUnits Sold: {UnitSold_max}\nUnit Cost: ${UnitCost_max}\nTotal Revenue: ${TotalRevenue_max}\nTotal Cost: ${TotalCost_max}\nTotal Profit: ${TotalProfit_max}\n")
print(results3)


with open("DataSamples/Marvel_Mart_Calc.txt", "a+") as reader:
    reader.writelines("Question 2:\n\n(A)\n\n")
    reader.writelines(results1)
    reader.writelines("\n(B)\n")
    reader.writelines(results2)
    reader.writelines("\n(C)\n")
    reader.writelines(results3)
with open("DataSamples/Marvel_Mart_Calc.txt", "r") as reader:
    for i in reader:
        print(i, end = '')

#Part 3: Cross-Reference Statistics

#Reading the Clean data, creating a dictionary and appending the countries in their appropriate regions
with open("DataSamples/Marvel_Mart_Sales_clean.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
   
    regiondict = {}
    for row in reader:
        if row["Region"] not in regiondict.keys():
            regiondict[row["Region"]] = []
        if row["Country"] not in regiondict.values():
            if row["Country"] not in regiondict[row["Region"]]:
                regiondict[row["Region"]].append(row["Country"])
                 
#writing the data in a CSV file      
with open("DataSamples/Countries_By_Region.csv", "w", newline = '') as csvfile:
    writer = csv.writer(csvfile)
    for k, v in regiondict.items():
        writer.writerow([k,v])

#The previous csv created did not have the correct format
#Therefore, it need to be transposed.

#Creating a variable that will transpose the data   
from itertools import zip_longest
data_transp = list(zip_longest(*regiondict.values()))

#writing the data in the same file Countries_By_Region but with the correct formatting
with open("DataSamples/Countries_By_Region.csv", "w+", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(regiondict.keys())
    for items in data_transp:
          writer.writerow(items)
    

    














      