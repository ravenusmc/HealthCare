#This file is were all of the validations will go for the program. 

def main_menu_valid(choice):
    if choice == 1:
        return True 
    else:
        return False 

def quit_main_menu_valid(selection):
    if selection == 1 or selection == 2:
        return True 
    else:
        return False 
