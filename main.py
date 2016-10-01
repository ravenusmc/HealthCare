#This is the main file for the program. 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime

from valid import *

#This function is what will launch the entire program.
def main():
    print("\033c")
    print("-------------------------------------------------")
    print("------Welcome to HealthCare Cost Information-----")
    print("Our Goal is to help you find cost effective care!")
    print("-------------------------------------------------")
    input("Press Enter for the main menu ")
    main_menu()

#This function provides the main menu to the program. 
def main_menu():
    print("\033c")
    print("1. Look for cheapest cost in your area ")
    choice = int(input("What is your option: "))
    while not main_menu_valid(choice):
        print("That option is not allowed.")
        choice = int(input("What is your option: "))
    if choice == 1:
        cheapestCost()

#This function finds the cheapest cost based on the area and the condition the indiviudal enters. However, 
#the problem is that the condition uses the DRG codes which are medical/technical terms and I need a way
#That the lay person can type in a condition and it is matched up to the DRG code.
def cheapestCost():
    #The data is pulled and set equal to health_data
    health_data = pd.read_csv("inpatientCharges.csv")
    print("\033c")
    state = input("What is your state: ")
    issue = input("What is your issue: ")
    cost = int(input("What is the cost that you are looking for: "))
    #Here the data will be sorted out to only find the information for that state the user wants to see.
    state_data = health_data[(health_data.ProviderState == state)]
    #This further seperatates out the data for only what the user wants to see.
    issue_data = state_data[state_data.DRGDefinition.str.contains(issue.upper())]
    #At this point I have to convert a column to a float, it is an object, and then I have to get rid of the $ sign.
    #Once that is done, the data will be pulled that is below a specific value.
    matches = issue_data[issue_data.AverageTotalPayments.str.extract(r'.*?(\d+\.*\d*)', expand=False).astype(float) <= cost]
    print("Here are the matches for your criteria: ")
    #The data is displayed which matches the state, issue and less than cost. 
    print(matches)
    quit_main_menu()

### Functions that are not critical to the running of the program:

#This function will allow the user to choose to head back to the main menu or quit the program. 
def quit_main_menu():
    print("1. Main Menu")
    print("2. Quit")
    selection = int(input("What is your choice: "))
    while not quit_main_menu_valid(selection):
        print("That selection is not valid!")
        selection = int(input("What is your choice: "))
    if selection == 1:
        main_menu()
    elif selection == 2:
        print("Sorry to see you leave!")
        print("Please come again!")


main()