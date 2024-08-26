# Author: Finn Toby Hall
# Date: 19/08/2024
# Purpose: To create a program for Julie's party hire so that customer orders can be stored and tracked.

from tkinter import *
from tkinter import messagebox, ttk
import random
import ast
import os

# Create window, title it and size it.
main_window = Tk()
main_window.title('Party Items Hired')

# Change background colour
main_window.config(bg = '#fff6d2')
# Scale up window in case the screen resolution makes it harder to see
main_window.tk.call('tk', 'scaling', 1.8)

# Styling for most widgets
style = ttk.Style()
style.configure('TLabel',
                foreground='#957000',
                background='#fff6d2',
                font=('Calibri', 10))
style.configure('TButton',
                foreground='#a57c00',
                background='#fff6d2',
                font=('Calibri', 10))

# Create a display row and a list for data entries so that each customer has a unique line and data for their inputs
display_row = 6
user_info = []

# Creates random receipt number to print
def generate_receipt_num():
    global receipt
    
    # Create a file to store the most recent receipt number
    receipt_file = 'latest_receipt_number.txt'
    # Create a file to store all the aleady used receipt numbers
    used_file = 'used_receipts.txt'

    # Give the used numbers a value
    used_numbers = set()

    # Validate if file exists
    if os.path.exists(used_file):
        # Read the last used number
        with open(used_file, 'r') as file:
            used_numbers = set(line.strip() for line in file)

        # Make a random number that isn't in the used file
    while True:
        new_latest_number = random.randint(100000000, 999999999)
        if str(new_latest_number) not in used_numbers:
            receipt = new_latest_number
            break

    # Add new number to the used numbers file
    with open(used_file, 'a') as file:
        file.write(f'{receipt}\n')

    # Save new number so that is the new latest number
    with open(receipt_file, 'w') as file:
        file.write(str(new_latest_number))

def get_data():
    global Name, Item, Item_count, Nameerror, Itemerror, Item_counterror
    Name = Name_entry.get().title()
    Item = Item_entry.get()
    Item_count = Item_count_entry.get()
    
    # Create blank variables which will be turned into error messages if there is an error
    Nameerror = ''
    Itemerror = ''
    Item_counterror = ''

    #Validate Name entry
    if Name == '':
        Nameerror = 'Must enter customer name'
    elif not Name.replace('-', '').replace(' ', '').isalpha():
        Nameerror = 'Name must only include letters, with the exception of a dash.'

    #Validate Item entry
    if Item == '':
        Itemerror = 'Item must be selected'

    #Validate Item Count Entry
    if Item_count == '':
        Item_counterror = 'Item amount must be entered'
    elif not Item_count.isdigit() or int(Item_count) < 0 or int(Item_count) > 500:
        Item_counterror = 'You must chosse an item amount between 1 and 500'

    #Check for errors(this is incase there is a blank input into a spinbox)
    if Nameerror or Itemerror or Item_counterror:
            messagebox.showerror('Error', f'''Invalid input.
{Nameerror}
{Itemerror}
{Item_counterror}''')
    
    
    # If everything is valid, print and save the data
    if Name.replace('-', '').replace(' ', '').isalpha() and Item != '' and 0 < int(Item_count) <= 500:
        generate_receipt_num() # Generates new receipt number so each customer has a unique one
        display(Name, Item, Item_count, receipt)
        save_data()

def display(Name, Item, Item_count, receipt):
    global display_row
    # Create variable to store all user inputs
    user_inputs = []
    # Customer info
    customerlbl = ttk.Label(text=f'Customer: {Name}')
    customerlbl.grid(column=0, row=display_row, pady=5, padx=2)
    user_inputs.append(customerlbl)

    # Item info
    itemlbl = ttk.Label(text=f'Item: {Item}', style='TLabel')
    itemlbl.grid(column=1, row=display_row, pady=5, padx=2)
    user_inputs.append(itemlbl)

    # Item amount info
    item_amountlbl = ttk.Label(text=f'Item Amount: {Item_count}', style='TLabel')
    item_amountlbl.grid(column=2, row=display_row, pady=5, padx=2)
    user_inputs.append(item_amountlbl)

    # Receipt info
    receiptlbl = ttk.Label(text=f'Receipt: {receipt}', style='TLabel')
    receiptlbl.grid(column=3, row=display_row, pady=5, padx=2)
    user_inputs.append(receiptlbl)

    # Store the inputs into the info variable
    user_info.append(user_inputs)
    # Create new row
    display_row += 1

# Save user info to a data file
def save_data():
    entries = [Name, Item, Item_count, receipt]
    with open('user_data.txt', 'a') as file:
        file.write(f'{entries}\n')

# Load the user info from the file I have created
def load_data():
    try:
        with open('user_data.txt', 'r') as file:
            for line in file:
                # Seperate the lines by commas so that each order can be picked out (had to import ast as it is the only reliable way I could find to strip characters
                entries = ast.literal_eval(line.strip())
                # Displays the entries as sets of 4 variables (there are 4 pieces of information stored per order)
                if len(entries) == 4:  
                    # Display the entries
                    display(entries[0], entries[1], entries[2], entries[3])
    except FileNotFoundError:
        #Just in case the file has not been created (when the program is first used)
        pass

def delete_data(row_number):
    try:
        # Access file and read the lines
        with open('user_data.txt', 'r') as file:
            lines = file.readlines()

        # Delete the row that is selected
        if 0 <= row_number < len(lines):
            lines.pop(row_number)
            
        # Rewrite the updated file so that the deleted order is gone
            with open('user_data.txt', 'w') as file:
                file.writelines(lines)
                                        
        else:
            messagebox.showerror('Error', 'That row number does not exist.')
    except FileNotFoundError:
        messagebox.showerror('Error', 'The file you are trying to access does not exist yet.')

def delete_row():
    global display_row
    # Make sure that the row selected is the correct one (it starts from 0 so 1 must be minused from the value
    row_selected = int(Delete_row_num.get()) - 1
    
    if 0 <= row_selected < len(user_info):
        # Remove user data from display
        for info in user_info[row_selected]:
            info.grid_forget()
        # Remove data from row
        user_info.pop(row_selected)
        # Remove data from file
        delete_data(row_selected)
        # Adjust rows
        for i in range(row_selected, len(user_info)):
            for info in user_info[i]:
                info.grid(row=6 + i)
            display_row -= 1
    else:
        messagebox.showerror('Error', 'Must input valid row number.')

    
# Button Labels function
def Labels():
    Customerlbl = ttk.Label(main_window, text='Customer:', style='TLabel')
    Customerlbl.grid(column=0, row=1, pady=5, padx=5, sticky='e')
    
    Itemlbl = ttk.Label(main_window, text='Item Hired:', style='TLabel')
    Itemlbl.grid(column=0, row=2, pady=5, sticky='e')
    
    Item_countlbl = ttk.Label(main_window, text='Item Amount:', style='TLabel')
    Item_countlbl.grid(column=0, row=3, pady=5, padx=5, sticky='e')    

# Create the entry points for user to type in name, item, and how many of the item they have hired
def Entries():
    global Name_entry, Item_entry, Item_count_entry, Delete_row_num
    Name_entry = Entry(main_window, width=15)
    Name_entry.grid(column=1, row=1, pady=5, padx=5, sticky='w')
    
    Item_entry = ttk.Combobox(main_window, width=13, style='TCombobox', values=['', 'Clown', 'Streamers', 'Entertainer', 'Party Hats', 'Cups', 'Alcohol'])
    Item_entry.grid(column=1, row=2, pady=5, padx=5, sticky='w')
    Item_entry['state'] = 'readonly'

    Item_count_entry = Spinbox(main_window, from_=1, to=500, width=15)
    Item_count_entry.grid(column=1, row=3, pady=5, padx=5, sticky='w')

    Delete_row_num = Spinbox(main_window, from_=1, to=100, width=5)
    Delete_row_num.grid(column=3, row=3, pady=5, padx=5, sticky='e')

# Buttons function
def Buttons():
    global btnQuit, btnSubmit, btnDelete, bin_image
    
    btnQuit = ttk.Button(main_window, text='Quit', command=main_window.destroy, style='TButton')
    btnQuit.grid(column=3, row=1, pady=5, padx=5, sticky='e')
    
    btnSubmit = ttk.Button(main_window, text='Submit', command=get_data, style='TButton')
    btnSubmit.grid(column=2, row=3, pady=5, padx=5, sticky='w')
    
    btnDelete = ttk.Button(main_window, text=f'Delete Row', command=delete_row, style='TButton')
    btnDelete.grid(column=3, row=2, pady=5, padx=5, sticky='e')


# Call all functions        
def main():
    Labels()
    Entries()
    Buttons()
    load_data()
    
# Call main function
main()
main_window.mainloop()
