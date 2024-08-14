from tkinter import *
from tkinter import messagebox, ttk
import random

# Create window, title it and size it.
main_window = Tk()
main_window.title('Party Items Hired')
# Scale up window in case the screen resolution makes it harder to see
main_window.tk.call('tk', 'scaling', 1.8)

# Creates random receipt number to print
def generate_receipt_num():
    global receipt
    receipt = random.randint(100000000, 999999999)

def get_data():
    global Name, Item, Item_count, Nameerror, Itemerror, Item_counterror
    Name = Name_entry.get().title()
    Item = Item_entry.get()
    Item_count = Item_count_entry.get()
    
    # Create blank variables which will be turned into error messages if there is an error
    Nameerror = ''
    Itemerror = ''
    Item_counterror = ''
    
    if not Name.replace('-', '').replace(' ', '').isalpha() or Item == '' or int(Item_count) <= 0 or int(Item_count) > 500:
        if Name == '':
            Nameerror = 'Must enter customer name'
            
        elif not Name.replace('-', '').replace(' ', '').isalpha():
            Nameerror = 'Name must only include letters, with the exception of a dash.'
        if Item == '':
            Itemerror = 'Item must be selected'
            
        if Item_count == '':
            Item_counterror = 'Item amount must be entered'
            
        elif not Item_count.isdigit() or int(Item_count) < 0 or int(Item_count) > 500:
            Item_counterror = 'You must chosse an item amount between 1 and 500'
        messagebox.showerror('Error', f'''Invalid input.
{Nameerror}
{Itemerror}
{Item_counterror}''')
        return
    
    # If everything is valid, print and save the data
    if Name.replace('-', '').replace(' ', '').isalpha() and Item != '' and 0 < int(Item_count) <= 500:
        generate_receipt_num() #generates new receipt number so each customer has a unique one
        display(Name, Item, Item_count, receipt)
        save_data()

# Create a display row and a list for data entries so that each customer has a unique line and data for their inputs
display_row = 6
user_info = []

def display(Name, Item, Item_count, receipt):
    global display_row
    # Create variable to store all user inputs
    user_inputs = []
    # Customer info
    customerlbl = Label(text=f'Customer: {Name}', fg='blue')
    customerlbl.grid(column=0, row=display_row, pady=5, padx=2)
    user_inputs.append(customerlbl)

    # Item info
    itemlbl = Label(text=f'Item: {Item}', fg='blue')
    itemlbl.grid(column=1, row=display_row, pady=5, padx=2)
    user_inputs.append(itemlbl)

    # Item amount info
    item_amountlbl = Label(text=f'Item Amount: {Item_count}', fg='blue')
    item_amountlbl.grid(column=2, row=display_row, pady=5, padx=2)
    user_inputs.append(item_amountlbl)

    # Receipt info
    receiptlbl = Label(text=f'Receipt: {receipt}', fg='blue')
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

def delete_row():
    row_selected = int(Delete_row_num.get()) - 1
    if 0 <= row_selected < len(user_info):
        # Remove user data from display
        for info in user_info[row_selected]:
            info.grid_forget()
        # Remove data from row
        user_info.pop(row_selected)
        # Adjust rows
        for i in range(row_selected, len(user_info)):
            for info in user_info[x]:
                info.grid(row=6 + x)
            display_row -= 1
    else:
        messagebox.showerror('Error', 'Must input valid row number.')

    
# Button Labels function
def Labels():
    Customerlbl = Label(main_window, text='Customer:').grid(column=0, row=1, pady=5, padx=5, sticky='e')
    Itemlbl = Label(main_window, text='Item Hired:').grid(column=0, row=2, pady=5, sticky='e')
    Item_countlbl = Label(main_window, text='Item Amount:').grid(column=0, row=3, pady=5, padx=5, sticky='e')    

# Create the entry points for user to type in name, item, and how many of the item they have hired
def Entries():
    global Name_entry, Item_entry, Item_count_entry, Delete_row_num
    Name_entry = Entry(main_window, width=12)
    Name_entry.grid(column=1, row=1, pady=5, padx=5, sticky='w')
    
    Item_entry = ttk.Combobox(main_window, width=10, values=['Clown', 'Streamers', 'Entertainer', 'Party Hats', 'Cups', 'Alcohol'])
    Item_entry.grid(column=1, row=2, pady=5, padx=5, sticky='w')
    Item_entry['state'] = 'readonly'
    
    Item_count_entry = Entry(main_window, width=12)
    Item_count_entry.grid(column=1, row=3, pady=5, padx=5, sticky='w')

    Delete_row_num = Spinbox(main_window, from_=1, to=100, width=5)
    Delete_row_num.grid(column=4, row=3, pady=5, padx=5, sticky='e')

# Buttons function
def Buttons():
    global btnQuit, btnSubmit, btnDelete
    
    btnQuit = Button(main_window, text='Quit', command=quit)
    btnQuit.grid(column=5, row=1, pady=5, padx=5, sticky='e')
    
    btnSubmit = Button(main_window, text='Submit', command=get_data)
    btnSubmit.grid(column=5, row=2, pady=5, padx=5, sticky='e')
    
    btnDelete = Button(main_window, text='Delete Row', command=delete_row)
    btnDelete.grid(column=5, row=3, pady=5, padx=5, sticky='e')

# Call all functions        
def main():
    Labels()
    Entries()
    Buttons()
    
# Call main function
main()
main_window.mainloop()
