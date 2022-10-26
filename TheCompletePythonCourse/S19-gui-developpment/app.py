# --------------------------------------------------------------------------------------------------------------
# Hello World
# --------------------------------------------------------------------------------------------------------------
# import tkinter as tk
# from tkinter import ttk
#
#
# def greet():
#     print("Hello, world")
#
#
# root = tk.Tk()
# root.title("Hello")
#
# greet_button = ttk.Button(root, text="Greet", command=greet)
# greet_button.pack(side="left", fill="x", expand=True)
#
# quit_button = ttk.Button(root, text="Quit", command=root.destroy)
# quit_button.pack(side="left", fill="x", expand=True)
# root.mainloop()

# --------------------------------------------------------------------------------------------------------------
# Label and Fields
# --------------------------------------------------------------------------------------------------------------
# import tkinter as tk
# from tkinter import ttk
#
#
# def greet():
#     print(f"Hello, {user_name.get() or 'world'}")
#
#
# root = tk.Tk()
# root.title("Greeter")
#
# user_name = tk.StringVar()
#
# name_label = ttk.Label(root, text="Name: ")
# name_label.pack(side="left", padx=(0, 10))
# name_entry = ttk.Entry(root, width=15, textvariable=user_name)
# name_entry.pack(side="left")
# name_entry.focus()
#
# greet_button = ttk.Button(root, text="Greet", command=greet)
# greet_button.pack(side="left", fill="x", expand=True)
#
# root.mainloop()

# --------------------------------------------------------------------------------------------------------------
# Packing components
# --------------------------------------------------------------------------------------------------------------
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()

# tk.Label(root, text="Lable 1", bg="green").pack(side="left")
# tk.Label(root, text="Lable 2", bg="red").pack(side="top")
# # -------------
# tk.Label(root, text="Lable 1", bg="green").pack(side="left", fill="y")
# tk.Label(root, text="Lable 2", bg="red").pack(side="top", fill="x")
# # -------------
# tk.Label(root, text="Lable 1", bg="green").pack(side="left", fill="both")
# tk.Label(root, text="Lable 2", bg="red").pack(side="top", fill="both")
# # -------------
# tk.Label(root, text="Lable 1", bg="green").pack(side="left", fill="both", expand=True)
# tk.Label(root, text="Lable 2", bg="red").pack(side="top")
# # -------------
# tk.Label(root, text="Lable 1", bg="green").pack(side="top", fill="both", expand=True)
# tk.Label(root, text="Lable 2", bg="red").pack(side="top", fill="both", expand=True)
# # -------------
# tk.Label(root, text="Label left", bg="green").pack(side="left", expand=True, fill="both")
#
# tk.Label(root, text="Lable top", bg="red").pack(side="top", fill="both", expand=True)
# tk.Label(root, text="Lable top", bg="red").pack(side="top", fill="both", expand=True)
#
# tk.Label(root, text="Label left", bg="green").pack(side="left", expand=True, fill="both")
# tk.Label(root, text="Label left", bg="green").pack(side="left", expand=True, fill="both")
#
# root.mainloop()

# --------------------------------------------------------------------------------------------------------------
# Using frames for different layouts
# --------------------------------------------------------------------------------------------------------------
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# main = ttk.Frame(root)
# main.pack(side="left", fill="both", expand=True)
#
# tk.Label(main, text="Label top", bg="red").pack(side="top", fill="both", expand=True)
# tk.Label(main, text="Label top", bg="red").pack(side="top", fill="both", expand=True)
#
# tk.Label(root, text="Label left", bg="green").pack(side="left", fill="both", expand=True)
# root.mainloop()

# # --------------------------------------------------------------------------------------------------------------
# # Starting our text editor project
# # --------------------------------------------------------------------------------------------------------------
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


text_contents = dict()


def check_for_changes():
    current = get_text_widget()
    content = current.get("1.0", "end-1c")
    name = notebook.tab("current")["text"]

    if hash(content) != text_contents[str(current)]:
        if name[-1] != "*":
            notebook.tab("current", text=name + "*")
    elif name[-1] == "*":
        notebook.tab("current", text=name[:-1])


def close_current_tab():
    if current_tab_unsaved() and not confirm_close():
        return

    current_tab = get_current_tab()

    if len(notebook.tabs()) == 1:
        create_file()

    notebook.forget(current_tab)


def confirm_close():
    return messagebox.askyesno(
        message="You have unsaved changes. Are you sure you want to close?",
        icon="question",
        title="Unsaved Changes"
    )


def confirm_quit():
    unsaved = False

    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_widget = tab_widget.winfo_children()[0]
        content = text_widget.get("1.0", "end-1c")

        if hash(content) != text_contents[str(text_widget)]:
            unsaved = True
            break

    if unsaved and not confirm_close():
        return

    root.destroy()


def create_file(content="", title="Untitled"):
    container = ttk.Frame(notebook)
    container.pack()

    text_area = tk.Text(container)
    text_area.insert("end", content)
    text_area.pack(side="left", fill="both", expand=True)

    notebook.add(container, text=title)
    notebook.select(container)

    text_contents[str(text_area)] = hash(content)

    text_scroll = ttk.Scrollbar(container, orient="vertical", command=text_area.yview)
    text_scroll.pack(side="right", fill="y")
    text_area["yscrollcommand"] = text_scroll.set


def current_tab_unsaved():
    text_widget = get_text_widget()
    content = text_widget.get("1.0", "end-1c")
    return hash(content) != text_contents[str(text_widget)]


def get_current_tab():
    return notebook.nametowidget(notebook.select())


def get_text_widget():
    current_tab = get_current_tab()
    text_widget = current_tab.winfo_children()[0]

    return text_widget


def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    try:
        filename = os.path.basename(file_path)

        with open(file_path, "r") as file:
            content = file.read()

    except (AttributeError, FileNotFoundError):
        print("Open operation cancelled")
        return

    create_file(content, filename)


def save_file():
    file_path = filedialog.asksaveasfilename()

    try:
        filename = os.path.basename(file_path)
        text_widget = get_text_widget()
        content = text_widget.get("1.0", "end-1c")  # end except the last character which is a new line

        with open(file_path, "w") as file:
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    notebook.tab("current", text=filename)
    text_contents[str(text_widget)] = hash(content)


def show_about_info():
    messagebox.showinfo(
        title="About",
        message="The Text Editor is a simple tabbed text editor designed to help you learn Tkinter."
    )


root = tk.Tk()
root.title("Text Editor")
root.option_add("*tearOff", False)  # the-complete-python-course - lecon 265

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=1, pady=(4, 0))

menubar = tk.Menu()
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)

menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=help_menu, label="Help")

file_menu.add_command(label="New", command=create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open...", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Close Tab", command=close_current_tab, accelerator="Ctrl+Q")
file_menu.add_command(label="Exit", command=confirm_quit)

help_menu.add_command(label="About", command=show_about_info)

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

create_file()

root.bind("<KeyPress>", lambda event: check_for_changes())
root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-q>", lambda event: close_current_tab())
root.bind("<Control-s>", lambda event: save_file())

root.mainloop()

######################################## listbox ######################################
# ------------------------------
# listbox single choice

# from tkinter import *
#
# ws = Tk()
# ws.title('Python Guides')
# ws.geometry('400x300')
# ws.config(bg='#446644')
#
# def showSelected():
#     show.config(text=lb.get(ANCHOR))
#
#
# lb = Listbox(ws)
# lb.pack()
# lb.insert(0, 'red')
# lb.insert(1, 'green')
# lb.insert(2, 'yellow')
# lb.insert(3, 'blue')
#
# Button(ws, text='Show Selected', command=showSelected).pack(pady=20)
# show = Label(ws)
# show.pack()
#
# ws.mainloop()

# ------------------------------
# Listbox multiple choice

# from tkinter import *
#
# ws = Tk()
# ws.title('Python Guides')
# ws.geometry('400x300')
#
# var = StringVar()
#
#
# def showSelected():
#     countries = []
#     cname = lb.curselection()
#     for i in cname:
#         op = lb.get(i)
#         countries.append(op)
#     for val in countries:
#         print(val)
#
#
# show = Label(ws, text="Select Your Country", font=("Times", 14), padx=10, pady=10)
# show.pack()
# lb = Listbox(ws, selectmode="multiple")
# lb.pack(padx=10, pady=10, expand=YES, fill="both")
#
# x = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Australia", "Brazil", "Canada", "China", "Iceland",
#      "Israel", "United States", "Zimbabwe"]
#
# for item in range(len(x)):
#     lb.insert(END, x[item])
#     lb.itemconfig(item, bg="#bdc1d6")
#
# Button(ws, text="Show Selected", command=showSelected).pack()
# ws.mainloop()

# ------------------------------
# # listbox multiple choices + add an entry in the listbox
# from tkinter import *
# from tkinter import ttk
#
#
# # import tkinter
#
#
# def selection():
#     if Lb1.curselection() != ():
#         for i in Lb1.curselection():
#             print(Lb1.get(i))
#     else:
#         print("Veuillez selectionner au moins une valeur")
#
#
# def start():
#     Lb1.delete(0, 5)
#     Lb1.pack()
#
#
# def recupVal():
#     # # original
#     # print(entry_field.get())
#     # Lb1.insert(Lb1.size(), entry_field.get())
#     # delete()
#
#     # # Test pour le jeux ortho
#     list1 = ["Python", "Perl", "C", "PHP", "JSP", "Ruby"]
#     list2 = []
#     for i, listbox_entry in enumerate(Lb1.get(0, END)):
#         list2.append(listbox_entry)
#
#     for element in list2:
#         if element in list1:
#             list1.remove(element)
#
#     print(f"list1 {list1}")
#     print(f"list2 {list2}")
#
#
# def delete():
#     entry_field.delete(0, 'end')
#
#
# root = Tk()
#
# Lb1 = Listbox(root, selectmode=MULTIPLE)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")
#
# Lb1.pack()
#
# quit_button = ttk.Button(text="Quit", command=root.destroy).pack()
# valid_button = ttk.Button(text="Validate", command=selection).pack()
#
# start_button = ttk.Button(text="Start", command=start).pack()
#
# button = Button(root, text="Valider", command=recupVal).pack()
#
# label_field = Label(root, text="add a word").pack(side=LEFT)
#
# entry_field = Entry(root, bd=5)
# entry_field.pack(side=RIGHT)
#
# root.mainloop()

# --------------------------------------------------------------------------------------------------------------

# # Create a window object
# window = tk.Tk()
#
# label = tk.Label(
#     text="Hello, Tkinter",
#     fg="white",
#     bg="black",
#     width=10,
#     height=10).pack()
#
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow"
# ).pack()
# window.mainloop()

# --------------------

# def add_name():
#     name = entry.get()
#     print(name)
#
#
# def delete_name():
#     entry.delete(0, tk.END)
#
#
# def insert_name():
#     entry.insert(0, "Python")
#     entry.insert(0, "Real ")
#
#
# label = tk.Label(window, text="Name")
# entry = tk.Entry(window)
# button_Name = tk.Button(window, text="Validate", command=add_name)
# button_Delete = tk.Button(window, text="Delete", command=delete_name)
# button_Insert = tk.Button(window, text="Insert", command=insert_name)
# label.pack()
# entry.pack()
# button_Name.pack(side=LEFT)
# button_Delete.pack(side=LEFT)
# button_Insert.pack(side=LEFT)

# window.mainloop()


# --------------------

# def Get():
#     print(text_box.get("1.0", tk.END))
#
#
# def Delete_charactere():
#     text_box.delete("1.0")
#
#
# def Delete_All():
#     text_box.delete("1.0", tk.END)
#
#
# def Insert():
#     text_box.insert("1.0", "Hello")
#
#
# def Insert2():
#     text_box.insert("2.0", " world!")
#
#
# def InsertAtTheEnd():
#     text_box.insert(tk.END, "\nPut me on at the end!")
#
#
# text_box = tk.Text(window)
# button_Delete_Charactere = tk.Button(window, text="Delete Char", height=1, width=12,  command=Delete_charactere)
# button_Delete_All = tk.Button(window, text="Delete All", height=1, width=12,  command=Delete_All)
# button_Insert = tk.Button(window, text="Insert", height=1, width=12,  command=Insert)
# button_Insert2 = tk.Button(window, text="Insert 2", height=1, width=12,  command=Insert2)
# button_InsertAtTheEnd = tk.Button(window, text="Insert at the end", height=1, width=12,  command=InsertAtTheEnd)
# button_Get = tk.Button(window, text="Get", height=1, width=12, command=Get)
# text_box.pack(side=RIGHT)
# button_Insert.pack(side=TOP)
# button_Insert2.pack(side=TOP)
# button_InsertAtTheEnd.pack(side=TOP)
# button_Delete_Charactere.pack(side=TOP)
# button_Delete_All.pack(side=TOP)
# button_Get.pack(side=TOP)
#
# window.mainloop()

# --------------------
# frame_a = tk.Frame()
# frame_b = tk.Frame()
#
#
# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()
#
# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()
#
# frame_a.pack()
# frame_b.pack()
#
# window.mainloop()

# --------------------

# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
#
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()

# window.mainloop()

# --------------------

# # Exercice: Write a complete script that displays an Entry widget that’s 40 text units wide and has a white background
# # and black text. Use .insert() to display text in the widget that reads "What is your name?".
# entry = tk.Entry(window, width=40, bg="white", fg="black")
# entry.pack()
#
# entry.insert(0, "What is your name")
#
# window.mainloop()

# --------------------

# Controlling Layout with Geometry Managers
# The .pack() Geometry Manager

# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# window.mainloop()

# --------------------

# # The .place() Geometry Manager
# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()
#
# label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
# label1.place(x=0, y=0)
#
# label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
# label2.place(x=75, y=75)
#
# window.mainloop()

# --------------------

# The .grid() Geometry Manager

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
#     for j in range(3):
#         frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()

# --------------------


# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)
#
# label1 = tk.Label(text="A")
# label1.grid(row=0, column=0, sticky="n")
#
# label2 = tk.Label(text="B")
# label2.grid(row=1, column=0, sticky="n")
#
# window.mainloop()

# --------------------

# window.rowconfigure(0, minsize=50)
# window.columnconfigure([0, 1, 2, 3], minsize=50)
#
# label1 = tk.Label(text="1", bg="black", fg="white")
# label2 = tk.Label(text="2", bg="black", fg="white")
# label3 = tk.Label(text="3", bg="black", fg="white")
# label4 = tk.Label(text="4", bg="black", fg="white")
#
# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1, sticky="ew")
# label3.grid(row=0, column=2, sticky="ns")
# label4.grid(row=0, column=3, sticky="nsew")
#
# window.mainloop()

# --------------------

# # Exercice: B
# # https://realpython.com/python-gui-tkinter/#controlling-layout-with-geometry-managers
# # Below is an image of an address entry form made with Tkinter.
# # An address entry form window built with Tkinter
# #
# # Write a complete script that re-creates the window. You may use any geometry manager you like.
#
# window.geometry("590x240")
# window.title("Address Entry Form")
#
# labels = ["First Name",
#           "Last Name",
#           "Address Line1",
#           "Address Line2",
#           "City",
#           "State/Province",
#           "Postal Code",
#           "Country"]
# initial_frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5, width=590, height=242)
# foot_frame = tk.Frame(master=window, width=560, height=20)
# midle_frame = tk.Frame(master=window, borderwidth=1, width=590, height=280)
#
#
# for i in range(len(labels)):
#
#     frame = tk.Frame(master=midle_frame, borderwidth=1)
#     frame.grid(row=i, sticky="e")
#     label = tk.Label(master=frame, text=labels[i])
#     label.grid(row=i)
#
#     for j in range(1, 2):
#         frame = tk.Frame(master=midle_frame, relief=tk.RAISED, borderwidth=1)
#         frame.grid(row=i, column=j)
#         entry = tk.Entry(master=frame, width=80, bg="white")
#         entry.pack(side=tk.RIGHT)
#
#
# initial_frame.grid(row=1, sticky="n")
# midle_frame.grid(row=1, pady=5, sticky="n")
# foot_frame.grid(row=1, padx=5, sticky="se")
#
# label1 = tk.Label(master=foot_frame, relief=tk.RAISED, borderwidth=2, width=84, height=2)
# button1 = tk.Button(master=foot_frame, text="Submit")
# button2 = tk.Button(master=foot_frame, text="Clear")
#
# label1.grid()
# button1.grid(row=0, sticky="e", padx=10)
# button2.grid(row=0, sticky="e", padx=70)
# window.mainloop()
#
# #####################
# # Solution possible #
# #####################
#
# # Create a new window with the title "Address Entry Form"
# window = tk.Tk()
# window.title("Address Entry Form")
#
# # Create a new frame `frm_form` to contain the Label
# # and Entry widgets for entering address information.
# frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# # Pack the frame into the window
# frm_form.pack()
#
# # List of field labels
# labels = [
#     "First Name:",
#     "Last Name:",
#     "Address Line 1:",
#     "Address Line 2:",
#     "City:",
#     "State/Province:",
#     "Postal Code:",
#     "Country:",
# ]
#
# # Loop over the list of field labels
# for idx, text in enumerate(labels):
#     # Create a Label widget with the text from the labels list
#     label = tk.Label(master=frm_form, text=text)
#     # Create an Entry widget
#     entry = tk.Entry(master=frm_form, width=50)
#     # Use the grid geometry manager to place the Label and
#     # Entry widgets in the row whose index is idx
#     label.grid(row=idx, column=0, sticky="e")
#     entry.grid(row=idx, column=1)
#
# # Create a new frame `frm_buttons` to contain the
# # Submit and Clear buttons. This frame fills the
# # whole window in the horizontal direction and has
# # 5 pixels of horizontal and vertical padding.
# frm_buttons = tk.Frame()
# frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
#
# # Create the "Submit" button and pack it to the
# # right side of `frm_buttons`
# btn_submit = tk.Button(master=frm_buttons, text="Submit")
# btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
#
# # Create the "Clear" button and pack it to the
# # right side of `frm_buttons`
# btn_clear = tk.Button(master=frm_buttons, text="Clear")
# btn_clear.pack(side=tk.RIGHT, ipadx=10)
#
# # Start the application
# window.mainloop()

# --------------------

# # Create an event handler
# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)
#
#
# # Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)

# --------------------

# def handle_click(event):
#     print("The button was clicked!")
#
#
# button = tk.Button(text="Click me!")
#
# button.bind("<Button-1>", handle_click)
#
# button.pack()
#
# # Run the event loop
# window.mainloop()

# --------------------

# def increase():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"
#
#
# def decrease():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"
#
#
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)
#
# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# btn_decrease.grid(row=0, column=0, sticky="nsew")
#
# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)
#
# btn_increase = tk.Button(master=window, text="+", command=increase)
# btn_increase.grid(row=0, column=2, sticky="nsew")
#
# window.mainloop()

# --------------------
# # Write a program that simulates rolling a six-sided die. There should be one button with the text "Roll".
# # When the user clicks the button, a random integer from 1 to 6 should be displayed.
# #
# # Hint: You can generate a random number using randint() in the random module. If you’re not familiar with the
# # random module, then check out Generating Random Data in Python (Guide) for more information.
# window.title("Rolling a six-side dice")
# window.rowconfigure([0, 1], minsize=50, weight=1)
# window.columnconfigure(0, minsize=50, weight=1)
#
# from random import randint
#
#
# def roll():
#     lbl_value["text"] = str(randint(1, 6))
#
#
# button_Roll = Button(master=window, text="Roll", height=5, width=20, command=roll)
# lbl_value = tk.Label(master=window, height=5, width=20, text="?")
#
# button_Roll.grid(row=0, column=0, sticky="nsew")
# lbl_value.grid(row=1, column=0)
#
# window.mainloop()

# --------------------

# def calcul():
#     degres_f = entry.get()
#     result = float((int(degres_f) - 32) * (5 / 9))
#     label2["text"] = f"{result:1.2f}"
#
#
# window.title("Temperature Converter")
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 4], minsize=30, weight=1)
# entry = tk.Entry(window, bd=5)
# label1 = tk.Label(window, text="\N{DEGREE FAHRENHEIT}")
# buttonCalcul = tk.Button(window, text="\N{RIGHTWARDS BLACK ARROW}", command=calcul)
# label2 = tk.Label(window, text="")
# label3 = tk.Label(window, text="\N{DEGREE CELSIUS}")
#
# entry.grid(row=0, column=0)
# label1.grid(row=0, column=1)
# buttonCalcul.grid(row=0, column=2)
# label2.grid(row=0, column=3)
# label3.grid(row=0, column=4)
# window.mainloop()

# --------------------

# # Building a Text Editor (Example App)
# #
# # In this section, you’ll build a text editor application that can create, open, edit, and save text files. There are
# # three essential elements in the application:
# #
# #     A Button widget called btn_open for opening a file for editing
# #     A Button widget called btn_save for saving a file
# #     A TextBox widget called txt_edit for creating and editing the text file
# #
# # The three widgets will be arranged so that the two buttons are on the left-hand side of the window, and the text box
# # is on the right-hand side. The whole window should have a minimum height of 800 pixels, and txt_edit should have a
# # minimum width of 800 pixels. The whole layout should be responsive so that if the window is resized, then txt_edit is
# # resized as well. The width of the Frame holding the buttons should not change, however.
# #
# # Here’s a sketch of how the window will look:
# # A design sketch for a text editor application
# #
# # You can achieve the desired layout using the .grid() geometry manager. The layout contains a single row and two
# # columns:
# #
# #     A narrow column on the left for the buttons
# #     A wider column on the right for the text box
# #
# # To set the minimum sizes for the window and txt_edit, you can set the minsize parameters of the window methods
# # .rowconfigure() and .columnconfigure() to 800. To handle resizing, you can set the weight parameters of these methods
# # to 1.
# #
# # In order to get both buttons into the same column, you’ll need to create a Frame widget called fr_buttons. According
# # to the sketch, the two buttons should be stacked vertically inside of this frame, with btn_open on top. You can do
# # that with either the .grid() or .pack() geometry manager. For now, you’ll stick with .grid() since it’s a little
# # easier to work with.
#
# window.title("Text Editor")
#
# btn_open = Button(text="OPEN")
# btn_saveas = Button(text="SaveAs")
#
# window.rowconfigure([0, 1], minsize=150, weight=0)
# window.columnconfigure([0, 1], minsize=30, weight=0)
#
# txt_edit = Text(window)
#
# btn_open.grid(row=0, column=0, sticky="ne", padx=10, pady=10)
# btn_saveas.grid(row=0, column=0, sticky="ne", padx=10, pady=60)
# txt_edit.grid(row=0, column=1, sticky="ns", rowspan=2, padx=10, pady=10)
#
# window.mainloop()
