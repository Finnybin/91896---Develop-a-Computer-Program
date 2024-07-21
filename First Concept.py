from tkinter import *
import random

#create window and title it
main_window = Tk()
main_window.title('Party Items Hired')

main_window.geometry('900x400')
#scale up window in case the screen resolution makes it harder to see
main_window.tk.call('tk', 'scaling', 3.0)

#Button Labels function
def Labels():
    global item_count
    Customerlbl = Label(main_window, text='Customer:').grid(column=0, row=1)
    Receiptlbl = Label(main_window, text='Receipt Number:').grid(column=0, row=2)
    Itemlbl = Label(main_window, text='Item Hired:').grid(column=0, row=3)
    item_countlbl = Label(main_window, text='Item Amount:').grid(column=0, row=4)

#creates random receipt number to print
receipt_num = random.randint(0, 999999999)

#creates the entry points for user to type in name, item, and how many of the item they have hired
def Entries():
    global Name_entry, Item_entry, Item_count_entry
    Name_entry = Entry(main_window, width = 12).grid(column=1, row=1)
    Item_entry = Entry(main_window, width = 12).grid(column=1, row=2)
    Item_count_entry = Entry(main_window, width = 12).grid(column=1, row=3)
    receipt_display = Label(main_window, text=receipt_num).grid(column=1, row=4)

#Buttons function
def Buttons():
        btnQuit = Button(main_window, text='Quit', command = quit)
        btnQuit.grid(column=5, row=1)
        btnSubmit = Button(main_window, text='Submit')
        btnSubmit.grid(column=5, row=2)
        btnDelete = Button(main_window, text='Delete Row')
        btnDelete.grid(column=5, row=3)

#call all functions        
def main():
    Labels()
    Entries()
    Buttons()
    
#call main function
main()
