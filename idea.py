import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


#First goal: Make a function that tells the user the lowest cost by zip code

#Will need to ask the person for their STATE -DONE
#Will need to ask the person for their medical condition
#I may want to have show the user what type of medical conditions that come up with what they want because 
#there many matches may come up. Thus the user will be presented with a list based on what they typed in 
#Which will further be refined. 

#May want to sort data by lowest to higher or just show them the highest value?
#Then I will take those two pieces of information and show them locations near them. 

#CHECKING DATA TYPES: 
#print(health_data['AverageCoveredCharges'].dtype)

health_data = pd.read_csv("inpatientCharges.csv")
# print(health_data.head()) 

issue = input("What is your issue: ")
print((health_data[health_data.DRGDefinition.str.contains(issue)]))

#Seeing if something contains a particular value:
#print(orders.item_name.str.contains('Chicken'))
#To see the rows that only contain chicken:
#print(orders[orders.item_name.str.contains('Chicken')])



#My current issue is that I need to select a specific value within the DRGDefinition instead of the whole line.
#These two lines work! 
#state = input("What is your state: ")
# issue = input("What is your issue: ")
#print((health_data[(health_data.ProviderState == state) & (health_data.DRGDefinition == "039 - EXTRACRANIAL PROCEDURES W/O CC/MCC")]))

#print(health_data.loc[(health_data["ProviderState"]==state) & (health_data["AverageCoveredCharges"] >= "20000") ])
# & (data["Education"]=="Not Graduate") & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]])

#print((health_data["AverageCoveredCharges"] >= "1"), ["AverageCoveredCharges"] )




#print(movies[(movies.duration > 200) & (movies.genre == 'Drama')])
#Using or
#print(movies[(movies.duration > 200) | (movies.genre == 'Drama')])












##### TO read from the codes file.
# codes = pd.read_table("codes.csv")
# print(codes.head())