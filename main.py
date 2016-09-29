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
    input("Press Enter for the main menu")
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

def cheapestCost():
    print("\033c")
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
    if choice == 1:
        main_menu()
    elif choice == 2:
        print("Sorry to see you leave!")
        print("Please come again!")


main()