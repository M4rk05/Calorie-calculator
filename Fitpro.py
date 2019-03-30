# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
import codecs
program = True
male = 66.5
female = 665
over = ''
choose = ''
activity = ''
sex_test = ''
choice = ''
score = ''
total = ''
activity_choice = str('')
language = ''
error_test = ''
weight_conv = ''
height_conv = ''


#  default behaviour of destroying the: choice language window
def master_pressed_x():
    global program
    program = False
    master.destroy()


#  default behaviour of destroying the: main program window
def window_pressed_x():
    global program
    program = False
    window.destroy()


#  on click: clear program window to default
def clear():
    display_text.set('')
    display_text_age.set('')
    display_text_weight.set('')
    display_text_height.set('')
    display.configure(state="disable")


def male_click():
    global sex_test
    global choose
    sex_test = ''
    sex_test = 'male'
    choose = ''
    choose = male
    pass


def female_click():
    global sex_test
    global choose
    sex_test = ''
    sex_test = 'female'
    choose = ''
    choose = female
    pass


#  on click: checking entry widgets(unit test) and assigning numbers to variables + invoke func. calculate
def calculate_click():
    global age
    global height
    global weight
    global error_test
    global weight_conv
    global height_conv
    age = ''
    height = ''
    weight = ''
    try:
        weight = (float(display_text_weight.get())/weight_conv)
        height = (float(display_text_height.get())/height_conv)
        age = float(display_text_age.get())
        calculate()
    except ValueError:
        if weight == '':
            error_test = 'input weight'
        elif height == '':
            error_test = 'input height'
        elif age == '':
            error_test = 'input age'
        display.configure(state="normal")
        display_text.set('Error: ' + error_test)
        display.configure(state="disable")


#  calculate algorithm
def calculate():
    global score
    global sex_test
    global total
    try:
        if sex_test == 'male':
            score = eval('choose+(13.7*weight)+(5*height)-(6.8*age)')
            total = eval('score*activity')
            display_text.set(total)
            display.configure(state="normal")
        if sex_test == 'female':
            score = eval('choose+(9.6*weight)+(1.85*height)-(4.7*age)')
            total = eval('score*activity')
            display_text.set(total)
            display.configure(state="normal")
        if sex_test == '':
            display.configure(state="normal")
            display_text.set('Error: choose Sex')
            display.configure(state="disable")
    except ValueError:
        display.configure(state="normal")
        display_text.set('Error')
        display.configure(state="disable")
    except TypeError:
        display.configure(state="normal")
        display_text.set('Error')
        display.configure(state="disable")


def list_box_select(index):
    global activity_choice
    global activity
    activity_choice = ct_listbox.get(ct_listbox.curselection())
    if activity_choice == ct_listbox.get(ct_listbox.index([0])):
        activity = float('1.0')
    if activity_choice == ct_listbox.get(ct_listbox.index([1])):
        activity = float('1.2')
    if activity_choice == ct_listbox.get(ct_listbox.index([2])):
        activity = float('1.4')
    if activity_choice == ct_listbox.get(ct_listbox.index([3])):
        activity = float('1.6')
    if activity_choice == ct_listbox.get(ct_listbox.index([4])):
        activity = float('1.8')
    if activity_choice == ct_listbox.get(ct_listbox.index([5])):
        activity = float('2.0')


#  loading text from polish.txt and entering it the list
def polish_language():
    try:
        ct_listbox.delete(0, END)
        with codecs.open("polish.txt", "r", "utf8") as file:
            line = file.readlines()
            for a in line:
                ct_listbox.insert(6, a)
            ct_listbox.update()
    except UnicodeDecodeError:
        print("error")


#  loading text from english.txt and entering it the list
def english_language():
    global ct_listbox
    ct_listbox.delete(0, END)
    with open("english.txt", "r") as file:
        line = file.readlines()
        for a in line:
            ct_listbox.insert(6, a)
        ct_listbox.update()


#  button quit action : breaking mainloop and close window
def quit_click():
    global program
    global window
    program = False
    window.destroy()


#  set global language (from selected)
def ok():
    global language
    global program
    language = str(variable.get())
    master.destroy()


#  invoke: Choice language window
def choice_language():
    global master
    global variable
    global program
    options = ["Polish", "English"]
    master = tk.Tk()
    master.protocol('WM_DELETE_WINDOW', master_pressed_x)
    master.geometry('185x90')
    master.title('Be Fit 1.0')
    variable = StringVar(master)
    variable.set(options[0])
    label_description = tk.Label(master, text="Select language:")
    label_description.pack()
    w = OptionMenu(master, variable, *options)
    w.pack()
    button = Button(master, text="Select", command=ok)
    button.pack()
    master.mainloop()


#  breaking window mainloop and start form beginning program mainloop
def change_language_click():
    global program
    global window
    window.destroy()


#  start mainloop
while program is True:
    try:
        if program is True:
            choice_language()
            if language == 'Polish':
                label_activity_lang = 'Wybierz rodzaj aktywności:'
                button_clear_lang = 'Wyczyść'
                button_calculate_lang = 'Oblicz'
                label_age_lang = 'Wiek'
                label_weight_lang = 'Waga'
                label_height_lang = 'Wzrost'
                button_male_lang = 'Mężczyzna'
                button_female_lang = 'Kobieta'
                label_kcaltarget_lang = 'Zapotrzebowanie kaloryczne'
                button_quit_lang = 'Zamknij'
                label_weight_unit_lang = 'kg'
                label_height_unit_lang = 'cm'
                weight_conv = float('1')
                height_conv = float('1')
            if language == 'English':
                label_activity_lang = 'Choose your activity level:'
                button_clear_lang = 'Clear'
                button_calculate_lang = 'Calculate'
                label_age_lang = 'Age'
                label_weight_lang = 'Weight'
                label_height_lang = 'Height'
                button_male_lang = 'Male'
                button_female_lang = 'Female'
                label_kcaltarget_lang = 'CALORIES/DAY'
                button_quit_lang = 'Close'
                label_weight_unit_lang = 'lbs'
                label_height_unit_lang = 'ft'
                weight_conv = float('2.2046226218')
                height_conv = float('0.032808399')

            window = tk.Tk()
            window.protocol('WM_DELETE_WINDOW', window_pressed_x)
            window.geometry('510x460')
            window.title('Be Fit 1.0')
            C = tk.Canvas(window, bg="blue", height=250, width=300)
            filename = tk.PhotoImage(file="fit.png")
            background_label = tk.Label(window, image=filename)
            background_label.place(x=1, y=210)

            menu = Menu(window)
            filemenu = Menu(menu, tearoff=0)
            filemenu.add_command(label="Change language", command=change_language_click)
            filemenu.add_separator()
            filemenu.add_command(label="Exit", command=quit_click)
            menu.add_cascade(label="File", menu=filemenu)
            window.config(menu=menu)

            button_quit = tk.Button(window, text=button_quit_lang, command=quit_click, width=7)
            button_quit.pack()
            button_quit.place(x=445, y=5)

            label_kcaltarget = tk.Label(window, text=label_kcaltarget_lang)
            label_kcaltarget.place(x=30, y=40)
            display_text = tk.StringVar()
            display = tk.Entry(window, textvariable=display_text)
            display.configure(state="disabled")
            display.place(x=190, y=40)

            button_male = tk.Button(window, text=button_male_lang, command=male_click, width=8)
            button_male.pack()
            button_male.place(x=30, y=60)

            button_female = tk.Button(window, text=button_female_lang, command=female_click, width=6)
            button_female.pack()
            button_female.place(x=99, y=60)

            label_weight = tk.Label(window, text=label_weight_lang)
            label_weight.place(x=30, y=90)
            display_text_weight = tk.StringVar()
            display_weight = tk.Entry(window, width=11, textvariable=display_text_weight)
            display_weight.place(x=81, y=90)
            label_weight_unit = tk.Label(window, text=label_weight_unit_lang)
            label_weight_unit.pack()
            label_weight_unit.place(x=150, y=90)

            label_height = tk.Label(window, text=label_height_lang)
            label_height.place(x=30, y=120)
            display_text_height = tk.StringVar()
            display_height = tk.Entry(window, width=11, textvariable=display_text_height)
            display_height.place(x=81, y=120)
            label_height_unit = tk.Label(window, text=label_height_unit_lang)
            label_height_unit.pack()
            label_height_unit.place(x=150, y=120)

            label_age = tk.Label(window, text=label_age_lang)
            label_age.place(x=30, y=150)
            display_text_age = tk.StringVar()
            display_age = tk.Entry(window, width=11, textvariable=display_text_age)
            display_age.place(x=81, y=150)

            button_calculate = tk.Button(window, text=button_calculate_lang, command=calculate_click, width=7)
            button_calculate.pack()
            button_calculate.place(x=30, y=180)

            button_clear = tk.Button(window, text=button_clear_lang, command=clear, width=7)
            button_clear.pack()
            button_clear.place(x=93, y=180)

            label_activity = tk.Label(window, text=label_activity_lang)
            label_activity.pack()
            label_activity.place(x=180, y=70)

            ct_listbox = tk.Listbox(window, width=52, height=6, exportselection=False)
            ct_listbox.pack()
            ct_listbox.place(x=180, y=88)
            ct_listbox.bind('<<ListboxSelect>>', list_box_select)

            if language == 'Polish':
                polish_language()
            elif language == 'English':
                english_language()
            window.mainloop()
        else:
            break
    except NameError:
        program = False
