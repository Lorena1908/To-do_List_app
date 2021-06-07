from tkinter import *
from tkinter import filedialog
import pickle

root = Tk()
root.geometry('320x415')
root.iconbitmap('Tasks.ico')
root.title('To-Dos')

# MAIN FRAME
tasks_frame = Frame(root)
tasks_frame.pack()

# TASK LIST
tasks_list = Listbox(tasks_frame, width=25, height=10, font=(20), bd=0, bg='#F0F0F0')
tasks_list.pack(padx=10, pady=10)

# ENTRY
input_entry = Entry(root, width=45)
input_entry.pack(ipady=5, pady=7)

# FUNCTIONS
def add_item():
    tasks_list.insert(END, input_entry.get())
    input_entry.delete(0, END)

def delete_item():
    tasks_list.delete(ANCHOR) # It deletes only one item from the list
    tasks_list.selection_clear(0, END)

def delete_all():
    tasks_list.delete(0, END)

def cross_item():
    tasks_list.itemconfig(tasks_list.curselection(), fg='grey')
    tasks_list.selection_clear(0, END)

def uncross_item():
    tasks_list.itemconfig(tasks_list.curselection(), fg='black')
    tasks_list.selection_clear(0, END)

def delete_crossed_items():
    index = 0

    while index < tasks_list.size():
        if tasks_list.itemcget(index, 'fg') == 'grey':
            tasks_list.delete(index)
        else:
            index += 1

def save_list():
    file_name = filedialog.asksaveasfilename(initialdir='/Users/lorel/Desktop', title='Save File', filetypes=(('Dat files', '*.dat'), ('All Files', '*.*')))

    if file_name:
        if file_name.endswith('.dat'):
            pass
        else:
            file_name = f'{file_name}.dat'
        
        delete_crossed_items()

        tasks = tasks_list.get(0, END)

        out_file = open(file_name, 'wb')

        pickle.dump(tasks, out_file)

def open_list():
    file_name =filedialog.askopenfilename(initialdir='/Users/lorel/Desktop', title='Open File', filetypes=(('Dat files', '*.dat'), ('All Files', '*.*')))

    if file_name:
        file = open(file_name, 'rb')
        content = pickle.load(file)

        for item in content:
            tasks_list.insert(END, item)

# ADD MENUS
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu, tearoff=False) # tearoff removes the --- line at the top
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Save List', command=save_list)
file_menu.add_command(label='Open List', command=open_list)

# BUTTON FRAME
btn_frame = Frame(root)
btn_frame.pack()

# BUTTONS
add_item_btn = Button(btn_frame, text='Add Item', command=add_item)
add_item_btn.grid(row=0, column=0, pady=(10, 5), padx=5)

delete_item_btn = Button(btn_frame, text='Delete Item', command=delete_item)
delete_item_btn.grid(row=0, column=1, pady=(10, 5), padx=5)

delete_all_btn = Button(btn_frame, text='Delete All', command=delete_all)
delete_all_btn.grid(row=0, column=2, pady=(10, 5), padx=5)

cross_item_btn = Button(btn_frame, text='Cross Item', command=cross_item)
cross_item_btn.grid(row=1, column=0, pady=(5,10), padx=5)

uncross_item_btn = Button(btn_frame, text='Uncross Item', command=uncross_item)
uncross_item_btn.grid(row=1, column=1, pady=(5,10), padx=5)

delete_crossed_items_btn = Button(btn_frame, text='Delete Crossed Items', command=delete_crossed_items)
delete_crossed_items_btn.grid(row=1, column=2, pady=(5,10), padx=5)

root.mainloop()
