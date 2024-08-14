from tkinter import*
from tkinter import messagebox, ttk
import random

#create window,title it and size it. 
main_window = Tk()
main_window.title('Party Items Hired')
#scale up window in case the screen resolution makes it harder to see
main_window.tk.call('tk', 'scaling', 1.8)

#creates random receipt number to print
def generate_receipt_num():
    global receipt
    receipt = random.randint(100000000, 999999999)

def get_data():
    global Name, Item, Item_count, Nameerror, Itemerror, Item_counterror
    Name = Name_entry.get().title()
    Item = Item_entry.get()
    Item_count = Item_count_entry.get()
    
    #create blank variables which will be turned into error messages if there is an error
    Namerror = ''
    Itemerror = ''
    Item_counterror = ''
    
    #validation control
    if not Item_count.isdigit():
        messagebox.showerror('Error', f'''Invalid input.
Item count must be number
''')
    while not Name.replace('-', '').replace(' ', '').isalpha() or Item == '' or 0 > int(Item_count) > 500:
        if Name == '':
            Nameerror = 'Must enter customer name'
        elif not Name.replace('-', '').replace(' ', '').isalpha():
            Nameerror = 'Name must only include letters,  with the exception of a dash.'
        if Item == '':
            Itemerror = 'Item must be selected'
        if Item_count == '':
            Item_counterror = 'Item amount must be entered'
        messagebox.showerror('Error', f'''Invalid input.
{Nameerror}
{Itemerror}
{Item_counterror}''')
        break
    #print everything if it is valid
    if Name.replace('-', '').replace(' ', '').isalpha() and Item != '' and 0 < int(Item_count) < 500:
        display(Name, Item, Item_count)
    
#create a display row so that each customer has a different line for their inputs
display_row = 6
def display(Name, Item, Item_count):
    global display_row
    Label(text=f'Customer: {Name}', fg='blue').grid(column=0, row=display_row, pady=5, padx=2)
    Label(text=f'Item: {Item}', fg='blue').grid(column=1, row=display_row, pady=5, padx=2)
    Label(text=f'Item Amount: {Item_count}', fg='blue').grid(column=2, row=display_row, pady=5, padx=2)
    Label(text=f'Receipt: {random.randint(100000000, 999999999)}', fg='blue').grid(column=3, row=display_row, pady=5, padx=2)
    generate_receipt_num()
    display_row = display_row + 1

#Button Labels function
def Labels():
    global item_countlbl
    Customerlbl = Label(main_window, text='Customer:').grid(column=0, row=1, pady = 5, padx = 5, sticky='e')
    Itemlbl = Label(main_window, text='Item Hired:').grid(column=0, row=2, pady = 5, sticky='e')
    Item_countlbl = Label(main_window, text='Item Amount:').grid(column=0, row=3, pady = 5, padx = 5, sticky='e')    

#creates the entry points for user to type in name, item, and how many of the item they have hired
def Entries():
    global Name_entry, Item_entry, Item_count_entry
    Name_entry = Entry(main_window, width = 12)
    Name_entry.grid(column=1, row=1, pady = 5, padx = 5, sticky='w')
    Item_entry = ttk.Combobox( main_window, width = 10, values = ['Clown', 'Streamers', 'Entertainer', 'Party Hats', 'Cups', 'Alcohol'])
    Item_entry.grid(column=1, row=2, pady = 5, padx = 5, sticky='w')
    Item_entry['state'] = 'readonly'
    Item_count_entry = Entry(main_window, width = 12)
    Item_count_entry.grid(column=1, row=3, pady = 5, padx = 5, sticky='w')

#Buttons function
def Buttons():
    global btnQuit, btnSubmit, btnDelete
    btnQuit = Button(main_window, text='Quit', command = quit)
    btnQuit.grid(column=5, row=1, pady = 5, padx = 5, sticky='e')
    btnSubmit = Button(main_window, text='Submit', command=get_data)
    btnSubmit.grid(column=5, row=2, pady = 5, padx = 5, sticky='e')
    btnDelete = Button(main_window, text='Delete Row')
    btnDelete.grid(column=5, row=3, pady = 5, padx = 5, sticky='e')

#call all functions        
def main():
    Labels()
    Entries()
    Buttons()
#call main function
main()
